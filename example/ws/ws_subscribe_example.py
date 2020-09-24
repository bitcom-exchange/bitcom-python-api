import json
import time

from bitcom.client.subscribe_client import SubscribeClient
from bitcom.constant import *


def on_wss_open(ws):
    cmd = """{"type": "subscribe", "instruments": ["BTC-PERPETUAL"],
     "channels": ["depth1"], "interval": "raw", "token": "13c8df77-038d-451b-9460-7de6c271efd8"}"""

    # check json
    obj = json.loads(cmd)

    print('send subscribe cmd: ' + cmd)
    ws.send(cmd)


def on_wss_msg(ws, data):
    print(data)


# Example
channel = SubscribeClient(WS_HOST, on_wss_open, on_wss_msg)
channel.start()

time.sleep(3)
