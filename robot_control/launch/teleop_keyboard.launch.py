import os

from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    remap_cmd_vel = ('/cmd_vel', '/cmd_vel_key')
    remap_odom = ('/odom', 'my_robot/odom')

    teleop_keyboard_node = Node(
        package="teleop_twist_keyboard",
        executable="teleop_twist_keyboard",
        name="teleop_twist_keyboard",
        prefix='xterm -e',
        remappings=[remap_cmd_vel]            
        # remappings=[remap_cmd_vel, remap_odom]
        )

    return LaunchDescription([
        teleop_keyboard_node
    ])