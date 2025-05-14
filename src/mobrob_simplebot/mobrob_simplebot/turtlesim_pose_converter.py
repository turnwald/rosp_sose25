import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from geometry_msgs.msg import Pose2D, Twist

class TurtlesimPoseConverter(Node):
    def __init__(self):
        super().__init__('turtlesim_pose_converter')
        self.pose_subscriber = self.create_subscription(
            Pose,
            '/turtle1/pose',
            self.pose_callback,
            10
        )
        self.twist_subscriber = self.create_subscription(
            Twist,
            '/cmd_vel',
            self.twist_callback,
            10
        )
        self.pose2d_publisher = self.create_publisher(Pose2D, 'robot_pose2d', 10)
        self.twist_publisher = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)

    def pose_callback(self, msg):
        pose2d_msg = Pose2D()
        pose2d_msg.x = msg.x
        pose2d_msg.y = msg.y
        pose2d_msg.theta = msg.theta
        self.pose2d_publisher.publish(pose2d_msg)

    def twist_callback(self, msg):
        twist_msg = Twist()
        twist_msg = msg
        self.twist_publisher.publish(twist_msg)

def main(args=None):
    rclpy.init(args=args)
    turtlesim_pose_converter = TurtlesimPoseConverter()
    rclpy.spin(turtlesim_pose_converter)
    turtlesim_pose_converter.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
