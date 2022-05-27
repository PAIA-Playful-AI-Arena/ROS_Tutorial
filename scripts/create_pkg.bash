export PKG_NAME=my_custom_ament_cmake_interface 
ros2 pkg create --build-type ament_cmake \
--license "Apache License 2.0" \
--maintainer-email "kylingithubdev@gmail.com" \
--maintainer-name "Kylin" \
--description "This is a pkg to demo how to create custom msg interface." \
$PKG_NAME 