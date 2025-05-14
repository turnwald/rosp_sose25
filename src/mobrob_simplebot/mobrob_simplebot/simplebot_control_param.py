import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Pose2D, Twist
import math

class RobotNavigator(Node):
    def __init__(self):
        super().__init__('simplebot_control_p')
        
        # Declare parameters for the goal position
        self.declare_parameter('goal_x', 5.0)  # Default goal x-coordinate
        self.declare_parameter('goal_y', 5.0)  # Default goal y-coordinate
        
        # Publisher for robot's velocity
        self.velocity_publisher = self.create_publisher(Twist, 'cmd_vel', 10)
        
        # Subscriber for robot's pose
        self.pose_subscriber = self.create_subscription(Pose2D, 'robot_pose2d', self.pose_callback, 10)
        
        # Initial goal point
        self.goal = Pose2D()
        self.update_goal()  # Initialize the goal position
        
        # Robot's current pose
        self.current_pose = Pose2D()
        
        # Control gains
        self.K1 = 1.0  # Gain for angular velocity
        self.K2 = 0.5  # Gain for linear velocity
        
        # Timer to update the robot's movement
        self.timer = self.create_timer(0.1, self.navigate_to_goal)

    def pose_callback(self, msg):
        self.current_pose = msg

    def update_goal(self):
        # Update the goal position from parameters
        self.goal.x = self.get_parameter('goal_x').get_parameter_value().double_value
        self.goal.y = self.get_parameter('goal_y').get_parameter_value().double_value
        self.get_logger().info(f"Goal is set to: ({self.goal.x}, {self.goal.y})")

    def navigate_to_goal(self):
        self.update_goal() # Update the goal
        # Calculate the distance to the goal
        delta_x = self.goal.x - self.current_pose.x
        delta_y = self.goal.y - self.current_pose.y
        distance = math.sqrt(delta_x**2 + delta_y**2)
        
        # Create a Twist message for velocity
        velocity_msg = Twist()
        
        if distance > 0.01:  # If the robot is not close to the goal
            # Calculate the desired angle to the goal
            delta_psi = math.atan2(delta_y, delta_x)
            # Calculate the orientation error
            e_psi = delta_psi - self.current_pose.theta
            
            # Normalize the orientation error to the range [-pi, pi]
            e_psi = (e_psi + math.pi) % (2 * math.pi) - math.pi
            
            if abs(e_psi) > 0.01:  # If the orientation error is large enough
                velocity_msg.angular.z = self.K1 * e_psi  # Turn towards the goal
                velocity_msg.linear.x = 0.0  # Stop moving forward
            else:
                velocity_msg.angular.z = 0.0  # Stop turning
                velocity_msg.linear.x = self.K2 * distance  # Move towards the goal
        else:
            # Stop the robot if the goal is reached
            velocity_msg.linear.x = 0.0
            velocity_msg.angular.z = 0.0
        
        # Publish the velocity command
        self.velocity_publisher.publish(velocity_msg)

def main(args=None):
    rclpy.init(args=args)
    robot_navigator = RobotNavigator()
    rclpy.spin(robot_navigator)
    robot_navigator.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
