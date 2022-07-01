cd  ~/Documents/Ros/dev_ws
# docker build  -t [image_name]:[tag_name] [path]
docker build  -t py_pubsub:latest .
# docker run -it --rm --name [container_name] [image_name] [command and params]
docker run -it --rm --name py_pubsub_container py_pubsub ros2 launch launch/launch_paia_simple_pub_and_sub.py
cd ~/Documents/Ros/dev_ws