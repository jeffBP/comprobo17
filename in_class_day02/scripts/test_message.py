#!/usr/bin/env python
""" This script is my first ROS node. We'll publish some messages """
from geometry_msgs.msg import PointStamped, Point
from std_msgs.msg import Header
import rospy

rospy.init_node('test_message')

r = rospy.Rate(2)
loopcount = 0
publisher = rospy.Publisher('/my_topic', PointStamped, queue_size=10)
while not rospy.is_shutdown():
    loopcount = loopcount + 1
    print "looping", loopcount
    my_header = Header(loopcount, rospy.Time.now(), "odom")
    my_point = Point(x=3.2, y=5.4, z=0.0)
    my_point_stamped = PointStamped(point=my_point, header=my_header)
    publisher.publish(my_point_stamped)

    r.sleep()

print('Node is finish')
