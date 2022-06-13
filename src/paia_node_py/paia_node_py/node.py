
from urllib import response
from rclpy.node import Node
from std_msgs.msg import String
from std_srvs.srv import SetBool
import abc
import rclpy

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

class SimpleServiceNode(Node):

    def __init__(self,service_name:str,SRV_TYPE=SetBool):
        super().__init__('SimpleServiceNode')
        self.srv = self.create_service(SRV_TYPE, service_name, self.get_response)

    @abc.abstractmethod
    def get_response(self, request, response):
        self.get_logger().info(f'Receive request: "{request.data}"' )
        response.success = True
        response.message = "Thanks for you request."
        return response


class SimpleClientNode(Node):

    def __init__(self,service_name:str,SRV_TYPE=SetBool):
        super().__init__('SimpleClientNode')
        self.cli = self.create_client(SRV_TYPE, service_name)
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.req = SRV_TYPE.Request()
        self.trig = False

    def prepare_request(self):
        self.req.data = self.trig
        self.trig = not self.trig
        self.future = self.cli.call_async(self.req)
        # TODO think more
    def handle_response(self,response):
        self.get_logger().info(
                        f'receive response: {response.message} ')

    def send_request(self):
        # check client
        # return response 
        self.prepare_request()
        while rclpy.ok():
            rclpy.spin_once(self)
            if self.future.done():
                try:
                    response = self.future.result()
                except Exception as e:
                    self.get_logger().info(
                        'Service call failed %r' % (e,))
                else:
                    self.handle_response(response)
                # self.prepare_request()
                break
