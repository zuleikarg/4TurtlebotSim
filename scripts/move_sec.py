#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion, quaternion_from_euler

from p1.msg import robot


class MoveRobot:

    def __init__(self):

        self.first = True
        self.state = 0                                                              #state 0: move fordward; state 1: spin
        self.moving = 0
        self.current_x = 0
        self.current_y = 0
        self.current_spin = 0

        self.prev_x = 0
        self.prev_y = 0
        self.prev_spin = 0
    
    def odometry(self,data):
        self.current_x = data.pose.pose.position.x
        self.current_y = data.pose.pose.position.y
        (roll, pitch, self.current_spin) = euler_from_quaternion ([data.pose.pose.orientation.x,data.pose.pose.orientation.y,data.pose.pose.orientation.z,data.pose.pose.orientation.w])

    def begin(self,data):
        self.moving = 1

    def move(self,id):
        global first
        pub = rospy.Publisher('/'+(id)+'/mobile_base/commands/velocity', Twist, queue_size=10)
        pub2 = rospy.Publisher('/'+(id)+'/done', robot, queue_size=10)

        rate = rospy.Rate(1000) # 10hz

        self.prev_x = self.current_x
        self.prev_y = self.current_y
        self.prev_spin = self.current_spin

        while not rospy.is_shutdown():
            message = Twist()
            message2 = robot()

            message.linear.x = 0
            message.linear.y = 0
            message.linear.z = 0
            message.angular.x = 0
            message.angular.y = 0
            message.angular.z = 0
            message2.done = False

            if(self.moving == 1):

                if(self.state == 0):
                    rospy.loginfo("Move fordward")

                    message.linear.x = 0.2

                    total = abs((self.current_x - self.prev_x) + (self.current_y - self.prev_y))

                    if(total >= 0.9):
                        self.state = 1
                        self.prev_x = self.current_x
                        self.prev_y = self.current_y
                        self.prev_spin = self.current_spin

                else:
                    rospy.loginfo("Spin")

                    message.angular.z = -0.5

                    total = abs((self.current_spin - self.prev_spin))

                    if(total >= 1.25):
                        self.state = 0
                        self.prev_x = self.current_x
                        self.prev_y = self.current_y
                        self.prev_spin = self.current_spin

                        self.moving = 0
                        message2.done = True
                        pub2.publish(message2)

            if(id == "robot1" and self.first == True):
                self.first = False
                self.moving = 1

            pub.publish(message)
            rate.sleep()
 
if __name__ == '__main__':
    try:
        rospy.init_node('move_sec_robot', anonymous=True, log_level=rospy.WARN)
        robot_id = str.lower(rospy.get_param('~robot_id'))

        robot_movement = MoveRobot()

        # num = [int(x) for x in robot_id.split() if x.isdigit()]
        num=0
        for c in robot_id:
            if c.isdigit():
                num = num + int(c)
        num = num-1

        if(num == 0):
            num=4

        rospy.Subscriber('/robot'+str(num)+'/done', robot, robot_movement.begin)
        rospy.Subscriber('/'+(robot_id)+'/odom', Odometry, robot_movement.odometry)

        robot_movement.move(robot_id)

    except rospy.ROSInterruptException:
        pass