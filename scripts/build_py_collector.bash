export PKG_NAME=comm
export NODE_NAME=collector
# !!!! should be at workspace root !!!!
colcon build --packages-select $PKG_NAME

echo "Completeted"
. install/setup.bash
# ros2 run $PKG_NAME $NODE_NAME