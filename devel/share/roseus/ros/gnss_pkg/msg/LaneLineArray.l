;; Auto-generated. Do not edit!


(when (boundp 'gnss_pkg::LaneLineArray)
  (if (not (find-package "GNSS_PKG"))
    (make-package "GNSS_PKG"))
  (shadow 'LaneLineArray (find-package "GNSS_PKG")))
(unless (find-package "GNSS_PKG::LANELINEARRAY")
  (make-package "GNSS_PKG::LANELINEARRAY"))

(in-package "ROS")
;;//! \htmlinclude LaneLineArray.msg.html


(defclass gnss_pkg::LaneLineArray
  :super ros::object
  :slots (_lines ))

(defmethod gnss_pkg::LaneLineArray
  (:init
   (&key
    ((:lines __lines) (let (r) (dotimes (i 0) (push (instance gnss_pkg::LaneLine :init) r)) r))
    )
   (send-super :init)
   (setq _lines __lines)
   self)
  (:lines
   (&rest __lines)
   (if (keywordp (car __lines))
       (send* _lines __lines)
     (progn
       (if __lines (setq _lines (car __lines)))
       _lines)))
  (:serialization-length
   ()
   (+
    ;; gnss_pkg/LaneLine[] _lines
    (apply #'+ (send-all _lines :serialization-length)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; gnss_pkg/LaneLine[] _lines
     (write-long (length _lines) s)
     (dolist (elem _lines)
       (send elem :serialize s)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; gnss_pkg/LaneLine[] _lines
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _lines (let (r) (dotimes (i n) (push (instance gnss_pkg::LaneLine :init) r)) r))
     (dolist (elem- _lines)
     (send elem- :deserialize buf ptr-) (incf ptr- (send elem- :serialization-length))
     ))
   ;;
   self)
  )

(setf (get gnss_pkg::LaneLineArray :md5sum-) "b311b16e049dce662db6f00b38186809")
(setf (get gnss_pkg::LaneLineArray :datatype-) "gnss_pkg/LaneLineArray")
(setf (get gnss_pkg::LaneLineArray :definition-)
      "
#------------------------------
#车道线序列
#------当前项目中车道线点序列长度为30
#------------------------------

LaneLine[]         lines

================================================================================
MSG: gnss_pkg/LaneLine

#------------------------------
#车道线
#------当前项目中车道线点序列长度为30
#------geometry_msgs/Point类型是（x,y,z),目前只填充x,y忽略z
#------s可以用来计算点位于地图的frenet的s坐标值
#------------------------------
uint32                         id
uint8                          type
float64[]                      x
float64[]                      y
float64[]                      s

geometry_msgs/Point[]          points
uint8                          current_lane_num
================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

")



(provide :gnss_pkg/LaneLineArray "b311b16e049dce662db6f00b38186809")


