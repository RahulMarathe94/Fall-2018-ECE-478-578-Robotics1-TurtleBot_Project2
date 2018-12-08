#!/usr/bin/env python
import dialogflow_v2 as dialogflow
import os
import rospy
from std_msgs.msg import String, Bool, Int32
import time
pubtext =rospy.Publisher('/Listen', String, queue_size=1)
pubgesture=rospy.Publisher('/lines', Int32,queue_size=1)

def detect_intent_audio(project_id, session_id, audio_file_path,
                        language_code):
	import dialogflow_v2 as dialogflow
	session_client = dialogflow.SessionsClient()
	print("detect intent")

	audio_encoding = dialogflow.enums.AudioEncoding.AUDIO_ENCODING_LINEAR_16
	sample_rate_hertz = 16000

	session = session_client.session_path(project_id, session_id)

	with open(audio_file_path, 'rb') as audio_file:
		input_audio = audio_file.read()

	audio_config = dialogflow.types.InputAudioConfig(
		audio_encoding=audio_encoding, language_code=language_code,
        sample_rate_hertz=sample_rate_hertz)
	query_input = dialogflow.types.QueryInput(audio_config=audio_config)

	response = session_client.detect_intent(
        session=session, query_input=query_input,
        input_audio=input_audio)
	print('Query text: {}'.format(response.query_result.query_text))
	print('Detected intent: {} (confidence: {})\n'.format(
        response.query_result.intent.display_name,
        response.query_result.intent_detection_confidence))
	print('Fulfillment text: {}\n'.format(
        response.query_result.fulfillment_text))	
	return response.query_result.fulfillment_text
	


def get_file_name(data):
	filename=data.data
	homedir = os.environ['HOME']
	filepath = homedir + "/catkin_ws/"
	#user_input = os.path.join(filepath, 'user_input3.wav')
	user_input = os.path.join(filepath, filename)
	print(user_input)
	time.sleep(2)
	result = detect_intent_audio("hello-19424", "1-1-1-1-1", user_input, 'en-US')
	print("done")
	print (result)
	if (result.find("Greetings")>=0)or(result.find("Hello")>=0)or(result.find("Hi")>=0):
		pubgesture.publish(6)
	elif result.find("Bye")>0:
		pubgesture.publish(6)
	elif result.find("No")>=0:
		pubgesture.publish(9)
	elif result.find("Gravity")>=0:
		pubgesture.publish(15)
	pubtext.publish(result)
	time.sleep(3)		
	
def dialog_speech_node():
	print("Called")
	print("Dialogflow Node Initialised")
	# Initializing the ROS node "polly_speech"	
	rospy.init_node('Dialog_speech', anonymous=True)
	rospy.Subscriber("filename",String,get_file_name)
	
	rospy.spin()
	"""
	homedir = os.environ['HOME']
	filepath = homedir + "/catkin_ws/src/"
	user_input = os.path.join(filepath, 'user_input3.wav')
	#user_input = os.path.join(filepath, filename)
	
	print(user_input)
	result = detect_intent_audio("hello-19424", "1-1-1-1-1", user_input, 'en-US')
	print("done")
	print (result)
	pubtext.publish(result)
	time.sleep(3)		
	rospy.spin()
	"""

if __name__ == '__main__':
	dialog_speech_node()	
	"""
	try:
		dialog_speech_node()
	except rospy.ROSInterruptexception:
		pass
	"""
