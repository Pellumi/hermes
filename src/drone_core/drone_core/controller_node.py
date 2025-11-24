import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped
from mavros_msgs.msg import State
from mavros_msgs.srv import CommandBool, SetMode

class ControllerNode(Node):
    def __init__(self):
        super().__init__('controller_node')
        
        # Subscribers
        self.state_sub = self.create_subscription(
            State, 'mavros/state', self.state_cb, 10)
        self.setpoint_sub = self.create_subscription(
            PoseStamped, 'drone/setpoint', self.setpoint_cb, 10)
            
        # Publishers
        self.local_pos_pub = self.create_publisher(
            PoseStamped, 'mavros/setpoint_position/local', 10)
            
        # Services
        self.arming_client = self.create_client(CommandBool, 'mavros/cmd/arming')
        self.set_mode_client = self.create_client(SetMode, 'mavros/set_mode')
        
        # State variables
        self.current_state = State()
        self.target_pose = None
        
        # Timer for control loop
        self.timer = self.create_timer(0.05, self.control_loop) # 20Hz
        
        self.get_logger().info("Controller Node Started")

    def state_cb(self, msg):
        self.current_state = msg

    def setpoint_cb(self, msg):
        self.target_pose = msg

    def control_loop(self):
        if self.target_pose is None:
            return
            
        # Publish setpoint to MAVROS
        # Ensure timestamp is current
        self.target_pose.header.stamp = self.get_clock().now().to_msg()
        self.local_pos_pub.publish(self.target_pose)
        
        # Auto-arm and set OFFBOARD mode (simplified logic for demo)
        # In a real system, this should be triggered by a specific command, not auto-loop
        # But for simulation testing, we might want to ensure we are in OFFBOARD mode if we have a target
        
        if self.current_state.mode != "OFFBOARD" and (self.get_clock().now().nanoseconds / 1e9) > 5.0:
             # Wait 5 seconds before trying to switch mode to allow connection
             self.set_mode("OFFBOARD")
             
        if not self.current_state.armed and self.current_state.mode == "OFFBOARD":
            self.arm()

    def set_mode(self, mode):
        if self.set_mode_client.wait_for_service(timeout_sec=1.0):
            req = SetMode.Request()
            req.custom_mode = mode
            future = self.set_mode_client.call_async(req)
            # We don't wait for result here to avoid blocking loop

    def arm(self):
        if self.arming_client.wait_for_service(timeout_sec=1.0):
            req = CommandBool.Request()
            req.value = True
            future = self.arming_client.call_async(req)

def main(args=None):
    rclpy.init(args=args)
    node = ControllerNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
