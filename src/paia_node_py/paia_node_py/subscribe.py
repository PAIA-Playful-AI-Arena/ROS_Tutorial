import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from .node import SimpleSubscribeNode


class Subscriber(SimpleSubscribeNode):
    def __init__(self, topic: str):
        super().__init__(topic=topic,MSG_TYPE=String)
        self.i =0

    def handle_msg(self,msg):
        
        self.get_logger().info('Heard: "%s"' % msg.data)
        # return msg

def main(args=None):
    # print("hello subscribe")
    rclpy.init(args=args)
    subscriber = Subscriber(topic="paia")

    rclpy.spin(subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
