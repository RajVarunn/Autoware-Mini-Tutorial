#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

class Publisher:
    def __init__(self):
        self.rate = rospy.get_param('~rate', 2) # 2hz per second, 0.5s per cycle
        self.rate = rospy.Rate(self.rate)
        self.message = rospy.get_param('~message', 'Hello World!') # Get the message parameter from the launch file

        # Publishers
        self.pub = rospy.Publisher('/message', String, queue_size=10) # Create a publisher that will publish messages of type String to the topic '/message' with a queue size of 10

    def run(self):
        while not rospy.is_shutdown():
            self.pub.publish(self.message) # Publish the message to the topic 
            self.rate.sleep() # Pauses the loop for the time remaining to hit the rate (2hz)

if __name__ == '__main__':
    rospy.init_node('publisher') # Initialize the node with the name 'publisher'
    node = Publisher()
    node.run()