#!/usr/bin/env python3
import time

import numpy as np
import rospy
from geometry_msgs.msg import PointStamped, Twist
from sensor_msgs.msg import Joy, LaserScan
from std_msgs.msg import Bool, Int8
from topic_tools.srv import MuxSelect, MuxSelectRequest

class ManualNode:
    def __init__(self) -> None:
        rospy.init_node("manual_node")
        self.my_var = rospy.Subscriber("/CCS_Data", Int8, self.callback) 
        self.mux_selector = rospy.ServiceProxy("/mux_cmdvel_ui/select", MuxSelect)
        rospy.loginfo("Mux Selector Node Started")
        rospy.spin()
    def callback(self, data):
        if data.data == 1:
            self.mux_selector(MuxSelectRequest("/none/cmd_vel"))
            rospy.loginfo("Mux Changed to none/cmd_vel")
        elif data.data == 0:
            self.mux_selector(MuxSelectRequest("/zeros/cmd_vel"))
            rospy.loginfo("Mux Changed to zeros/cmd_vel")

def main():
    follow_node = ManualNode()


if __name__ == "__main__":
    main()
