#!/usr/bin/env python3
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()

    listener_node = Node(
        package="mobrob_praktikum_lt",
        executable="mein_listener_oop",
        name="listener_launched"
    )

    talker_node = Node(
        package="mobrob_praktikum_lt",
        executable="mein_talker_oop",
        name="talker_launched"
    )
     

    ld.add_action(listener_node)
    ld.add_action(talker_node)
    return ld