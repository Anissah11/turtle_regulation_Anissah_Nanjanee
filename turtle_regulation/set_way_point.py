import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
from std_msgs.msg import Bool
import math

class SetWayPoint(Node):
    def __init__(self):
        super().__init__('set_way_point')
        self.pose = None
        self.waypoint = {'x': 7.0, 'y': 7.0}
        self.Kp = 2.0
        self.Kpl = 1.5
        self.distance_tolerance = 0.2

        self.pose_sub = self.create_subscription(
            Pose, '/turtle1/pose', self.pose_callback, 10)
        self.cmd_pub = self.create_publisher(
            Twist, '/turtle1/cmd_vel', 10)
        self.is_moving_pub = self.create_publisher(
            Bool, 'is_moving', 10)
        self.timer = self.create_timer(0.1, self.control_loop)

    def pose_callback(self, msg):
        self.pose = msg

    def control_loop(self):
        if self.pose is None:
            return

        distance = math.sqrt(
            (self.waypoint['x'] - self.pose.x) ** 2 +
            (self.waypoint['y'] - self.pose.y) ** 2
        )

        is_moving_msg = Bool()

        if distance > self.distance_tolerance:
            theta_desired = math.atan2(
                self.waypoint['y'] - self.pose.y,
                self.waypoint['x'] - self.pose.x
            )
            e = math.atan2(
                math.sin(theta_desired - self.pose.theta),
                math.cos(theta_desired - self.pose.theta)
            )
            cmd = Twist()
            cmd.angular.z = self.Kp * e
            cmd.linear.x = self.Kpl * distance
            self.cmd_pub.publish(cmd)
            is_moving_msg.data = True
        else:
            self.cmd_pub.publish(Twist())
            is_moving_msg.data = False

        self.is_moving_pub.publish(is_moving_msg)

def main(args=None):
    rclpy.init(args=args)
    node = SetWayPoint()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
