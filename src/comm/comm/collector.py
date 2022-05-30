from time import time
from traceback import print_stack
import rclpy
from rclpy.node import Node

from std_msgs.msg import String

from .util import parse_topic_and_type

class Collector(Node):

    def __init__(self):
        super().__init__('Collector')
        topic_and_types = parse_topic_and_type( self.get_topic_names_and_types())
        subscriptions=[]
        for topic , msg_types in topic_and_types.items():
            print(topic)
            for msg_type in msg_types:
                try:
                    subscriptions.append(
                    self.create_subscription(
                        String,   # message type
                        topic,      # topic name
                        self.listener_callback,
                        10))
                except Exception as e:
                    print(e)
        # topic_map = self.get_topic_names_and_types()

        # self.subscription  # prevent unused variable warning
        print(subscriptions)

    def listener_callback(self, msg):
        self.get_logger().info(f"I heard : {msg}.")
        


def main(args=None):
    rclpy.init(args=args)

    collector = Collector()

    rclpy.spin(collector)
    

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    collector.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()