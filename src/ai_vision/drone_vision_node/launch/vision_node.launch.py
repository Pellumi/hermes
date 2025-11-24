from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='drone_vision_node',
            executable='drone_vision_node.py',
            name='drone_vision_node',
            output='screen'
        )
    ])
