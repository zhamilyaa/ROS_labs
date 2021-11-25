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

My MoveIt package is called "lab4". 

2. Create a node moves the “end” by 1.4 (in rviz units mm or m) along X axis

3. Create a node that moves “end” to Draw a rectangle

4. Create a node that moves “end” to Draw a circle

## LAB 5

## LAB 6

Importing libraries. 
```
import numpy as np
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense
from keras import backend as K
import pandas as pd
from sklearn.model_selection import train_test_split
```

Reading generated csv file. 
```
def main():
    data = pd.read_csv("/home/zhamilya/catkin_ws_zhamilya/dict1.csv", header = None, names = ["Angles", "XY"])
    print(data.head(10))
```
![Screenshot from 2021-11-25 06-04-22](https://user-images.githubusercontent.com/40009146/143327639-f64b5749-79aa-4c91-b423-051940c4586b.png)

Splitting into train and test. 

```
    train = data['Angles'].to_numpy()
    labels = data['XY'].to_numpy()

    X = list()
    Y = list()
    for i in range(len(train)):
        labels[i] = labels[i].replace('     ', ' ')
        labels[i] = labels[i].replace('   ', ' ')
        labels[i] = labels[i].replace('  ', ' ')
        labels[i] = labels[i].strip('[ ').strip(' ]')
        train[i] = train[i].strip('(').strip(')')
        result = [float(val) for val in train[i].split(',')]
        Y.append(result)
        result = [float(val) for val in labels[i].split(' ')]
        X.append(result)

    X_train, X_test, y_train, y_test = train_test_split(np.asarray(X), np.asarray(Y), test_size=0.80)
```
TRAIN X SHAPE  (2000, 5)
TRAIN Y SHAPE  (2000, 3)
TEST X SHAPE  (8001, 5)
TEST Y SHAPE  (8001, 3)

```
def rmse(y_true, y_pred):
        return K.sqrt(K.mean(K.square(y_pred - y_true)))
```

## LAB 7

