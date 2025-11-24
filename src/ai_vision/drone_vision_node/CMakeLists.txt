cmake_minimum_required(VERSION 3.8)
project(drone_vision_node)

find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)

install(
  PROGRAMS
    src/drone_vision_node.py
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()
