#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from std_msgs.msg import String
from cv_bridge import CvBridge
import cv2
from ultralytics import YOLO
import numpy as np
import time


class DroneVisionNode(Node):
    def __init__(self):
        super().__init__("drone_vision_node")
        self.get_logger().info("🚀 Hermes Drone Vision Node Initialized")

        # Initialize CV bridge and YOLO model
        self.bridge = CvBridge()
        self.model = YOLO("yolov8n.pt")  # Lightweight model; upgrade later

        # Parameters
        self.conf_threshold = 0.45
        self.frame_skip = 2  # Process every 2nd frame for speed
        self.frame_count = 0

        # ROS2 topics
        self.subscription = self.create_subscription(
            Image, "/camera/image_raw", self.image_callback, 10
        )
        self.publisher = self.create_publisher(String, "/vision/obstacles", 10)

    def image_callback(self, msg):
        self.frame_count += 1
        if self.frame_count % self.frame_skip != 0:
            return

        start_time = time.time()

        # Convert ROS2 image to OpenCV image
        frame = self.bridge.imgmsg_to_cv2(msg, desired_encoding="bgr8")

        # Run YOLO detection
        results = self.model(frame, verbose=False)
        detections = []

        for r in results:
            boxes = r.boxes
            for box in boxes:
                cls_id = int(box.cls[0])
                conf = float(box.conf[0])
                if conf < self.conf_threshold:
                    continue
                label = self.model.names[cls_id]
                detections.append(label)

                # Draw bounding boxes for visualization
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(
                    frame,
                    f"{label} {conf:.2f}",
                    (x1, y1 - 5),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6,
                    (0, 255, 0),
                    2,
                )

        # Publish detections
        if detections:
            msg_out = String()
            msg_out.data = ",".join(set(detections))
            self.publisher.publish(msg_out)
            self.get_logger().info(f"🧠 Detected: {msg_out.data}")

        # Performance logging
        latency = (time.time() - start_time) * 1000
        self.get_logger().info(f"Frame latency: {latency:.1f} ms")

        # Optional visualization
        cv2.imshow("Hermes Drone Vision", frame)
        cv2.waitKey(1)


def main(args=None):
    rclpy.init(args=args)
    node = DroneVisionNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info("Shutting down Drone Vision Node")
    finally:
        node.destroy_node()
        rclpy.shutdown()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
