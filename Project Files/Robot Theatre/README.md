# Robot Theatre

This section involved synching up 3 robots to perform a section of a play written by Prof. Perkowski. 

## 

Each robot recieved a version of the script file, newton.py, with the rosnode name and file path to their lines changed 
depending on which robot the script was given to (Dim and Einstein). The nodes created in these scripts subscribe to a topic called /lines which is a 32 bit int which corresponds to which line of the play is being spoken. After speaking the nodes publish to a topic called /increment which is subscribed to by the node created in the script counter.py. Counter.py uses this as an indicator of when to increment /lines for the next line to be spoken. This system is relatively modular and can be adapted to be used on more than 3 robots with the only changes to code being node name and filepath to audio files. 

### Dependencies

The audio player used in the script depended on what was preinstalled on each robot. Our robot, Newton had a version of Ubuntu Mate for Raspberry Pi installed as well as several python libraries. For audio, Python's Pygame library was used.
