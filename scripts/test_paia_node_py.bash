export PKG_NAME=paia_node_py 

colcon test --return-code-on-test-failure --packages-select $PKG_NAME --python-testing pytest --event-handlers console_direct+