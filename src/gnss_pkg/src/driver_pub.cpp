#include <ros/ros.h>
#include <iostream>
#include <unistd.h>
#include <string>
#include <vector>   
#include <sstream> 
#include <fstream>
#include <gnss_pkg/location.h>
#include "uart.h"


// 接收数组
char recvBuff[1024];

// 将字符串转换为不同类型的数值，如整数、浮点数等
template <typename Type>
Type stringToNum(const std::string &str)
{
	std::stringstream iss(str);
	Type num;
	iss >> num;
	return num;
}



int main( int argc, char **argv )
{
	std::cout<<"Program begins ... "<<std::endl;
	// 接受次数	指向接收缓冲区中确切数据位置的指针。
	int recvCount = 0;
	int previous = 0, rear = 0; 

	// 初始化ros节点创建ros句柄发布者对象
	ros::init( argc, argv, "location_publisher" );
	ros::NodeHandle n;
	ros::Publisher pub = n.advertise<gnss_pkg::location>( "navi_msg", 1);


	// 打开串口设置参数
	int uart_fd = open_port();
	std::cout<<"uart fd = "<<uart_fd <<std::endl;
	if( uart_fd > 0 ){
		if( set_opt( uart_fd ) != true ){
			std::cerr<<"set port failed ... "<<std::endl;
			return false;
		}
	}
	else{
		std::cerr<<"open port failed ..."<<std::endl;
		exit(-1);
	}
	sleep( 1 );



	std::string s1; 
	std::vector<std::string> arr1; // define a vector of string
	int position = 0;	
	gnss_pkg::location recvMsg;

	while(ros::ok()){
		memset( recvBuff, 0, sizeof( recvBuff ) );
		if( recvData( uart_fd, recvBuff, sizeof( recvBuff ) ) ){
			if( recvCount <= 1 ) recvCount ++;
			if( recvCount > 1 ){
				s1 = recvBuff;

				do{
					std::string tmp_s;
                    //找到逗号的位置   
					position = s1.find(",");   
                    //截取需要的字符串 
					tmp_s = s1.substr(0, position);      
                    //将已读取的数据删去 
					s1.erase(0, position + 1);
                    //将字符串压入容器中       
					arr1.push_back(tmp_s);       
				} while (position != -1);
	
				// int d0 = stringToNum<int>( arr1[1] ); // GPSWeek 
				// recvMsg.GPSWeek = d0;
				double d1 = stringToNum<double>( arr1[2] ); // GPSTime 时间
				recvMsg.GPStime = d1;
				double d2 = stringToNum<double>( arr1[3] ); // heading 航向角
				recvMsg.heading = d2;
				double d3 = stringToNum<double>( arr1[4] ); // Pitch俯仰角
				recvMsg.pitch = d3;
				double d4 = stringToNum<double>( arr1[5] ); // Roll翻滚角
				recvMsg.roll = d4;
				// double d5 = stringToNum<double>( arr1[6] ); // gyroX
				// recvMsg.gyroX = d5;
				// double d6 = stringToNum<double>( arr1[7] ); // gyroY
				// recvMsg.gyroY = d6;
				// double d7 = stringToNum<double>( arr1[8] ); // gyroZ
				// recvMsg.gyroZ = d7;
				// double d8 = stringToNum<double>( arr1[9] ); // accX
				// recvMsg.accX = d8;
				// double d9 = stringToNum<double>( arr1[10] ); // accY
				// recvMsg.accY = d9;
				// double d10 = stringToNum<double>( arr1[11] ); // accZ
				// recvMsg.accZ = d10;
				double d11 = stringToNum<double>( arr1[12] ); // latitude经度
				recvMsg.latitude = d11;
				double d12 = stringToNum<double>( arr1[13] ); // longitude纬度
				recvMsg.longtitude = d12;
				double d13 = stringToNum<double>( arr1[14] ); // attitude海拔
				recvMsg.altitude = d13;
				double d14 = stringToNum<double>( arr1[15] ); // Ve向东速度
				recvMsg.Ve = d14;
				double d15 = stringToNum<double>( arr1[16] ); // Vn向北速度
				recvMsg.Vn = d15;
				double d16 = stringToNum<double>( arr1[17] ); // Vu天向速度
				recvMsg.Vu = d16;
				double d17 = stringToNum<double>( arr1[18] ); // V车辆速度
				recvMsg.speed2d = d17;
				int d18 = stringToNum<int>( arr1[19] ); // 纬度标准差
				recvMsg.pose_type = 0;
				int d19 = stringToNum<int>( arr1[20] ); // 解算状态
				recvMsg.Lat_vart = 0;
				char d20 = stringToNum<char>( arr1[21] ); // 定位状态
				recvMsg.pose_type = d20;
				double d21 = stringToNum<double>( arr1[22] ); // 经度标准差
				recvMsg.Lon_vart = 0;
				arr1.clear();
				recvMsg.header.stamp = ros::Time::now();
				pub.publish( recvMsg );
			}
		}
	}

	return 0;
}