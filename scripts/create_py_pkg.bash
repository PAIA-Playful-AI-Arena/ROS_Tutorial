export PKG_NAME=paia_node_py 
export NODE_NAME=publish
ros2 pkg create --build-type ament_python \
--license "Apache License 2.0" \
--maintainer-email "kylingithubdev@gmail.com" \
--maintainer-name "Kylin" \
--description "This is a package to create a framework for development in PAIA." \
--node-name $NODE_NAME \
$PKG_NAME 