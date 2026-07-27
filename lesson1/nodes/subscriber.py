#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

class Subscriber:
    def __init__(self):
        # Subscribers
        rospy.Subscriber('/message', String, self.message_callback) # Subscriber that will listen for messages of type String on the topic 

    def message_callback(self, msg):
        print(msg.data)

    def run(self):
        rospy.spin() # Keeps the node from exiting until the node has been shutdown (stay alive)


if __name__ == '__main__':
    rospy.init_node('subscriber') # Initialize the node with the name 'subscriber' 
    node = Subscriber()
    node.run()