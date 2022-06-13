import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from .node import SimpleClientNode

def main(args=None):
    rclpy.init(args=args)

    minimal_client = SimpleClientNode(service_name="paia")
    minimal_client.send_request()
    minimal_client.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()