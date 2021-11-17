# ROS LABS
## LAB 3 
### PART 1

**PREREQUISITES**: Download and compile the 5 DOF planar robot packages.

sudo apt-get install ros-noetic-ros-control ros-noetic-ros-controllers //
git clone https://github.com/arebgun/dynamixel_motor //
git clone https://github.com/fenixkz/ros_snake_robot.git
sudo apt-get install ros-noetic-gazebo-ros-pkgs ros-noetic-gazebo-ros-control 

After every download: 
catkin_make
source ~/CATKIN_WORKSPACE/devel/setup.bash 

**TASK**: Create a rosnode that will “listen” for std_msgs/Float64 type data and “publish” this 
data to the joint of the planar robot. The node should send the command to move if 
the any new incoming value is lower than the previous one. 

Below can be seen images when position of joint 4 and 3 were changed. 
![alt text](https://github.com/zhamilyaa/ROS_labs/blob/main/joint4_changed.png)
![alt text](https://github.com/zhamilyaa/ROS_labs/blob/main/joint3_changed.png)
