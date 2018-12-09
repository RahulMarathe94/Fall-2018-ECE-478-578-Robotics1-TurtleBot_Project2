# Fall-2018-ECE-478-578-Robotics1-TurtleBot_Project2

## Project Requirements:

### For project 2 we implemented all these functions in ROS :- 
#### Different kinds of motions such as Gestures like Bye, Hi,Taunt ,Dancing, Speech Synthesis and Robot Theatre  

Bot can be controlled by publishing to ROS topics

### Node1: 
#### Servos
Responsible for motion: subscribes to a topic /Lines: and moves the robot arm servos

### Node2: 
#### Record: 
Responsible for speech recognition, Recording Audio Input , subscribes to topic /Start_Recording

### Node3: 
#### Dialogflow :
Responsible for speech synthesis, subscribes to topic /filename which is the audio input file for detecting intents

### Node 4: 
#### Polly 
Text to Speech conversion subscribes to topic /text which is the string for conversion to Speech

### Hardware: 
#### Kobuki Turtle Bot Base: 
The base is a Turtlebot 2i built upon a Kobuki base which has two motorized wheels for mobility. 
It also has several built-in sensors including a bumper along the front half of the robot which alerts the robot of collisions, drop sensors in both wheels to signal changes in terrain, cliff sensors to signal when the robot is about to drop off a ledge, and a gyro sensor for navigation. These sensors serve as inputs to the Bot and can be intergated together.


### Dynamixel Servos: 
#### HR OS1 
The HR-OS1 is a small humanoid robot which utilizes several Dynamic Cell servos as its joints. The upper portion of the HR-OS1 was attached to the Turtlebot due to the Turtlebot having a higher stability than the HR-OS1’s servo legs. The integration of this torso also allows for gestural interactions with the turtlebot system.


## Project Team : 
### Team Member 1 Kanna Lakshmanan 
### Team Member 2 Jennifer Lara 
### Team Member 3 Lauren Voepel 
### Team Member 4 Rahul Marathe
