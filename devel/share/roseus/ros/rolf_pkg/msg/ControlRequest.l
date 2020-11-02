;; Auto-generated. Do not edit!


(when (boundp 'rolf_pkg::ControlRequest)
  (if (not (find-package "ROLF_PKG"))
    (make-package "ROLF_PKG"))
  (shadow 'ControlRequest (find-package "ROLF_PKG")))
(unless (find-package "ROLF_PKG::CONTROLREQUEST")
  (make-package "ROLF_PKG::CONTROLREQUEST"))

(in-package "ROS")
;;//! \htmlinclude ControlRequest.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass rolf_pkg::ControlRequest
  :super ros::object
  :slots (_header _speed _turn ))

(defmethod rolf_pkg::ControlRequest
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:speed __speed) 0.0)
    ((:turn __turn) 0.0)
    )
   (send-super :init)
   (setq _header __header)
   (setq _speed (float __speed))
   (setq _turn (float __turn))
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:speed
   (&optional __speed)
   (if __speed (setq _speed __speed)) _speed)
  (:turn
   (&optional __turn)
   (if __turn (setq _turn __turn)) _turn)
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; float32 _speed
    4
    ;; float32 _turn
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; float32 _speed
       (sys::poke _speed (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _turn
       (sys::poke _turn (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; float32 _speed
     (setq _speed (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _turn
     (setq _turn (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get rolf_pkg::ControlRequest :md5sum-) "2efba620e13f7dc8f506729dd1f67c40")
(setf (get rolf_pkg::ControlRequest :datatype-) "rolf_pkg/ControlRequest")
(setf (get rolf_pkg::ControlRequest :definition-)
      "Header header
float32 speed
float32 turn

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



(provide :rolf_pkg/ControlRequest "2efba620e13f7dc8f506729dd1f67c40")

