#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import rospy
import geometry_msgs.msg
from gnss_pkg.msg import LaneLineArray, LaneLine
import psycopg2

def parse_database_row(row):
    # 解析数据库行数据并返回车道线消息类型变量
    lane_line = LaneLine()

    lane_line.id = int(row[1])  # 使用id作为id字段的值
    # lane_line.id = int(row[0])  # 使用objectid作为id字段的值
    lane_line.type = 1  # 默认设置为1

    x_val = float(row[4])  # 获取x坐标值
    y_val = float(row[5])  # 获取y坐标值

    point = geometry_msgs.msg.Point()
    point.x = x_val
    point.y = y_val
    point.z = 0.0

    lane_line.x.append(x_val)
    lane_line.y.append(y_val)
    lane_line.points.append(point)  # 将点的坐标添加到points列表中

    lane_line.current_lane_num = 1  # 默认设置为1

    return lane_line


def read_data_from_database():
    # 连接到数据库，查询数据，并逐行解析
    conn = psycopg2.connect(dbname='sde', user='postgres', password='123456', host='192.168.88.135')
    cursor = conn.cursor()

    query = "SELECT objectid, id, orig_fid, pointorder, point_x, point_y FROM test_412_linkpoints"
    cursor.execute(query)
    rows = cursor.fetchall()

    # 逐行解析数据并填写到车道线数组变量中
    lane_lines = []

    for row in rows:
        lane_line = parse_database_row(row)
        lane_lines.append(lane_line)   
    
    # 计算每个点的frenet的s坐标值
    s_vals = [0.0]
    lane_lines[0].s=s_vals
    if len(lane_lines) > 1:  # 当有多个点时进行计算
        for i in range(1, len(lane_lines)):
            dx = lane_lines[i].x[0] - lane_lines[i-1].x[0]
            dy = lane_lines[i].y[0] - lane_lines[i-1].y[0]
            ds = (dx**2 + dy**2)**0.5
            s_val = s_vals[-1] + ds
            lane_lines[i].s.append(s_val)
            s_vals.append(s_val)
    

    # 关闭数据库连接
    cursor.close()
    conn.close()

    lane_line_array = LaneLineArray()
    lane_line_array.lines = lane_lines

    return lane_line_array


def main():
    rospy.init_node('database_reader')

    # 读取数据
    lane_line_array = read_data_from_database()
    # 发布数据到ROS topic
    pub = rospy.Publisher('road_lane', LaneLineArray, queue_size=10)
    print("road_lane初始化成功")
    rate = rospy.Rate(10)  # 设置发布频率为10Hz
    
    while not rospy.is_shutdown():
        pub.publish(lane_line_array)
        rate.sleep()

if __name__ == '__main__':
    main()
