import rclpy
from rclpy.node import Node
from std_msgs.msg import String

# from .BasicPublishNode import SimplePublishNode
class SimplePublishNode(Node):

    def __init__(self,topic:str,MSG_TYPE=String,timer_period:float=1.0):
        super().__init__('SimplePublishNode')
        self.publisher_ = self.create_publisher(MSG_TYPE, topic, 10)
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = String()
        msg.data = 'Hello World: %d' % self.i
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
        self.i += 1

def main(args=None):
    rclpy.init(args=args)

    publisher = SimplePublishNode(topic="paia_pub",timer_period=0.5)

    rclpy.spin(publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
