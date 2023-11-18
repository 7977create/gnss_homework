std_msgs/Header header

float32     pitch         #俯仰角
float32     roll            #翻滚角
float32     heading     #航向角

float64     longtitude  #经度
float64     latitude      #纬度
float64     altitude      #海拔

float32     speed2d     #车辆速度
#-------------------------------->
float64     Ve               #向东速度
float64     Vn               #向北速度
float64     Vu               #天向速度
#<-------------------------------
float64    GPStime      #时间
int32       pose_type   #定位状态
int32       INS_Status  #解算状态
float32    Lat_vart      #纬度标准差
float32    Lon_vart     #经度标准差