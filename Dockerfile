# FROM osrf/ros:foxy-desktop
FROM paia/ros2-base:latest

ENV ROS2_WS /root/ros_workspace
COPY . ${ROS2_WS}

WORKDIR ${ROS2_WS}
# RUN pip3 install -r requirements.txt
# RUN pip3 freeze | grep pytest \
#     && python3 -m pytest --version

RUN . /opt/ros/foxy/setup.sh && \
    colcon build --symlink-install && \
    . ${ROS2_WS}/install/setup.sh
    
# =================================
COPY ./ros_entrypoint.sh /
ENTRYPOINT [ "/ros_entrypoint.sh" ] 
# CMD [ "tail",'-f','/dev/null' ]
CMD ["bash"]
