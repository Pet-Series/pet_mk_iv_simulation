#!/usr/bin/env python
# Pet-Mk-IV
#  \licens       Software License Agreement (MIT)
#  \authors      stefan.kull@gmail.com (Github ID 'SeniorKullken')
#  \repository   https://github.com/Pet-Series
#  \repository   https://github.com/Pet-Series/pet_mk_iv_simulation
#  \description  Adapter that convert Pet-series /cmd_vel TwistStamped => Gazebo /cmd_vel (twist)
#
#  Reason is that...
#  Publisher: Pet-series using /cmd_vel with msgType = TwistStamped
#  Subscribe: Gazebo using gazebo/cmd_vel with msgType = Twist (via plgin "libgazebo_ros_diff_drive.so")
#
# ----- Usage: Corresponding cmd line and launch file ------------------------------
# Alt 1) ...but not working suffecently 
#    $ rosrun topic_tools transform /cmd_vel /gazebo/cmd_vel geometry_msgs/Twist 'm.twist'
#
# Alt 2) ...but not working suffecently
# <launch>
#   <node name="TwistStamped_2_Twist" type="transform" pkg="topic_tools" args="/cmd_vel /gazebo/cmd_vel geometry_msgs/Twist 'm.twist'" />
# </launch>
#
# ----- Test ------------------------------
# $ rosrun pet_mk_iv_simulation gazebo_cmd_vel_adapter.py
# $ rostopic pub /cmd_vel geometry_msgs/TwistStamped "header:
#   seq: 0
#   stamp:
#     secs: 0
#     nsecs: 0
#   frame_id: ''
#  twist:
#   linear:
#     x: 1.0
#     y: 0.0
#     z: 0.0
#   angular:
#     x: 0.0
#     y: 0.0
#     z: 0.0"
# $ rostopic echo /gazebo/cmd_vel 
#  linear: 
#    x: 1.0
#    y: 0.0
#    z: 0.0
#  angular: 
#    x: 0.0
#    y: 0.0
#    z: 0.0
#  ---
#
# -----Prerequisite------------------------------
# <launch>
#   <node name="gazebo_cmd_vel_adapter_node" pkg="pet_mk_iv_simulation" type="gazebo_cmd_vel_adapter.py" />
# </launch>

import rospy
from geometry_msgs.msg  import TwistStamped # As input from the Pet-series the velocity controller
from geometry_msgs.msg  import Twist        # As output to Gazebo velocity controller-plugin


def callback(twist_stamped_msg):

    publisher.publish(twist_stamped_msg.twist)


if __name__ == "__main__":
    rospy.init_node("gazebo_cmd_vel_adapter_node")

    publisher  = rospy.Publisher("gazebo/cmd_vel", Twist, queue_size=10)
    subscriber = rospy.Subscriber("cmd_vel", TwistStamped, callback)

    rospy.spin()