#!/usr/bin/env python3

import rospy
from std_msgs.msg import Bool
from pynput import keyboard

def on_press(key):
    try:
        if key.char == 'r':
            pub.publish(True)
            rospy.loginfo("Published True on 'trigger_topic'")
        elif key.char == 'q':
            rospy.loginfo("Stopped trigger service.")
            return False  # Stop listener
    except AttributeError:
        pass

if __name__ == "__main__":
    rospy.init_node('keyboard_trigger_client')
    pub = rospy.Publisher('trigger_topic', Bool, queue_size=10)
    rospy.loginfo("Press 'r' to publish trigger. Press 'q' to stop trigger service.")

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

