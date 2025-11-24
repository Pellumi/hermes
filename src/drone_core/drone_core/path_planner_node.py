import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped
from nav_msgs.msg import Path

class PathPlannerNode(Node):
    def __init__(self):
        super().__init__('path_planner_node')
        
        # Subscribers
        self.goal_sub = self.create_subscription(
            PoseStamped, 'drone/goal', self.goal_cb, 10)
        self.local_pose_sub = self.create_subscription(
            PoseStamped, 'mavros/local_position/pose', self.pose_cb, 10)
            
        # Publishers
        self.path_pub = self.create_publisher(Path, 'drone/path', 10)
        self.setpoint_pub = self.create_publisher(PoseStamped, 'drone/setpoint', 10)
        
        self.current_pose = None
        
        self.get_logger().info("Path Planner Node Started")

    def pose_cb(self, msg):
        self.current_pose = msg

    def goal_cb(self, msg):
        self.get_logger().info(f"Received goal: {msg.pose.position.x}, {msg.pose.position.y}")
        
        if self.current_pose is None:
            self.get_logger().warn("Current pose unknown, cannot plan path")
            return
            
        # Simple straight line planner (just set the goal as the setpoint for now)
        # In a real implementation, we would generate intermediate waypoints
        
        path = Path()
        path.header.stamp = self.get_clock().now().to_msg()
        path.header.frame_id = "map"
        
        # Start point
        path.poses.append(self.current_pose)
        # End point
        path.poses.append(msg)
        
        self.path_pub.publish(path)
        self.setpoint_pub.publish(msg) # Publish the final goal as the immediate setpoint

def main(args=None):
    rclpy.init(args=args)
    node = PathPlannerNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
