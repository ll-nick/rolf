; Auto-generated. Do not edit!


(cl:in-package rolf_pkg-msg)


;//! \htmlinclude ControlRequest.msg.html

(cl:defclass <ControlRequest> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (speed
    :reader speed
    :initarg :speed
    :type cl:float
    :initform 0.0)
   (turn
    :reader turn
    :initarg :turn
    :type cl:float
    :initform 0.0))
)

(cl:defclass ControlRequest (<ControlRequest>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ControlRequest>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ControlRequest)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name rolf_pkg-msg:<ControlRequest> is deprecated: use rolf_pkg-msg:ControlRequest instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <ControlRequest>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader rolf_pkg-msg:header-val is deprecated.  Use rolf_pkg-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'speed-val :lambda-list '(m))
(cl:defmethod speed-val ((m <ControlRequest>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader rolf_pkg-msg:speed-val is deprecated.  Use rolf_pkg-msg:speed instead.")
  (speed m))

(cl:ensure-generic-function 'turn-val :lambda-list '(m))
(cl:defmethod turn-val ((m <ControlRequest>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader rolf_pkg-msg:turn-val is deprecated.  Use rolf_pkg-msg:turn instead.")
  (turn m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ControlRequest>) ostream)
  "Serializes a message object of type '<ControlRequest>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'speed))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'turn))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ControlRequest>) istream)
  "Deserializes a message object of type '<ControlRequest>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'speed) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'turn) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ControlRequest>)))
  "Returns string type for a message object of type '<ControlRequest>"
  "rolf_pkg/ControlRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ControlRequest)))
  "Returns string type for a message object of type 'ControlRequest"
  "rolf_pkg/ControlRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ControlRequest>)))
  "Returns md5sum for a message object of type '<ControlRequest>"
  "2efba620e13f7dc8f506729dd1f67c40")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ControlRequest)))
  "Returns md5sum for a message object of type 'ControlRequest"
  "2efba620e13f7dc8f506729dd1f67c40")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ControlRequest>)))
  "Returns full string definition for message of type '<ControlRequest>"
  (cl:format cl:nil "Header header~%float32 speed~%float32 turn~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ControlRequest)))
  "Returns full string definition for message of type 'ControlRequest"
  (cl:format cl:nil "Header header~%float32 speed~%float32 turn~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ControlRequest>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ControlRequest>))
  "Converts a ROS message object to a list"
  (cl:list 'ControlRequest
    (cl:cons ':header (header msg))
    (cl:cons ':speed (speed msg))
    (cl:cons ':turn (turn msg))
))
