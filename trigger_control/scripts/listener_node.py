#!/usr/bin/env python3

import rospy
from std_msgs.msg import Bool

def trigger_callback(msg):
    if msg.data:
        rospy.loginfo("Trigger received! Running the action...")
        # TODO: Put your custom action code here
        # Example: call a function, move robot, start process, etc.
        perform_action()

def perform_action():
    # Replace this with whatever action you want to perform
    rospy.loginfo("Performing the triggered action!")

if __name__ == "__main__":
    rospy.init_node('trigger_listener')
    rospy.Subscriber('trigger_topic', Bool, trigger_callback)
    rospy.loginfo("Waiting for trigger on 'trigger_topic'...")
    rospy.spin()

