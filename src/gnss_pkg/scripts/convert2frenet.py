#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
import numpy as np
from gnss_pkg.msg import LaneLineArray, LaneLine,coordinate,CurPose,location
import math

class CartesianToFrenetConverter:
    def __init__(self):
        rospy.init_node('cartesian_to_frenet_converter')
        
        # 订阅小车自身位置信息的话题
        self.coordinate_sub = rospy.Subscriber('coordinate', coordinate, self.coordinate_callback)
        
        self.gps_sub = rospy.Subscriber('navi_msg',location, self.gps_callback)
        # 订阅地图数据信息的话题
        self.lane_lines_sub = rospy.Subscriber('road_lane', LaneLineArray, self.lane_lines_callback)
        
        # 创建一个发布器发布小车的frenet坐标信息
        self.frenet_pub = rospy.Publisher('cur_pose_all', CurPose, queue_size=10)
        
        # 保存车道线数据
        self.lane_lines = None
        print("cartesian_to_frenet_converter初始化成功")

        
    def coordinate_callback(self, data):
        # 获取小车自身位置信息
        car_x = data.x
        car_y = data.y
        
        if self.lane_lines is not None:
            s, d = self.cartesian_to_frenet(car_x, car_y)
            
            # 创建一个CurPose消息类型的对象
            frenet_coord = CurPose()#CurPose
            frenet_coord.s = s
            frenet_coord.d = d
            frenet_coord.x = car_x
            frenet_coord.y = car_y
            frenet_coord.theta =self.gps_msg.heading*  math.pi  / 180.0     #弧度制

            # 发布frenet坐标信息
            self.frenet_pub.publish(frenet_coord)

    def gps_callback(self, data):
        # 保存gps数据信息
        self.gps_msg = data

    def lane_lines_callback(self, data):
        # 保存地图数据信息
        self.lane_lines = data.lines

    def cartesian_to_frenet(self, x, y):
        # 计算小车笛卡尔坐标转换为frenet坐标
        
        min_distance = float('inf')
        closest_point = None
        
        # 遍历车道线上的每个点，找到离小车最近的点
        for i in range(len(self.lane_lines) - 1):
            point1 = self.lane_lines[i]
            point2 = self.lane_lines[i+1]
            
            projection = self.calculate_projection(x, y, point1, point2)
            distance = self.calculate_distance(x, y, projection)
            
            if distance < min_distance:
                min_distance = distance
                closest_point = projection
        print(self.lane_lines[1].x)
        # 计算投影点在参考线上的路径长度（s值）
        s = closest_point.s[0]

        # 计算d值
        d = min_distance

        if closest_point.current_lane_num == 0:
            d=-1*d

        # rospy.loginfo("s: {}".format(s))
        # rospy.loginfo("d: {}".format(d))
        # print(closest_point.current_lane_num)
        return s, d
    
    
    def calculate_projection(self, x, y, point1, point2):
    # 计算点(x, y)在参考线上的投影点

        # 参考线上的点坐标
        x1 = point1.x[0]
        y1 = point1.y[0]
        x2 = point2.x[0]
        y2 = point2.y[0]

        # 计算参考线的方向向量
        direction_vector = np.array([x2 - x1, y2 - y1])

        # 计算从参考线起点到点(x, y)的向量
        point_vector = np.array([x - x1, y - y1])

        # 计算投影向量
        projection_vector = (np.dot(point_vector, direction_vector) / np.dot(direction_vector, direction_vector)) * direction_vector

        cross_product = np.cross(direction_vector, point_vector)

        # 计算投影点的坐标
        projection_x = x1 + projection_vector[0]
        projection_y = y1 + projection_vector[1]

        # 创建一个LaneLine类型的对象保存投影点的坐标和s值
        projection = LaneLine()
        projection.x = [projection_x]
        projection.y = [projection_y]

        # 根据夹角范围设置projection.current_lane_num的值
        if cross_product > 0:
        # 小车位于右侧
            projection.current_lane_num = 0
        else:
        # 小车位于左侧
             projection.current_lane_num = 2

        # 计算投影点的s值
        if np.dot(projection_vector, direction_vector) >= 0:
            projection.s = [point2.s[0] + np.linalg.norm(projection_vector)]
        else:
            projection.s = [point1.s[0] - np.linalg.norm(projection_vector)]

        return projection


    
    def calculate_distance(self, x, y, point):
        # 计算两点之间的距离
        dx = x - point.x[0]
        dy = y - point.y[0]
        distance = (dx**2 + dy**2) ** 0.5
        return distance
    
    def run(self):
        rospy.spin()

if __name__ == '__main__':
    converter = CartesianToFrenetConverter()
    converter.run()
