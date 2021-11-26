#!/usr/bin/env python3
import rospy
import tf
from std_msgs.msg import Float64
from sensor_msgs.msg import JointState
import numpy as np
import csv
import random

rospy.init_node("dataset")
listener = tf.TransformListener()

dataset = {}
pub = [rospy.Publisher('/robot/joint5_position_controller/command', Float64, queue_size=5), rospy.Publisher('/robot/joint2_position_controller/command', Float64, queue_size=5),
rospy.Publisher('/robot/joint3_position_controller/command', Float64, queue_size=5), rospy.Publisher('/robot/joint4_position_controller/command', Float64, queue_size=5), rospy.Publisher('/robot/joint1_position_controller/command', Float64, queue_size=5)]
rate = rospy.Rate(100)
while True:
    angle = np.round(random.uniform(-0.5, 0.5), 2)
    motor = random.randint(0, 4)
    while True:
        pub[motor].publish(Float64(angle))
        s = rospy.wait_for_message('/robot/joint_states', JointState, timeout = 5)
        if (abs(s.position[motor] - angle) < 0.01):
            break
        rate.sleep()
    trans = None
    while trans is None:
        try:
            (trans,rot) = listener.lookupTransform('/world', '/sensor_frame', rospy.Time(0))
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            continue
    q = rospy.wait_for_message('/robot/joint_states', JointState, timeout=5)
    dataset[tuple(np.round(q.position, 4))] = np.round(trans,4)
    rate.sleep()
    print(len(dataset))
    if len(dataset) > 10000:
        break


with open('dict1.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    for key, value in dataset.items():
       writer.writerow([key, value])
