# Use the official OSRF ROS Noetic desktop full image
FROM osrf/ros:noetic-desktop-full
RUN mkdir -p /rosstart
COPY start-roscore.sh /rosstart
COPY start-gazebo.sh /rosstart
COPY entrypoint.sh /rosstart
RUN chmod +x /rosstart/entrypoint.sh
RUN chmod +x /rosstart/start-gazebo.sh
RUN chmod +x /rosstart/start-roscore.sh
RUN mkdir -p /home/lajos
RUN mkdir -p /home/lajos/catkin_ws
COPY catkin_ws/. /home/lajos/catkin_ws
WORKDIR /home/lajos/catkin_ws
# RUN /bin/bash -c '. /opt/ros/noetic/setup.bash; catkin_make'
# RUN echo "source /home/lajos/catkin_ws/devel/setup.bash" >> ~/.bashrc

# Install some useful tools and dependencies for development
RUN apt-get update && apt-get install -y \
    ros-noetic-velodyne \
    supervisor \
    bash \ 
    dos2unix \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Setup environment variables needed for ROS
ENV ROS_WS=/home/lajos/catkin_ws

# # Create a catkin workspace
# RUN mkdir -p $ROS_WS/src && \
#     /bin/bash -c "source /opt/ros/noetic/setup.bash; catkin_init_workspace $ROS_WS/src"

# Build the catkin workspace
RUN /bin/bash -c "source /opt/ros/noetic/setup.bash; cd $ROS_WS; catkin_make"

# Automatically source the workspace in each bash session
RUN echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc && \
    echo "source $ROS_WS/devel/setup.bash" >> ~/.bashrc

# Set the default command to execute
# Keeps the container running and provides an interactive shell
# CMD ["bash"]
# Copy the Supervisor configuration file to the container
# COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# ENTRYPOINT ["sh","/rosstart/entrypoint.sh"]
COPY start-services.sh /rosstart/start-services.sh
RUN chmod +x /rosstart/start-services.sh