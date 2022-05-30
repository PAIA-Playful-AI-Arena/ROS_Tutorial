# from comm.util import *
import os.path
import sys

from src.comm.comm.util import parse_topic_and_type
sys.path.append(os.path.join(os.path.dirname(__file__),"..","comm"))
from util import *
def test_parse_topic_and_msg():
    topic_names_and_types = [('/parameter_events', ['rcl_interfaces/msg/ParameterEvent']),
                             ('/rosout', ['rcl_interfaces/msg/Log']),
                             ('/topic', ['std_msgs/msg/String'])
                             ]

    # print()
    result = parse_topic_and_type(topic_names_and_types)
    # print(result)
    assert "parameter_events" in result
    assert "rosout" in result
    assert "topic" in result
    for topic , msg_types in result.items():
        print(topic)
        for msg_type in msg_types:
            print(msg_type)

