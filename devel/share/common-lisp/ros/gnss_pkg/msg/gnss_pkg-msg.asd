
(cl:in-package :asdf)

(defsystem "gnss_pkg-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :geometry_msgs-msg
               :std_msgs-msg
)
  :components ((:file "_package")
    (:file "CurPose" :depends-on ("_package_CurPose"))
    (:file "_package_CurPose" :depends-on ("_package"))
    (:file "LaneLine" :depends-on ("_package_LaneLine"))
    (:file "_package_LaneLine" :depends-on ("_package"))
    (:file "LaneLineArray" :depends-on ("_package_LaneLineArray"))
    (:file "_package_LaneLineArray" :depends-on ("_package"))
    (:file "coordinate" :depends-on ("_package_coordinate"))
    (:file "_package_coordinate" :depends-on ("_package"))
    (:file "location" :depends-on ("_package_location"))
    (:file "_package_location" :depends-on ("_package"))
  ))