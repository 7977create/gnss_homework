#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import Float64
from geometry_msgs.msg import Point#, Pose, Quaternion
from visualization_msgs.msg import Marker
import psycopg2
import numpy as np

def connect_to_database():#正常连接数据库没问题
    conn = psycopg2.connect(dbname='sde', user='postgres', password='123456', host='192.168.88.135')
    return conn

def query_data():#成功读取数据库数据，没问题
    conn = connect_to_database()
    cur = conn.cursor()
    
    # 查询 test_412_leftpoints 表的数据
    cur.execute("SELECT point_x, point_y FROM test_412_leftpoints")
    rowsleft = cur.fetchall()
    # # 查询 test_412_rightpoints 表的数据
    cur.execute("SELECT point_x, point_y FROM test_412_rightpoints")
    rowsright= cur.fetchall()
    # # 查询 test_412_linkpoints 表的数据
    cur.execute("SELECT point_x, point_y FROM test_412_linkpoints")
    rowslink = cur.fetchall()

    return rowsleft,rowslink,rowsright

def fit_curve(data):#
    x = np.array([float(row[0]) for row in data])
    y = np.array([float(row[1]) for row in data])

    return x, y

def publish_data():
    rospy.init_node('db_reader', anonymous=True)

    pub01 = rospy.Publisher('leftpoints', Marker, queue_size=10)
    pub02 = rospy.Publisher('linkpoints', Marker, queue_size=10)
    pub03 = rospy.Publisher('rightpoints', Marker, queue_size=10)
    rate = rospy.Rate(10) # 10hz

    while not rospy.is_shutdown():
        dataleft,datalink,dataright = query_data()

        x_left, y_left = fit_curve(dataleft)
        x_link, y_link = fit_curve(datalink)
        x_right, y_right = fit_curve(dataright)

        msg_left = Marker()
        msg_left.header.frame_id = "world"
        msg_left.type = msg_left.LINE_STRIP
        msg_left.action = msg_left.ADD
        msg_left.scale.x = 0.1
        msg_left.color.a = 1.0
        msg_left.color.r = 1.0

        for i in range(len(x_left)):
            point = Point()
            point.x = x_left[i]
            point.y = y_left[i]
            point.z = 0.0
            msg_left.points.append(point)

        # 对于左边的点消息
        if len(x_left) > 0:
            point = Point()
            point.x = x_left[0]
            point.y = y_left[0]
            point.z = 0.0
            msg_left.points.append(point)

        msg_link = Marker()
        msg_link.header.frame_id = "world"
        msg_link.type = msg_link.LINE_STRIP
        msg_link.action = msg_link.ADD
        msg_link.scale.x = 0.1
        msg_link.color.a = 1.0
        msg_link.color.g = 1.0

        for i in range(len(x_link)):
            point = Point()
            point.x = x_link[i]
            point.y = y_link[i]
            point.z = 0.0
            msg_link.points.append(point)
        
        # 对于连接的点消息
        if len(x_link) > 0:
            point = Point()
            point.x = x_link[0]
            point.y = y_link[0]
            point.z = 0.0
            msg_link.points.append(point)

        msg_right = Marker()
        msg_right.header.frame_id = "world"
        msg_right.type = msg_right.LINE_STRIP
        msg_right.action = msg_right.ADD
        msg_right.scale.x = 0.1
        msg_right.color.a = 1.0
        msg_right.color.r = 1.0

        for i in range(len(x_right)):
            point = Point()
            point.x = x_right[i]
            point.y = y_right[i]
            point.z = 0.0
            msg_right.points.append(point)

            # 对于右边的点消息
        if len(x_right) > 0:
            point = Point()
            point.x = x_right[0]
            point.y = y_right[0]
            point.z = 0.0
            msg_right.points.append(point)

        pub01.publish(msg_left)
        pub02.publish(msg_link)
        pub03.publish(msg_right)
        rate.sleep()

if __name__ == '__main__':
    try:
        publish_data()
    except rospy.ROSInterruptException:
        pass
