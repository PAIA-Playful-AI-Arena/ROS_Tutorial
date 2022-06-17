import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from .node import SimplePublishNode
from .config import publisher_setting

class CountPublisher(SimplePublishNode):
    def __init__(self):
        super().__init__(topic=publisher_setting.topic_name,MSG_TYPE=String,timer_period=publisher_setting.time_period)
        self.i =0
    def prepare_msg(self):
        msg = String()
        msg.data = f'Hello Count: {self.i}'
        self.i+=1
        self.get_logger().info('Publishing: "%s"' % msg.data)
        return msg

def main(args=None):
    rclpy.init(args=args)

    publisher = CountPublisher()

    rclpy.spin(publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
