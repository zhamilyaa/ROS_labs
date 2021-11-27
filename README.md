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

https://user-images.githubusercontent.com/40009146/143334838-46552277-8d4a-4bcc-a4c1-ead42a228435.mov


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

File to run is located in scripts/src/test.cpp
```
rosrun scripts test_test
```


https://user-images.githubusercontent.com/40009146/143573960-956a1310-ec5d-4f1a-a00f-e942235f4656.mov


3. Create a node that moves “end” to Draw a rectangle
File to run is located in scripts/src/test_rectangle.cpp

```
rosrun scripts test_rect
```

https://user-images.githubusercontent.com/40009146/143570345-b3cd5076-ceab-453a-9853-a58260c6110f.mov


## LAB 5

## LAB 6

**TASK**: Obtain Forward Kinematics without the robot model

Dataset is located in scripts/src/dict1.csv. Dataset was obtained by scripts/src/dataset.py

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
        X.append(result)
        result = [float(val) for val in labels[i].split(' ')]
        Y.append(result)

    X_train, X_test, y_train, y_test = train_test_split(np.asarray(X), np.asarray(Y), test_size=0.80)
    print("TRAIN X SHAPE ", np.shape(X_train))
    print("TRAIN Y SHAPE ", np.shape(y_train))
    print("TEST X SHAPE ", np.shape(X_test))
    print("TEST Y SHAPE ", np.shape(y_test))
```
![Screenshot from 2021-11-25 06-09-07](https://user-images.githubusercontent.com/40009146/143327912-8e702cd5-7d1c-4a75-8acf-469c1f6a8352.png)

Loss Function: Root Mean Square
```
def rmse(y_true, y_pred):
        return K.sqrt(K.mean(K.square(y_pred - y_true)))
```

Model
```
    model = Sequential()
    model.add(Dense(10, input_dim = 5, activation = 'relu'))
    model.add(Dense(16, activation = 'relu'))
    model.add(Dense(3, activation='linear'))
    model.compile(loss=rmse, optimizer=Adam(0.01))
    print(model.summary())
```
![Screenshot from 2021-11-25 06-13-26](https://user-images.githubusercontent.com/40009146/143328099-817f5497-826d-491f-a2d0-c924a4166a02.png)


```
    model.fit(X_train, y_train, epochs = 15)
    scores = model.evaluate(X_test, y_test, verbose=0) 
    print("RMSE: %.2f" % (scores))
```
RMSE: 0.10

### CHANGING THE LOSSES
1. Mean Squared Logarithmic Error
```
    model = Sequential()
    model.add(Dense(10, input_dim =5, activation = 'relu'))
    model.add(Dense(16, activation = 'relu'))
    model.add(Dense(3, activation='linear'))
    model.compile(loss='mean_squared_logarithmic_error', optimizer=keras.optimizers.Adam(0.01))

```
```
mean_squared_logarithmic_error 0.0005
```
3. Mean Absolute Error
```
    model = Sequential()
    model.add(Dense(10, input_dim =5, activation = 'relu'))
    model.add(Dense(16, activation = 'relu'))
    model.add(Dense(3, activation='linear'))
    model.compile(loss='mean_absolute_error', optimizer=keras.optimizers.Adam(0.01))

```
```
mean_absolute_error 0.0331
```

2. Mean Squared Error
```
    model = Sequential()
    model.add(Dense(10, input_dim =5, activation = 'relu'))
    model.add(Dense(16, activation = 'relu'))
    model.add(Dense(3, activation='linear'))
    model.compile(loss='mean_squared_error', optimizer=keras.optimizers.Adam(0.01))

```
```
mean_squared_error 0.0036
```
4. Root Mean Squared Error

```
    model = Sequential()
    model.add(Dense(10, input_dim =5, activation = 'relu'))
    model.add(Dense(16, activation = 'relu'))
    model.add(Dense(3, activation='linear'))
    model.compile(loss=rmse, optimizer=keras.optimizers.Adam(0.01))
