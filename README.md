# bitcom-python-api

**API Doc**  
https://www.bit.com/docs/en-us/#introduction

## Quick Start

**Prerequisite**

- Python3


**Install package**

```shell
pip3 install bitcom
```

**Host**

You can get the latest production/testnet hosts here, including REST API and WebSocket.

https://www.bit.com/docs/en-us/#api-hosts-production

**Rest public client example**

```python
from bitcom.client.market_client import MarketClient
from bitcom.utils import *
from bitcom.constant import *

market_client = MarketClient(url=USER1_HOST)


param_map = {
    'instrument_id': 'BTC-PERPETUAL',
}
funding_rate_response = market_client.get_funding_rate(param_map)
LogInfo.output("Get funding rate: ", funding_rate_response)
```

**Rest private client example**  

```python
from bitcom.client.order_client import OrderClient
order_client = OrderClient(url=USER1_HOST, access_key='<your-access-key>', secret_key='<your-secret-key>')

ret = order_client.place_new_order({
    'instrument_id': 'BTC-PERPETUAL',
    'qty': '1500',
    'side': 'buy',
    'order_type': 'market',
})
print(ret)
```

**Websocket subscribe example**

```python
from bitcom.client.ws_auth_client import WsAuthClient
from bitcom.client.subscribe_client import SubscribeClient
from bitcom.utils import *
from bitcom.constant import *
import json
import time


ws_client = WsAuthClient(url=USER1_HOST, access_key=USER1_ACCESS_KEY, secret_key=USER1_SECRET_KEY)

token_response = ws_client.get_ws_auth_token()
LogInfo.output("Get websocket token: ", token_response)

def on_wss_open(ws):
    cmd = """{"type": "subscribe", "instruments": ["BTC-PERPETUAL"],
     "channels": ["depth1"], "interval": "raw", "token": {your_token}}"""

    # check json
    obj = json.loads(cmd)

    print('send subscribe cmd: ' + cmd)
    ws.send(cmd)


def on_wss_msg(ws, data):
    print(data)


channel = SubscribeClient(WS_HOST, on_wss_open, on_wss_msg)
channel.start()

time.sleep(3)
```


