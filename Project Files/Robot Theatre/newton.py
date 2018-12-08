#!/usr/bin/env python

'''
says a line if the line exists for the robot.
Then publishes increment to indicate its done.
'''


import rospy
import pygame
import os
import time
from std_msgs.msg import Int32



def lineCallback(data):
	line = data.data
	audio_file = "/home/turtle1/catkin_ws/src/project2_play/scripts/lines/act1/"+ str(line) +".wav"

	if(os.path.isfile(audio_file)):
		pygame.mixer.init(44100, -16, 2, 2048)
		pygame.mixer.init()
		audio_play = pygame.mixer.Sound(audio_file)
		free_channel = pygame.mixer.find_channel()
		playing = audio_play.play()
		while playing.get_busy():
			pygame.time.wait(50)
		time.sleep(2.5)
		increment.publish(line)
	return

rospy.init_node("Newton")
increment = rospy.Publisher('/increment', Int32, queue_size=1)
rospy.Subscriber("/lines",Int32,lineCallback)
rospy.spin()

