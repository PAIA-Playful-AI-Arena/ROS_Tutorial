
from urllib import response
from rclpy.node import Node
from std_msgs.msg import String
from std_srvs.srv import SetBool
import abc
import rclpy

class SimplePublishNode(Node):

    def __init__(self, topic: str, MSG_TYPE=String, timer_period: float = 1.0):
        super().__init__(f'{topic}_publisher_node')
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
        super().__init__(f'{topic}_subscriber_node')

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
        super().__init__(f'{service_name}_service_node')
        self.srv = self.create_service(SRV_TYPE, service_name, self.get_response)

    @abc.abstractmethod
    def get_response(self, request, response):
        self.get_logger().info(f'Receive request: "{request.data}"' )
        response.success = True
        response.message = "Thanks for you request."
        return response


class SimpleClientNode(Node):

    def __init__(self,service_name:str,SRV_TYPE=SetBool):
        super().__init__(f'{service_name}_client_node')
        self._cli = self.create_client(SRV_TYPE, service_name)
        self.get_logger().info(f'{service_name}_client_node start...')

        while not self._cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.req = SRV_TYPE.Request()
        self.resp=SRV_TYPE.Response()

    
    def send_request_and_get_resp(self,request):
        # check client
        # return response 
        self.req = request
        self.get_logger().info(f'Send request : {self.req}')
        self.future = self._cli.call_async(self.req)
        while rclpy.ok():
            rclpy.spin_once(self)
            if self.future.done():
                try:
                    self.resp = self.future.result()
                except Exception as e:
                    self.get_logger().info(
                        'Service call failed %r' % (e,))
                break
        self.get_logger().info(f'Get response : {self.resp}')
        return self.resp
