;; Auto-generated. Do not edit!


(when (boundp 'gnss_pkg::coordinate)
  (if (not (find-package "GNSS_PKG"))
    (make-package "GNSS_PKG"))
  (shadow 'coordinate (find-package "GNSS_PKG")))
(unless (find-package "GNSS_PKG::COORDINATE")
  (make-package "GNSS_PKG::COORDINATE"))

(in-package "ROS")
;;//! \htmlinclude coordinate.msg.html


(defclass gnss_pkg::coordinate
  :super ros::object
  :slots (_x _y ))

(defmethod gnss_pkg::coordinate
  (:init
   (&key
    ((:x __x) 0.0)
    ((:y __y) 0.0)
    )
   (send-super :init)
   (setq _x (float __x))
   (setq _y (float __y))
   self)
  (:x
   (&optional __x)
   (if __x (setq _x __x)) _x)
  (:y
   (&optional __y)
   (if __y (setq _y __y)) _y)
  (:serialization-length
   ()
   (+
    ;; float64 _x
    8
    ;; float64 _y
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
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64 _x
     (setq _x (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _y
     (setq _y (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(setf (get gnss_pkg::coordinate :md5sum-) "209f516d3eb691f0663e25cb750d67c1")
(setf (get gnss_pkg::coordinate :datatype-) "gnss_pkg/coordinate")
(setf (get gnss_pkg::coordinate :definition-)
      "
float64     x  #经度
float64     y      #纬度


")



(provide :gnss_pkg/coordinate "209f516d3eb691f0663e25cb750d67c1")


