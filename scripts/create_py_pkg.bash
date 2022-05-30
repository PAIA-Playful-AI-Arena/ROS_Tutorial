export PKG_NAME=comm 
export NODE_NAME=collector
ros2 pkg create --build-type ament_python \
--license "Apache License 2.0" \
--maintainer-email "kylingithubdev@gmail.com" \
--maintainer-name "Kylin" \
--description "This is a pkg to demo how to collect local msg and communicate to web." \
--node-name $NODE_NAME \
$PKG_NAME 