import json
import os
import sys

import requests
from src.comm.comm.util import *
sys.path.append(os.path.join(os.path.dirname(__file__),"..","comm"))
from util import *

def test_send_data():
    body = "send topic data: "
    resp = post_to_content(body)
    assert resp.ok
