cmake_minimum_required(VERSION 3.8)
project(drone_simulation)

find_package(ament_cmake REQUIRED)

# Install launch files
install(DIRECTORY launch
  DESTINATION share/${PROJECT_NAME}
)

# Install world files
# We assume the world file is in ../gazebo_worlds relative to this package source
# But for installation, we should copy it to share/drone_simulation/worlds
# We need to copy from the external directory or move the worlds into this package.
# For simplicity, let's assume we move the world file into this package structure or install it from where it is.
# Current structure: simulation/gazebo_worlds/hermes_world.world
# We will install it explicitly.

install(FILES ../gazebo_worlds/hermes_world.world
  DESTINATION share/${PROJECT_NAME}/worlds
)

# Install models
install(DIRECTORY ../drone_models
  DESTINATION share/${PROJECT_NAME}/models
)

ament_package()
