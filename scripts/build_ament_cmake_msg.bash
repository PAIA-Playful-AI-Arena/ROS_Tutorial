export PKG_NAME=my_custom_ament_cmake_interface
# export NODE_NAME=py_talker
# !!!! should be at workspace root !!!!
colcon build --symlink-install --packages-select  $PKG_NAME
. install/setup.bash
# ros2 run $PKG_NAME $NODE_NAME