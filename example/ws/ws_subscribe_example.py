import json
import time

from bitcom.client.subscribe_client import SubscribeClient
from bitcom.constant import *


def on_wss_open(ws):
    cmd = {"type": "subscribe", "instruments": ["BTC-PERPETUAL"],
           "channels": ["ticker"], "interval": "raw", "token": "13c8df77-038d-451b-9460-7de6c271efd8"}

    # convert to string
    cmdStr = json.dumps(cmd)

    print('send subscribe cmd: ' + cmdStr)
    ws.send(cmdStr)


def on_wss_msg(ws, data):
    print(data)


# Example
channel = SubscribeClient(WS_HOST, on_wss_open, on_wss_msg)
channel.start()

time.sleep(3)
