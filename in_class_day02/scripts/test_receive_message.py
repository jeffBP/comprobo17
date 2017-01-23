#!/usr/bin/env python
""" This script is my first ROS node. We'll publish some messages """
from geometry_msgs.msg import PointStamped, Point
from std_msgs.msg import Header
import rospy

rospy.init_node('test_receive_message')

def process_point(m):
    print m


r = rospy.Rate(2)
rospy.Subscriber('/my_topic', PointStamped, process_point)

while not rospy.is_shutdown():
        r.sleep()

print('Node is finish')
