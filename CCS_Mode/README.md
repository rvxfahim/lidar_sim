# Manual Node for Innok Heros Robot Control

## Overview
This ROS node (`manual_node`) is designed for manual control over a robot's movement, managing the cmd_vel multiplexer based on incoming commands from the `/CCS_Data` topic. It enables control over the robot's motion by selecting appropriate cmd_vel topics.

## Installation
1. Place the Python script into your ROS package structure as follows:
   /home/heros/catkin_ws/src/manual_mode/src/

2. Ensure the script is executable:
   chmod +x manual_node.py

3. Build your catkin workspace using catkin build (not catkin_make):

cd ~/catkin_ws
catkin build

4. Source the setup file to update your environment:
source devel/setup.bash

5. Put the heros_all.launch file in the following dir
/home/heros/cockpit/

## Running the Node
This node is designed to be launched via a launch file which automatically initializes all necessary parameters and nodes. The launch file for the heros robot is executed automatically on boot

## Node Details:

### Subscribed Topics
/CCS_Data (std_msgs/Int8): Listens for commands to control the cmd_vel topic multiplexer:

1: Activates /none/cmd_vel (enables robot movement over cmd_vel topic)

0: Activates /zeros/cmd_vel (disables any movement)
### Services Used
/mux_cmdvel_ui/select (topic_tools/MuxSelect): Switches the active cmd_vel topic based on the received commands.