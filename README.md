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
**TASK**: Get the step response of (you can create a node that will send a 
square-wave function):  
1. the joint at the base of the robot 

https://user-images.githubusercontent.com/40009146/143324486-7c62110d-9d00-46c1-af9a-ae03b7df1f0d.mov

![base_step](https://user-images.githubusercontent.com/40009146/143324706-9666152e-0d0e-4cbe-869c-04502b3d359b.png)


2. the joint at the end-effector of the robot 

https://user-images.githubusercontent.com/40009146/143324505-068d092e-0c0a-408f-8688-12ace2fe1a19.mov

![end_step](https://user-images.githubusercontent.com/40009146/143324720-5345a48a-cc5b-4b64-896d-9131d6a7eaee.png)

Get the sine-wave response of (you can create a node that will send a sine-wave 
function):  
3. the joint at the base of the robot 

https://user-images.githubusercontent.com/40009146/143324526-d920c683-2617-4fff-882c-7120bd425913.mov

![base_sin](https://user-images.githubusercontent.com/40009146/143324731-7c71d332-0e7e-4b5f-927a-6ae3bea5cf61.png)

4. the joint at the end-effector of the robot 

https://user-images.githubusercontent.com/40009146/143324537-609ec2f8-4dcf-46e0-8b2e-e8a058d0f56d.mov

![end_sin](https://user-images.githubusercontent.com/40009146/143324736-b7593ffc-8307-4d1a-8e39-38133a66419f.png)


## LAB 4

**TASK**: 1. Configure MoveIt library

```
sudo apt install ros-noetic-moveit
```
Steps to follow to create your own moveit package: 
1. Create a new moveit_robot.urdf.xacro file in ~/CATKIN_WORKSPACE/src/ros_snake_robot/robot_description folder. 
2. Copy the content of the  moveit_robot.xacro to new moveit_robot.urdf.xacro file. 
3. ``` roslaunch moveit_setup_assistant setup_assistant.launch``` (link for the moveit_setup_assistant tutorial https://ros-planning.github.io/moveit_tutorials/doc/setup_assistant/setup_assistant_tutorial.html)
4. Press in the moveit_setup_assistant "Create New MoveIt Configuration Package" and browse moveit_robot.urdf.xacro that we created. 
5. Click on the Self-Collisions pane selector on the left-hand side and click on the Generate Collision Matrix button.
6. Click on the Planning Groups pane selector, click on Add Group, enter Group Name (and remember the name as you will need it furthermore, you can name it for example, "joint" or "base"), choose kdl_kinematics_plugin/KDLKinematicsPlugin as the kinematics solver, now, click on the Add Joints button, add m2m, joint2,4,6, then save. 
7. Add group with new name (for instance, "end"), again choose kdl_kinematics_plugin/KDLKinematicsPlugin as the kinematics solver, click on the Add Joints button, add the last joint - "end". 
8. Fill in the Author Information.
9. Create new folder for your moveit package with '''mkdir ~/CATKIN_WORKSPACE/src/{moveit_package_name}''' in the Terminal.
10. Choose path to your new package. Exit the assistant. 
***P.S. if you will want to change something in your package when opening moveit_setup_assistant again, you can choose "Edit Existing MoveIt Configuration Package"***

To check if everything works well:
```
roslaunch {moveit_package_name} demo.launch
```
(link for the Rviz visualization tutorial https://ros-planning.github.io/moveit_tutorials/doc/quickstart_in_rviz/quickstart_in_rviz_tutorial.html)



