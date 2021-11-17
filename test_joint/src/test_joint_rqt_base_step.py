#!/usr/bin/env python3
import rospy
from time import sleep
from std_msgs.msg import Float64
from sensor_msgs.msg import JointState
import numpy as np

def main():
    rospy.init_node('joints')
    radian = -1.0
    output = 0
    while True:
        if output == -1:
            output = 1
        else: 
            output = -1
            
        a_new = output
        e_new = 0

        pub1 = rospy.Publisher('/robot/joint1_position_controller/command', Float64, queue_size=5)
        pub5 = rospy.Publisher('/robot/joint5_position_controller/command', Float64, queue_size=5)

        while not False:
            pub1.publish(Float64(a_new))
            pub5.publish(Float64(e_new))
            angles = rospy.wait_for_message('/robot/joint_states', JointState, timeout = 5)

            if (abs(angles.position[4] - a_new) < 0.01 and abs(angles.position[0] - e_new) < 0.01):
                break

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass




