#!/usr/bin/env python

'''
says a line if the line exists for the robot.
Then publishes increment to indicate its done.
'''


import rospy
import os
import time
from std_msgs.msg import Int32
from playsound import playsound

def lineCallback(data):
	line = data.data
	audio_file = "/home/turtle1/catkin_ws/src/project2_play/scripts/einstein/"+ str(line) +".wav")):
	if(os.path.isfile(audio_file)):
		playsound(audio_file)
		time.sleep(2.5)
		increment.publish(line)
	return

rospy.init_node("Einstein")
increment = rospy.Publisher('/increment', Int32, queue_size=1)
rospy.Subscriber("/lines",Int32,lineCallback)
rospy.spin()

