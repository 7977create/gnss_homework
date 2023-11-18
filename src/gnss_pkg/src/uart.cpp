#include "uart.h"

int open_port()
{
    char *dev = "/dev/ttyUSB0";                                                  // 串口设备路径
    int fd = open( dev, O_RDWR | O_NOCTTY | O_NDELAY );       // 打开串口设备
    if( fd == -1 ){                                                                            // 如果打开失败
        std::cout<<"error1 ..."<<std::endl;                                     // 输出错误信息
        return false;                                                                         // 返回错误标志
    }
    if( fcntl( fd, F_SETFL, 0 ) < 0 ){                                                // 设置文件标识符状态
        std::cout<<"error2 ..."<<std::endl;     
        return false;
    }
    if( isatty( STDIN_FILENO ) == 0 ){                                             // 判断标准输入是否为终端设备
        std::cout<<"error3 ..."<<std::endl;
        return false;
    }
    std::cout<<"open port successfully ..."<<std::endl;               // 输出成功信息
    return fd;                                                                                   // 返回成功标志，即串口设备文件描述符
}

// 串口通信进行配置的函数，用于设置串口的属性。
int set_opt( int fd )
{
// 通过tcgetattr函数读取串口的原始属性，保存在oldtio结构体中。
    struct termios newtio, oldtio;
    if( tcgetattr( fd, &oldtio ) != 0 ){
        std::cout<<"read old serial attributions failed ..."<<std::endl;
        return false;
    }
    bzero( &newtio, sizeof( newtio ) );
// 设置本地连接和接收使能。
    newtio.c_cflag |= CLOCAL | CREAD;
// 设置数据位为8位。
    newtio.c_cflag &= ~CSIZE;
    newtio.c_cflag |= CS8;
// 禁用奇偶校验。
    newtio.c_cflag &= ~PARENB;
// 设置串口的输入输出波特率为115200。
    cfsetispeed( &newtio, B115200 );
    cfsetospeed( &newtio, B115200 );
    // 设置停止位为1位。
    newtio.c_cflag &= ~CSTOPB;
// 设置读取串口数据的最小字符数和超时等待时间。
    newtio.c_cc[VTIME] = 0;
    newtio.c_cc[VMIN] = 1;
// 使用tcflush函数清空输入缓冲区。
    tcflush( fd, TCIFLUSH );
// 使用tcsetattr函数将新的串口属性应用到串口，如果设置失败则返回false。
    if( ( tcsetattr( fd, TCSANOW, &newtio ) ) != 0 ){
        std::cout<<"com set error ... "<<std::endl;
        return false;
    }
    std::cout<<"set port successfully ..."<<std::endl;
    return true;
}

// 从给定的文件描述符（fd）中读取数据到接收缓冲区（recvBuff）中。
bool recvData( int fd, char *recvBuff, int n )
{
        int count = 1;
        // 调用read函数以每次读取一个字节的方式从文件描述符（fd）中读取数据
        //  并将其存储到接收缓冲区（recvBuff）的第一个位置（&recvBuff[0]）。
        read( fd, &recvBuff[0], 1 );
        // 判断是否接收到了以$开头的数据帧，如果是，则进入一个循环。
        if( recvBuff[0] == '$' ){
                do{
                    // 调用read函数以每次读取一个字节的方式从文件描述符（fd）中读取数据
                    // 并将其存储到接收缓冲区（recvBuff）的下一个位置（&recvBuff[count]）
                        read( fd, &recvBuff[ count ], 1 );
                        count ++ ;
                    // 读取到回车（0x0D）和换行（0x0A）字符为止，表示数据帧结束
		}while( recvBuff[count - 1] != 0x0D && recvBuff[count] != 0x0A );// "count < n " should not be exist in here, maybe, waiting for a test
            // 输出当前读取到的数据帧的长度（count的值）。
                std::cout<<"count is: "<<count<<std::endl;
                // count重置为1，为下一个数据帧的接收做准备
                count = 1;
        }
	else{
        // 如果没有读取到以$开头的数据帧，则返回false，表示接收失败
		return false;
	}
    // 如果成功读取到数据帧，返回true，表示接收成功
	return true;
}

// 发送一个字节的数据到给定的文件描述符（fd）。
bool send_Byte( int fd, char byte )
{
    // 使用write函数将一个字节的数据（byte）写入到文件描述符（fd）中。
    // write函数的返回值是否等于1，如果不等于1，则表示写入失败。
	if( write( fd, &byte, 1 ) != 1){
		return false;
	}
    // 写入成功，函数会返回true，并输出一个发送成功的提示信息到控制台。
	else{
		std::cout<<"send commander successfully ..."<<std::endl;
		return true;
	}
}