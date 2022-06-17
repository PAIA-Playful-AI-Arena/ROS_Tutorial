from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='paia_node_py',
            namespace='paia_node',
            executable='publish',
            
        ),
        Node(
            package='paia_node_py',
            namespace='paia_node',
            executable='subscribe',
            
        ),
    ])