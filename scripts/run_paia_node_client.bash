export PKG_NAME=paia_node_py 
export EXECUTABLE=client
. install/setup.bash 
ros2 run $PKG_NAME $EXECUTABLE