```
```
rmse 0.0508
```
Mean Squared Logarithmic Error showed the best results.

### CHANGING THE NUMBER OF LAYERS
Layer number Mean Squared Logarithmic Error  
2 ------------> 0.000359  
3 ------------> 0.088592  
4 ------------> 0.088045  
5 ------------> 0.088894  
6 ------------> 0.000551  
7 ------------> 0.000601  

2 layers showed the best results.

### CHANGING THE ACTIVATION FUNCTIONS

1. Tanh
```
    model = Sequential()
    model.add(Dense(10, input_dim =5, activation = 'tanh'))
    model.add(Dense(16, activation = 'tanh'))
    model.add(Dense(16, activation = 'tanh'))
    model.add(Dense(3, activation='linear'))
    model.compile(loss='mean_squared_logarithmic_error', optimizer=keras.optimizers.Adam(0.01))
```
```
0.000190
```
2. Sigmoid
```
    model = Sequential()
    model.add(Dense(10, input_dim =5, activation = 'sigmoid'))
    model.add(Dense(16, activation = 'sigmoid'))
    model.add(Dense(16, activation = 'sigmoid'))
    model.add(Dense(3, activation='linear'))
    model.compile(loss='mean_squared_logarithmic_error', optimizer=keras.optimizers.Adam(0.01))
```
```
0.017334
```
3. Linear
```
    model = Sequential()
    model.add(Dense(10, input_dim =5, activation = 'linear'))
    model.add(Dense(16, activation = 'linear'))
    model.add(Dense(16, activation = 'linear'))
    model.add(Dense(3, activation='linear'))
    model.compile(loss='mean_squared_logarithmic_error', optimizer=keras.optimizers.Adam(0.01))
```
```
0.002832
```
4. Softmax
```
    model = Sequential()
    model.add(Dense(10, input_dim =5, activation = 'softmax'))
    model.add(Dense(16, activation = 'softmax'))
    model.add(Dense(16, activation = 'softmax'))
    model.add(Dense(3, activation='linear'))
    model.compile(loss='mean_squared_logarithmic_error', optimizer=keras.optimizers.Adam(0.01))
```
```
0.019299
```
Tanh showed the best results

### RESULTS

Mean Squared Logarithmic Error: 0.000215  

Dataset Size -> 10000   
Number of Hidden Layers -> 2   
Optimizer -> Adam   
Activation Function -> Tanh   
Loss -> Mean Squared Logarithmic Error   
Epochs -> 15   

## LAB 7
**TASK**: Obtain Inverse Kinematics without the robot model

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
    print("TRAIN X SHAPE ", np.shape(X_train))
    print("TRAIN Y SHAPE ", np.shape(y_train))
    print("TEST X SHAPE ", np.shape(X_test))
    print("TEST Y SHAPE ", np.shape(y_test))
```
![Screenshot from 2021-11-25 07-09-55](https://user-images.githubusercontent.com/40009146/143334271-5b070d3d-aea8-4d87-91f1-fe1abbd6d2e9.png)


Model
```
    model = Sequential()
    model.add(Dense(10, input_dim =3, activation = 'tanh'))
    model.add(Dense(16, activation = 'tanh'))
    model.add(Dense(16, activation = 'tanh'))
    model.add(Dense(16, activation = 'tanh'))
    model.add(Dense(16, activation = 'tanh'))
    model.add(Dense(16, activation = 'tanh'))
    model.add(Dense(16, activation = 'tanh'))
    model.add(Dense(16, activation = 'tanh'))
    model.add(Dense(16, activation = 'tanh'))
    model.add(Dense(5, activation='linear'))
    model.compile(loss='mean_squared_logarithmic_error', optimizer=keras.optimizers.Adam(0.01))
```
Model Fitting

```
    model.fit(X_train, y_train, epochs = 200)
    scores = model.evaluate(X_test, y_test, verbose=0) 
    print("RMSE: %.2f" % (scores))
```
![Screenshot from 2021-11-25 07-01-55](https://user-images.githubusercontent.com/40009146/143334137-68505e5d-35e9-4726-9d96-b16f32907e27.png)

### RESULTS

Mean Squared Logarithmic Error: 0.015960

Dataset Size -> 10000  
Number of Hidden Layers -> 8  
Optimizer -> Adam  
Activation Function -> Tanh  
Loss -> Mean Squared Logarithmic Error  
Epochs -> 200  
