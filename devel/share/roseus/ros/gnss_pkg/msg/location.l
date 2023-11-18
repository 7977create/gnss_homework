;; Auto-generated. Do not edit!


(when (boundp 'gnss_pkg::location)
  (if (not (find-package "GNSS_PKG"))
    (make-package "GNSS_PKG"))
  (shadow 'location (find-package "GNSS_PKG")))
(unless (find-package "GNSS_PKG::LOCATION")
  (make-package "GNSS_PKG::LOCATION"))

(in-package "ROS")
;;//! \htmlinclude location.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass gnss_pkg::location
  :super ros::object
  :slots (_header _pitch _roll _heading _longtitude _latitude _altitude _speed2d _Ve _Vn _Vu _GPStime _pose_type _INS_Status _Lat_vart _Lon_vart ))

(defmethod gnss_pkg::location
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:pitch __pitch) 0.0)
    ((:roll __roll) 0.0)
    ((:heading __heading) 0.0)
    ((:longtitude __longtitude) 0.0)
    ((:latitude __latitude) 0.0)
    ((:altitude __altitude) 0.0)
    ((:speed2d __speed2d) 0.0)
    ((:Ve __Ve) 0.0)
    ((:Vn __Vn) 0.0)
    ((:Vu __Vu) 0.0)
    ((:GPStime __GPStime) 0.0)
    ((:pose_type __pose_type) 0)
    ((:INS_Status __INS_Status) 0)
    ((:Lat_vart __Lat_vart) 0.0)
    ((:Lon_vart __Lon_vart) 0.0)
    )
   (send-super :init)
   (setq _header __header)
   (setq _pitch (float __pitch))
   (setq _roll (float __roll))
   (setq _heading (float __heading))
   (setq _longtitude (float __longtitude))
   (setq _latitude (float __latitude))
   (setq _altitude (float __altitude))
   (setq _speed2d (float __speed2d))
   (setq _Ve (float __Ve))
   (setq _Vn (float __Vn))
   (setq _Vu (float __Vu))
   (setq _GPStime (float __GPStime))
   (setq _pose_type (round __pose_type))
   (setq _INS_Status (round __INS_Status))
   (setq _Lat_vart (float __Lat_vart))
   (setq _Lon_vart (float __Lon_vart))
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:pitch
   (&optional __pitch)
   (if __pitch (setq _pitch __pitch)) _pitch)
  (:roll
   (&optional __roll)
   (if __roll (setq _roll __roll)) _roll)
  (:heading
   (&optional __heading)
   (if __heading (setq _heading __heading)) _heading)
  (:longtitude
   (&optional __longtitude)
   (if __longtitude (setq _longtitude __longtitude)) _longtitude)
  (:latitude
   (&optional __latitude)
   (if __latitude (setq _latitude __latitude)) _latitude)
  (:altitude
   (&optional __altitude)
   (if __altitude (setq _altitude __altitude)) _altitude)
  (:speed2d
   (&optional __speed2d)
   (if __speed2d (setq _speed2d __speed2d)) _speed2d)
  (:Ve
   (&optional __Ve)
   (if __Ve (setq _Ve __Ve)) _Ve)
  (:Vn
   (&optional __Vn)
   (if __Vn (setq _Vn __Vn)) _Vn)
  (:Vu
   (&optional __Vu)
   (if __Vu (setq _Vu __Vu)) _Vu)
  (:GPStime
   (&optional __GPStime)
   (if __GPStime (setq _GPStime __GPStime)) _GPStime)
  (:pose_type
   (&optional __pose_type)
   (if __pose_type (setq _pose_type __pose_type)) _pose_type)
  (:INS_Status
   (&optional __INS_Status)
   (if __INS_Status (setq _INS_Status __INS_Status)) _INS_Status)
  (:Lat_vart
   (&optional __Lat_vart)
   (if __Lat_vart (setq _Lat_vart __Lat_vart)) _Lat_vart)
  (:Lon_vart
   (&optional __Lon_vart)
   (if __Lon_vart (setq _Lon_vart __Lon_vart)) _Lon_vart)
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; float32 _pitch
    4
    ;; float32 _roll
    4
    ;; float32 _heading
    4
    ;; float64 _longtitude
    8
    ;; float64 _latitude
    8
    ;; float64 _altitude
    8
    ;; float32 _speed2d
    4
    ;; float64 _Ve
    8
    ;; float64 _Vn
    8
    ;; float64 _Vu
    8
    ;; float64 _GPStime
    8
    ;; int32 _pose_type
    4
    ;; int32 _INS_Status
    4
    ;; float32 _Lat_vart
    4
    ;; float32 _Lon_vart
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; float32 _pitch
       (sys::poke _pitch (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _roll
       (sys::poke _roll (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _heading
       (sys::poke _heading (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float64 _longtitude
       (sys::poke _longtitude (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _latitude
       (sys::poke _latitude (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _altitude
       (sys::poke _altitude (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float32 _speed2d
       (sys::poke _speed2d (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float64 _Ve
       (sys::poke _Ve (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _Vn
       (sys::poke _Vn (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _Vu
       (sys::poke _Vu (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _GPStime
       (sys::poke _GPStime (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; int32 _pose_type
       (write-long _pose_type s)
     ;; int32 _INS_Status
       (write-long _INS_Status s)
     ;; float32 _Lat_vart
       (sys::poke _Lat_vart (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _Lon_vart
       (sys::poke _Lon_vart (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; float32 _pitch
     (setq _pitch (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _roll
     (setq _roll (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _heading
     (setq _heading (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float64 _longtitude
     (setq _longtitude (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _latitude
     (setq _latitude (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _altitude
     (setq _altitude (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float32 _speed2d
     (setq _speed2d (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float64 _Ve
     (setq _Ve (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _Vn
     (setq _Vn (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _Vu
     (setq _Vu (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _GPStime
     (setq _GPStime (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; int32 _pose_type
     (setq _pose_type (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; int32 _INS_Status
     (setq _INS_Status (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; float32 _Lat_vart
     (setq _Lat_vart (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _Lon_vart
     (setq _Lon_vart (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get gnss_pkg::location :md5sum-) "d10dd53c2060c0966a0cb0e0c08fa213")
(setf (get gnss_pkg::location :datatype-) "gnss_pkg/location")
(setf (get gnss_pkg::location :definition-)
      "std_msgs/Header header

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
================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
string frame_id

")



(provide :gnss_pkg/location "d10dd53c2060c0966a0cb0e0c08fa213")


