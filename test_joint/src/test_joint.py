#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float64
from sensor_msgs.msg import JointState

def main():
    rospy.init_node('joints')

    while 1:

        a_new = float(input("Joint 1: "))
        b_new = float(input("Joint 2: "))
        c_new = float(input("Joint 3: "))
        d_new = float(input("Joint 4: "))
        e_new = float(input("Joint 5: "))

        pub1 = rospy.Publisher('/robot/joint1_position_controller/command', Float64, queue_size=5)
        pub2 = rospy.Publisher('/robot/joint2_position_controller/command', Float64, queue_size=5)
        pub3 = rospy.Publisher('/robot/joint3_position_controller/command', Float64, queue_size=5)
        pub4 = rospy.Publisher('/robot/joint4_position_controller/command', Float64, queue_size=5)
        pub5 = rospy.Publisher('/robot/joint5_position_controller/command', Float64, queue_size=5)

        while 1:
            pub1.publish(Float64(a_new))
            pub2.publish(Float64(b_new))
            pub3.publish(Float64(c_new))
            pub4.publish(Float64(d_new))
            pub5.publish(Float64(e_new))
            angles = rospy.wait_for_message('/robot/joint_states', JointState, timeout = 5)
            if (abs(angles.position[4] - a_new) < 0.01 and abs(angles.position[1] - b_new) < 0.01 and \
                    abs(angles.position[2] - c_new) < 0.01 and abs(angles.position[3] - d_new) < 0.01 and abs(angles.position[0] - e_new) < 0.01):
                break

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
