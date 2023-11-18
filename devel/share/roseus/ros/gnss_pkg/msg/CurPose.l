;; Auto-generated. Do not edit!


(when (boundp 'gnss_pkg::CurPose)
  (if (not (find-package "GNSS_PKG"))
    (make-package "GNSS_PKG"))
  (shadow 'CurPose (find-package "GNSS_PKG")))
(unless (find-package "GNSS_PKG::CURPOSE")
  (make-package "GNSS_PKG::CURPOSE"))

(in-package "ROS")
;;//! \htmlinclude CurPose.msg.html


(defclass gnss_pkg::CurPose
  :super ros::object
  :slots (_x _y _theta _s _d ))

(defmethod gnss_pkg::CurPose
  (:init
   (&key
    ((:x __x) 0.0)
    ((:y __y) 0.0)
    ((:theta __theta) 0.0)
    ((:s __s) 0.0)
    ((:d __d) 0.0)
    )
   (send-super :init)
   (setq _x (float __x))
   (setq _y (float __y))
   (setq _theta (float __theta))
   (setq _s (float __s))
   (setq _d (float __d))
   self)
  (:x
   (&optional __x)
   (if __x (setq _x __x)) _x)
  (:y
   (&optional __y)
   (if __y (setq _y __y)) _y)
  (:theta
   (&optional __theta)
   (if __theta (setq _theta __theta)) _theta)
  (:s
   (&optional __s)
   (if __s (setq _s __s)) _s)
  (:d
   (&optional __d)
   (if __d (setq _d __d)) _d)
  (:serialization-length
   ()
   (+
    ;; float64 _x
    8
    ;; float64 _y
    8
    ;; float64 _theta
    8
    ;; float64 _s
    8
    ;; float64 _d
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64 _x
       (sys::poke _x (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _y
       (sys::poke _y (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _theta
       (sys::poke _theta (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _s
       (sys::poke _s (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _d
       (sys::poke _d (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64 _x
     (setq _x (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _y
     (setq _y (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _theta
     (setq _theta (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _s
     (setq _s (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _d
     (setq _d (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(setf (get gnss_pkg::CurPose :md5sum-) "e749843f9524582d302890cf564a4840")
(setf (get gnss_pkg::CurPose :datatype-) "gnss_pkg/CurPose")
(setf (get gnss_pkg::CurPose :definition-)
      "#---------------------------------------------------------------
# 作者 ：刘孟鑫
# 时间 ：2019.08.12
# 版权 ：重庆邮电大学自动化学院汽车电子工程中心智能车辆技术团队
# 说明 ：
#----------------------------------------------------------------

float64                 x               #x位置
float64                 y               #y位置
float64                 theta           #航向
float64                 s               #s位置
float64                 d               #d位置

")



(provide :gnss_pkg/CurPose "e749843f9524582d302890cf564a4840")


