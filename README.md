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

![caption](https://github.com/zhamilyaa/ROS_labs/blob/master/test_joint/lab3_part1.mov)

<video src='https://github.com/zhamilyaa/ROS_labs/blob/master/test_joint/lab3_part1.mov' width=180/>


https://user-images.githubusercontent.com/40009146/142288231-38abe949-54f2-4522-b43c-7d5f7af4eeac.mov

lab3_part2_base_sin.mov


## lab3_part2_base_sin.mov
