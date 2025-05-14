#!/usr/bin/env python3
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess

def generate_launch_description():
    ld = LaunchDescription()

    sim_node = Node(
        package="turtlesim",
        executable="turtlesim_node",
        name="simulation"
    )

    converter_node = Node(
        package="mobrob_simplebot",
        executable="turtlesim_pose_converter",
        name="converter"
    )


    control_node = Node(
        package="mobrob_simplebot",
        executable="simplebot_control_ps",
        name="controller"
    )

    # Add rqt
    add_rqt = ExecuteProcess(
        cmd=['rqt'],
        output='screen',
    )


    ld.add_action(sim_node)
    ld.add_action(converter_node)
    ld.add_action(control_node)
    ld.add_action(add_rqt)
    return ld