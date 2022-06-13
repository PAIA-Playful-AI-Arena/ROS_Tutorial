export PKG_NAME=paia_node_py 
# !!!! should be at workspace root !!!!
colcon build --packages-select $PKG_NAME --symlink-install --event-handlers console_direct+

