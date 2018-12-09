# Fall-2018-ECE-478-578-Robotics1-TurtleBot_Project2

## Project Requirements:

For project 2 we implemented all these functions in ROS :- 
Different kinds of motions such as moving forward, backward, left, right, turning around, dancing, Speech Synthesis and Robot Theatre  

Bot can be controlled by publishing to ROS topics

### Node1: 
####Servos
responsible for motion: subscribes to a topic /Lines: and moves the robot arm servos

### Node2: 
#### Record: 
responsible for speech recognition, Recording Audio Input , subscribes to topic /Start_Recording

### Node3: 
#### Dialogflow :
responsible for speech synthesis, subscribes to topic /filename which is the audio input file for detecting intents

###Node 4: 
#### Polly 
Text to Speech conversion subscribes to topic /text which is the string for conversion to Speech

