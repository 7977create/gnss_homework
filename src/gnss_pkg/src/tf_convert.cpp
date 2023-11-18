#include <ros/ros.h>
#include <geometry_msgs/PointStamped.h>
#include <tf2_ros/transform_broadcaster.h>
#include <gnss_pkg/location.h>
#include <gnss_pkg/coordinate.h>
#include "tf2/LinearMath/Quaternion.h"
#include <GeographicLib/LocalCartesian.hpp> 
/**************引入写数据头文件******************/
#include<iostream>
#include<string>
#include<fstream>
/****************发布path***************/ 
#include <nav_msgs/Path.h>
#include <visualization_msgs/Marker.h>

using namespace std;


class GPSToENUConverter
{
public:
  GPSToENUConverter();
  void gpsCallback(const gnss_pkg::location::ConstPtr& msg);
  // void timerCallback(const ros::TimerEvent&);//timer to path point publish


private:
// 句柄、订阅节点、发布节点、tf广播节点、写入文件路径、
  ros::NodeHandle nh;
  ros::Subscriber sub_;
  ros::Publisher pub_;
  ros::Publisher marker_pub_;
  boost::shared_ptr<tf2_ros::TransformBroadcaster> tf_broadcaster_;
  //文档储存位置
  string fileName02 = "/home/ubuntu18/learning/navi_msg.txt"; 
  // 设置参考坐标系的原点
  double reference_lat_= 29.74668727;
  double reference_lon_ = 106.55382867;
  double reference_alt_= 239.0;
  ofstream ofm02;
 // 存储行使路径点
  std::vector<geometry_msgs::Point> path_points_;
  // ros::Timer timer_;
};

int main(int argc, char** argv)
{
  setlocale(LC_ALL,"");
  ros::init(argc, argv, "gps_to_enu_converter");
  std::cout<<"节点初始化成功"<<std::endl;
  GPSToENUConverter converter;
  ros::spin();
  return 0;
}

GPSToENUConverter::GPSToENUConverter()
{
  // gps驱动订阅器、xy坐标发布器和TF广播器
  sub_ = nh.subscribe("navi_msg", 10, &GPSToENUConverter::gpsCallback, this);
  pub_=nh.advertise<gnss_pkg::coordinate>("coordinate",10);
  marker_pub_ = nh.advertise<visualization_msgs::Marker>("marker", 10);
  tf_broadcaster_.reset(new tf2_ros::TransformBroadcaster());
  std::cout<<"订阅器和TF广播器初始化成功"<<std::endl;
  //默认以截断的形式打开文件，且会覆盖原有内容
  ofm02.open(fileName02); 

  // timer_ = nh.createTimer(ros::Duration(0.1), &GPSToENUConverter::timerCallback, this); // 设置定时器的周期为0.1s，可以根据需要调整
}

void GPSToENUConverter::gpsCallback(const gnss_pkg::location::ConstPtr& msg)
{
  // 接收到GPS坐标消息，进行转换
  double lat = msg->latitude;
  double lon = msg->longtitude; 
  double alt = msg->altitude;  
  // 存储转换后的ENU坐标
  double local_E, local_N, local_U; 

  // 设置坐标原点  经纬度转ENU
  GeographicLib::LocalCartesian geo_converter;
  geo_converter.Reset(reference_lat_,reference_lon_, reference_alt_);
  geo_converter.Forward(lat, lon, alt, local_E, local_N, local_U);
  // std::cout << "转东:" << local_E << ",转北：" << local_N << ",转天：" << local_U << std::endl;

 // 发布xy坐标
 gnss_pkg::coordinate cdt;
 cdt.x=local_E;
 cdt.y=local_N;
 pub_.publish(cdt);

  // 构造TF变换并发布
  geometry_msgs::TransformStamped transformStamped;
  transformStamped.header.stamp = ros::Time::now();
  transformStamped.header.frame_id = "world";
  transformStamped.child_frame_id = "gps_tf";
  transformStamped.transform.translation.x = local_E;
  transformStamped.transform.translation.y = local_N;
  transformStamped.transform.translation.z = local_U;

  // 创建一个标记消息对象
  visualization_msgs::Marker marker_msg;
  marker_msg.header.stamp = ros::Time::now();
  marker_msg.header.frame_id = "world";
  marker_msg.ns = "car_path";
  marker_msg.action = visualization_msgs::Marker::ADD;
  marker_msg.pose.orientation.w = 1.0;
  marker_msg.type = visualization_msgs::Marker::LINE_STRIP;
  marker_msg.scale.x = 0.1;
  marker_msg.color.a = 1.0;
  marker_msg.color.r = 0.0;
  marker_msg.color.g = 0.0;
  marker_msg.color.b = 1.0;
  // 设置标记的位置
  geometry_msgs::Point point;
  point.x = local_E;
  point.y = local_N;
  point.z = local_U;
  // 将点添加到标记的点集中
  path_points_.push_back(point);
 
  // 发布标记信息
  if (path_points_.size() >= 2) {
      // 添加路径点到标记的点集中
      marker_msg.points = path_points_;
      // 发布标记信息
      marker_pub_.publish(marker_msg);
  }

  // xy坐标写入文件(后续要更改)根据这个文档里面的数据进行分析定位精度
  ofm02<<"("<<local_E<<","<<local_N<<") ";

  // 四元数变换tfs相当于transformStamped
  tf2::Quaternion qtn;
  qtn.setRPY(0,0,msg->heading* M_PI / 180.0);//偏航弧度制
  transformStamped.transform.rotation.x=qtn.getX();
  transformStamped.transform.rotation.y=qtn.getY();
  transformStamped.transform.rotation.z=qtn.getZ();
  transformStamped.transform.rotation.w=qtn.getW();

  // 广播发布
  tf_broadcaster_->sendTransform(transformStamped);


// //add path message
//   geometry_msgs::Point point;
//   point.x = local_E;
//   point.y = local_N;
//   point.z = local_U;
//   path_points_.push_back(point);
}


// void GPSToENUConverter::timerCallback(const ros::TimerEvent&)
// {
//   visualization_msgs::Marker marker_msg;
//   marker_msg.header.stamp = ros::Time::now();
//   marker_msg.header.frame_id = "world";
//   marker_msg.ns = "car_path";
//   marker_msg.action = visualization_msgs::Marker::ADD;
//   marker_msg.pose.orientation.w = 1.0;
//   marker_msg.type = visualization_msgs::Marker::LINE_STRIP;
//   marker_msg.scale.x = 0.1;
//   marker_msg.color.a = 1.0;
//   marker_msg.color.r = 0.0;
//   marker_msg.color.g = 0.0;
//   marker_msg.color.b = 1.0;
//   marker_msg.points = path_points_;

//   if (path_points_.size() >= 2) {
//     marker_pub_.publish(marker_msg);
//   }
// }