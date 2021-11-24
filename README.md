# ROS_labs
## LAB 3
### PART 1

**PREREQUISITES**: Download and compile the 5 DOF planar robot packages.
```
sudo apt-get install ros-noetic-ros-control ros-noetic-ros-controllers //
git clone https://github.com/arebgun/dynamixel_motor //
git clone https://github.com/fenixkz/ros_snake_robot.git
sudo apt-get install ros-noetic-gazebo-ros-pkgs ros-noetic-gazebo-ros-control 
```
After every download: 
```
catkin_make
source ~/CATKIN_WORKSPACE/devel/setup.bash 
```
**TASK**: Create a rosnode that will “listen” for std_msgs/Float64 type data and “publish” this 
data to the joint of the planar robot. The node should send the command to move if 
the any new incoming value is lower than the previous one. 

Joint Movement of Planar Robot 


### PART 2
**TASK**: Get the step response (see example fig.1) of (you can create a node that will send a 
square-wave function):  
1. the joint at the base of the robot 

https://user-images.githubusercontent.com/40009146/143324486-7c62110d-9d00-46c1-af9a-ae03b7df1f0d.mov

2. the joint at the end-effector of the robot 

https://user-images.githubusercontent.com/40009146/143324505-068d092e-0c0a-408f-8688-12ace2fe1a19.mov

Get the sine-wave response of (you can create a node that will send a sine-wave 
function):  
3. the joint at the base of the robot 

https://user-images.githubusercontent.com/40009146/143324526-d920c683-2617-4fff-882c-7120bd425913.mov

4. the joint at the end-effector of the robot 

https://user-images.githubusercontent.com/40009146/143324537-609ec2f8-4dcf-46e0-8b2e-e8a058d0f56d.mov




