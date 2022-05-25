export PKG_NAME=py_pubsub
export NODE_NAME=py_talker
# !!!! should be at workspace root !!!!
colcon build --packages-select $PKG_NAME
. install/setup.bash
ros2 run $PKG_NAME $NODE_NAME