#!/usr/bin/env python3
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()

    sim_node = Node(
        package="mobrob_simplebot",
        executable="simplebot_sim",
        name="simulation"
    )

    control_node = Node(
        package="mobrob_simplebot",
        executable="simplebot_control_ps",
        name="controller"
    )



    ld.add_action(sim_node)
    ld.add_action(control_node)
    return ld