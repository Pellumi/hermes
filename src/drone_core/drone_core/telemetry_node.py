import rclpy
from rclpy.node import Node
from mavros_msgs.msg import State
from sensor_msgs.msg import BatteryState, NavSatFix
from std_msgs.msg import String
import json

class TelemetryNode(Node):
    def __init__(self):
        super().__init__('telemetry_node')
        
        # Subscribers
        self.state_sub = self.create_subscription(
            State, 'mavros/state', self.state_cb, 10)
        self.battery_sub = self.create_subscription(
            BatteryState, 'mavros/battery', self.battery_cb, 10)
        self.gps_sub = self.create_subscription(
            NavSatFix, 'mavros/global_position/global', self.gps_cb, 10)
            
        # Publishers
        self.telemetry_pub = self.create_publisher(String, 'drone/telemetry', 10)
        
        # State variables
        self.current_state = State()
        self.battery_status = BatteryState()
        self.gps_position = NavSatFix()
        
        # Timer for publishing telemetry
        self.timer = self.create_timer(1.0, self.publish_telemetry)
        
        self.get_logger().info("Telemetry Node Started")

    def state_cb(self, msg):
        self.current_state = msg

    def battery_cb(self, msg):
        self.battery_status = msg

    def gps_cb(self, msg):
        self.gps_position = msg

    def publish_telemetry(self):
        telemetry_data = {
            "mode": self.current_state.mode,
            "armed": self.current_state.armed,
            "connected": self.current_state.connected,
            "battery_percentage": self.battery_status.percentage,
            "latitude": self.gps_position.latitude,
            "longitude": self.gps_position.longitude,
            "altitude": self.gps_position.altitude
        }
        
        msg = String()
        msg.data = json.dumps(telemetry_data)
        self.telemetry_pub.publish(msg)
        self.get_logger().debug(f"Published telemetry: {msg.data}")

def main(args=None):
    rclpy.init(args=args)
    node = TelemetryNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
