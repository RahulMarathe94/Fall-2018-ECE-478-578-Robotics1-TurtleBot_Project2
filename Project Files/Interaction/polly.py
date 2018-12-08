#!/usr/bin/env python
import boto3
import rospy

#import actionlib
from std_msgs.msg import String, Bool,Int32
import time
from pygame import mixer
Text_Input="" 
p=""

print("Session Created")
polly_client = boto3.Session(
        aws_access_key_id="AKIAJOMEDGVCFB46I4SQ",                     
	    aws_secret_access_key="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",
	    region_name='us-west-2').client('polly')
print("Waiting for Callback")	

start_recording=rospy.Publisher('Start_Recording',Int32,queue_size=1)

def Speak_callback(data):
	global Text
	
	global polly_client
	Text_Input=data.data
	response = polly_client.synthesize_speech(VoiceId='Brian',
		        OutputFormat='mp3', 
		        #Text = 'Robotics Sample Text.')
			Text = Text_Input)

	file = open('speech.mp3', 'w')
	file.write(response['AudioStream'].read())
	file.close()
	
	#time.sleep(2)
	mixer.init()
	mixer.music.load('/home/turtle1/catkin_ws/speech.mp3')
	mixer.music.play()
	print("File Played")
	
	time.sleep(4)
	start_recording.publish(4)
	print("Done Speaking")
def polly_speech_node():
	global Text
	print("Called")
	#rate = rospy.Rate(10) # 10Hz
	print("Polly Node Initialised")
	# Initializing the ROS node "polly_speech"	
	rospy.init_node('polly_speech', anonymous=True)
	print("Session Ended")
	# Creating Subscriber topics for Listen
	rospy.Subscriber("Listen",String,Speak_callback)
	
	rospy.spin()
if __name__ == '__main__':
	try:
		polly_speech_node()
	except rospy.ROSInterruptexception:
		pass


