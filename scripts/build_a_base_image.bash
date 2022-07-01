cd  ~/Documents/Ros/dev_ws/ros_docker
# docker build  -t [image_name]:[tag_name] [path]
docker build  -t paia/ros2-base:latest .
# docker run -it --rm --name [container_name] [image_name] [command and params]
cd ~/Documents/Ros/dev_ws