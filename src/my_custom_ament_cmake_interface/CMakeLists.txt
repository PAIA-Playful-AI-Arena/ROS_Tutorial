cmake_minimum_required(VERSION 3.5)
project(my_custom_ament_cmake_interface)

# Default to C99
if(NOT CMAKE_C_STANDARD)
  set(CMAKE_C_STANDARD 99)
endif()

# Default to C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
# uncomment the following section in order to fill in
# further dependencies manually.
# find_package(<dependency> REQUIRED)


if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  # the following line skips the linter which checks for copyrights
  # uncomment the line when a copyright and license is not present in all source files
  #set(ament_cmake_copyright_FOUND TRUE)
  # the following line skips cpplint (only works in a git repo)
  # uncomment the line when this package is not in a git repo
  #set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

find_package(rosidl_default_generators REQUIRED)

rosidl_generate_interfaces(${PROJECT_NAME}
  "msg/Num.msg"
  "srv/AddThreeInts.srv"
)


find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(my_custom_ament_cmake_interface REQUIRED)                         # CHANGE

add_executable(num_talker src/num_talker.cpp)
ament_target_dependencies(num_talker rclcpp my_custom_ament_cmake_interface)         # CHANGE

add_executable(num_listener src/num_listener.cpp)
ament_target_dependencies(num_listener rclcpp my_custom_ament_cmake_interface)     # CHANGE

install(TARGETS
  num_talker
  num_listener
  DESTINATION lib/${PROJECT_NAME})



find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(my_custom_ament_cmake_interface REQUIRED)        # CHANGE

add_executable(add_three_ints_server src/add_three_ints_server.cpp)
ament_target_dependencies(add_three_ints_server
  rclcpp my_custom_ament_cmake_interface)                      #CHANGE

add_executable(add_three_ints_client src/add_three_ints_client.cpp)
ament_target_dependencies(add_three_ints_client
  rclcpp my_custom_ament_cmake_interface)                      #CHANGE

install(TARGETS
  add_three_ints_server
  add_three_ints_client
  DESTINATION lib/${PROJECT_NAME})

ament_package()