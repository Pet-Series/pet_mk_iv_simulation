#!/usr/bin/env python
# Pet-Mk-IV
#  \licens       Software License Agreement (MIT)
#  \authors      karl.viktor.kull@gmail.com  (Github ID 'Kullken')
#  \authors      stefan.kull@gmail.com (Github ID 'SeniorKullken')
#  \repository   https://github.com/Pet-Series
#  \repository   https://github.com/Pet-Series/pet_mk_iv_simulation
#  \description  Adapter that convert Gazebo Camera/Image topics to LineDetection<"DARK"/"LIGHT">.
#
#  Reason is that Gazebo/Virtual vs. Real/Physical robot has different type of topics.
#  Convert from Gazebo-camera interface => Bolean True/False
#
# TODO: Parametric linesAre=LineDetection.DARK or linesAre=LineDetection.LIGHT
#
# -----Prerequisite/Usage------------------------------
# <launch>
#  <node name="line_sensor_left_converter" pkg="pet_mk_iv_simulation" type="gazebo_line_sensor_adapter.py"> 
#    <remap from="camera"      to="/line_sensor/left/image_raw" />
#    <remap from="line_sensor" to="/line_sensor/left" />
#  </node>
#  <node name="line_sensor_mid_converter" pkg="pet_mk_iv_simulation" type="gazebo_line_sensor_adapter.py"> 
#    <remap from="camera"      to="/line_sensor/middle/image_raw" />
#    <remap from="line_sensor" to="/line_sensor/middle" />
#  </node>
#  <node name="line_sensor_right_converter" pkg="pet_mk_iv_simulation" type="gazebo_line_sensor_adapter.py"> 
#    <remap from="camera"      to="/line_sensor/right/image_raw" />
#    <remap from="line_sensor" to="/line_sensor/right" />
#  </node>
# </launch>
import rospy
from sensor_msgs.msg import Image

from pet_mk_iv_msgs.msg import LineDetection

GRAYSCALE_THRESHOLD = 50

def callback(image):
    sum = 0
    for pixel in image.data:
        sum += pixel
    mean = sum / len(image.data)

    line_msg = LineDetection()
    line_msg.header = image.header
    if mean > GRAYSCALE_THRESHOLD:
        line_msg.value = LineDetection.LIGHT
    else:
        line_msg.value = LineDetection.DARK

    publisher.publish(line_msg)


if __name__ == "__main__":
    rospy.init_node("line_sensor_gazebo_converter")

    publisher = rospy.Publisher("line_sensor", LineDetection, queue_size=10)
    subscriber = rospy.Subscriber("camera", Image, callback)

    rospy.spin()

