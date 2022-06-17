import random
import rclpy
from rclpy.node import Node
from .node import SimpleServiceNode
from paia_demo_interface.srv import Distance
from .config import service_setting

#include "my_custom_ament_cmake_interface/srv/add_three_ints.hpp"     // CHANGE

class MyService(SimpleServiceNode):
    def __init__(self):
        super().__init__(service_setting.service_name, Distance)
        self.get_logger().info(f"{service_setting.service_name} start with Msg {Distance}")
    
    def get_response(self, request, response):
        self.get_logger().info(f"Received {request}")
        response.distance = random.randint(1,10)
        return response



def main(args=None):
    rclpy.init(args=args)

    minimal_service = MyService()

    rclpy.spin(minimal_service)

    rclpy.shutdown()


if __name__ == '__main__':
    main()