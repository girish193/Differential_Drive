#!/usr/bin/env python

import numpy as np
import rospy
from geometry_msgs.msg import Twist


def go_to_goal():

    # Initialize your ROS node
    rospy.init_node("move_robot")
    # Set up a publisher to the /cmd_vel topic
    pub = rospy.Publisher("cmd_vel", Twist, queue_size=10)
    # Declare a message of type Twist
    velocity_msg = Twist()
    # publish the velocity at 10 Hz (10 times per second)
    frequency = 10  # 10 Hz
    rate = rospy.Rate(frequency)

    velocity_msg.linear.z = 0
    velocity_msg.linear.y = 0
    velocity_msg.angular.x = 0
    velocity_msg.angular.y = 0

    data = np.loadtxt('./differential_drive/code/action_controls_test_case_(1 0.5 0).txt')

    x_pts = data[:, 0]
    y_pts = data[:, 1]
    vel_x = data[:, 2]
    w_z = data[:, 3]

    t = 1  # time for each action used in a-star code

    n_iterations = len(vel_x) - 1
    cycles = int(frequency*t)

    iter_ = 0
    while not rospy.is_shutdown() and iter_ < n_iterations:
        rospy.loginfo('Control action {}'.format(iter_+1))
        velocity_msg.linear.x = vel_x[iter_]
        velocity_msg.angular.z = w_z[iter_]
        rospy.loginfo(velocity_msg)

        for i in range(cycles):
            pub.publish(velocity_msg)
            rate.sleep()
        iter_ += 1

    velocity_msg.linear.x = 0
    velocity_msg.angular.z = 0
    pub.publish(velocity_msg)
    rate.sleep()

    rospy.loginfo('Goal Reached')


if __name__ == "__main__":
    try:
        go_to_goal()
    except rospy.ROSInterruptException:
        pass
