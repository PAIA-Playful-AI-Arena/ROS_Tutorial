export PKG_NAME=PAIA_NODE_PY 
export NODE_NAME=BasicPublishNode
# !!!! should be at workspace root !!!!
colcon build --packages-select $PKG_NAME
. install/setup.bash
ros2 run $PKG_NAME $NODE_NAME