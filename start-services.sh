#!/bin/bash
# Start roscore in the background
. /ros_entrypoint.sh
# Source ROS Noetic setup
source /opt/ros/noetic/setup.bash
source /home/lajos/catkin_ws/devel/setup.bash
roscore &
ROSCORE_PID=$!

# Wait a bit to ensure roscore is up
sleep 5

# Start Velodyne launch in the background
roslaunch velodyne_pointcloud VLP16_points.launch &
VELODYNE_PID=$!

# Start Gazebo launch in the background
roslaunch innok_heros_gazebo innok_heros_gazebo.launch &
GAZEBO_PID=$!

# Wait for all processes to finish
wait $ROSCORE_PID
wait $VELODYNE_PID
wait $GAZEBO_PID