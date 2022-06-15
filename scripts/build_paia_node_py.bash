export PKG_NAME=paia_node_py 
# !!!! should be at workspace root !!!!
pip install -r src/$PKG_NAME/requirements.txt
colcon build --packages-select paia_demo_interface --symlink-install --event-handlers console_direct+
colcon build --packages-select $PKG_NAME --symlink-install --event-handlers console_direct+