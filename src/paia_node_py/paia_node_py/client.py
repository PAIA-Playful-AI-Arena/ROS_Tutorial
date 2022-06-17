import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from .node import SimpleClientNode
from paia_demo_interface.srv import Distance
from .config import service_setting


def main(args=None):
    rclpy.init(args=args)

    minimal_client = SimpleClientNode(service_name=service_setting.service_name,SRV_TYPE= Distance)
    request = Distance.Request()
    request.device_type = "Sonic"
    resp = minimal_client.send_request_and_get_resp(request)
    print(resp)
    minimal_client.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()