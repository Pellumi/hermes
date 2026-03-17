import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument

def generate_launch_description():
    # Get the directory of the world file
    # In a real setup, we would install the world file to share/
    # For now, we point to the source or assume it's installed
    
    # We need to find where the world file is. 
    # Since we are creating a package 'drone_simulation', it should be in share/drone_simulation/worlds
    
    pkg_share = get_package_share_directory('drone_simulation')
    world_file = os.path.join(pkg_share, 'worlds', 'hermes_world.world')
    
    # URDF file
    # We assume the model file is in simulation/drone_models/iris_base.xacro
    # Since we didn't install it in CMakeLists yet, we might need to point to source or install it
    # Let's assume we will install it to share/drone_simulation/models
    
    # For now, let's point to the source file if possible, or better, install it.
    # We will update CMakeLists.txt to install the models directory.
    
    urdf_file = os.path.join(get_package_share_directory('drone_simulation'), 'models', 'iris_base.xacro')

    return LaunchDescription([
        DeclareLaunchArgument(
            'world',
            default_value=world_file,
            description='Path to world file'
        ),
        
        # Launch Gazebo
        ExecuteProcess(
            cmd=['gazebo', '--verbose', LaunchConfiguration('world'), '-s', 'libgazebo_ros_init.so', '-s', 'libgazebo_ros_factory.so'],
            output='screen'
        ),
        
        # Publish Robot State
        # We need to process xacro first. 
        # For simplicity in this step, we'll assume xacro is processed or we use a simple command substitution if needed.
        # But 'xacro' command is available.
        
        ExecuteProcess(
            cmd=['xacro', urdf_file, '-o', '/tmp/drone.urdf'],
            output='screen'
        ),
        
        # Spawn Entity
        ExecuteProcess(
            cmd=['ros2', 'run', 'gazebo_ros', 'spawn_entity.py', '-file', '/tmp/drone.urdf', '-entity', 'hermes_drone', '-x', '0', '-y', '0', '-z', '0.5'],
            output='screen'
        ),
    ])
