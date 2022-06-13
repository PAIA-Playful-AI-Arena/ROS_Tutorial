
from rclpy.node import Node
from std_msgs.msg import String
import abc

class SimplePublishNode(Node):

    def __init__(self, topic: str, MSG_TYPE=String, timer_period: float = 1.0):
        super().__init__('SimplePublishNode')
        self._publisher = self.create_publisher(MSG_TYPE, topic, 10)
        self._timer = self.create_timer(timer_period, self.__timer_callback)

    def __timer_callback(self):
        msg = self.prepare_msg()
        self._publisher.publish(msg)

    @abc.abstractmethod
    def prepare_msg(self):

        msg = String()
        msg.data = 'hello world'
        self.get_logger().info('Publishing: "%s"' % msg.data)
        return msg
class SimpleSubscribeNode(Node):

    def __init__(self, topic: str, MSG_TYPE=String, timer_period: float = 1.0):
        super().__init__('SimplePublishNode')

        self.subscription = self.create_subscription(
            MSG_TYPE,
            topic,
            self.handle_msg,
            10)
        self.subscription  # prevent unused variable warning

    @abc.abstractmethod
    def handle_msg(self, msg):
        self.get_logger().info('I heard: "%s"' % msg.data)

    