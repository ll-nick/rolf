
(cl:in-package :asdf)

(defsystem "rolf_pkg-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :std_msgs-msg
)
  :components ((:file "_package")
    (:file "ControlRequest" :depends-on ("_package_ControlRequest"))
    (:file "_package_ControlRequest" :depends-on ("_package"))
  ))