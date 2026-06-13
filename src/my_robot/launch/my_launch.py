from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='my_robot',
            executable='talker',
            name='my_talker',
            output='screen'
        ),
        Node(
            package='my_robot',
            executable='listener',
            name='my_listener',
            output='screen'
        ),
    ])
