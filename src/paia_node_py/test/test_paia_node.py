import rclpy
from paia_node_py.node import SimplePublishNode
def test_simple_publish():
    rclpy.init()
    node = SimplePublishNode(topic="test_topic")
    assert "hello world" == node.prepare_msg().data

