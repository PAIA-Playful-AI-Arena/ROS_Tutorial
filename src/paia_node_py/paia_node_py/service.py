import rclpy
from rclpy.node import Node
from .node import SimpleServiceNode

def main(args=None):
    rclpy.init(args=args)

    minimal_service = SimpleServiceNode(service_name="paia")

    rclpy.spin(minimal_service)

    rclpy.shutdown()


if __name__ == '__main__':
    main()