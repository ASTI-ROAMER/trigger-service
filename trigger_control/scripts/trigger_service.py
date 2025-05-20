#!/usr/bin/env python3

import rospy
from std_srvs.srv import Trigger, TriggerResponse
from std_msgs.msg import Bool

def handle_trigger(req):
    rospy.loginfo("Service was triggered!")
    pub.publish(True)  # Publish bool True instead of string
    return TriggerResponse(success=True, message="Trigger received.")

if __name__ == "__main__":
    rospy.init_node("trigger_service_node")
    pub = rospy.Publisher("/trigger_topic", Bool, queue_size=10)

    srv = rospy.Service("trigger_service", Trigger, handle_trigger)
    rospy.loginfo("Trigger service ready.")
    rospy.spin()

