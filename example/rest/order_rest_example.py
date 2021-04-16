from bitcom.client.order_client import OrderClient
from bitcom.utils import *
from bitcom.constant import *

order_client = OrderClient(url=USER1_HOST, access_key=USER1_ACCESS_KEY, secret_key=USER1_SECRET_KEY)

param_map = {
    'instrument_id': 'BTC-PERPETUAL',
    'qty': '1000',
    'side': 'buy',
    'price': '11000.50',
    'order_type': 'limit',
    'time_in_force': 'gtc',
}
new_order_response = order_client.place_new_order(param_map)
LogInfo.output("Place new order: ", new_order_response)


param_map = {
    "currency": "ETH",
    "orders_data": [
        {"instrument_id": "ETH-PERPETUAL", "price": "2000", "qty": "100", "side": "buy"},
        {"instrument_id": "ETH-PERPETUAL", "price": "2000", "qty": "100", "side": "sell"}
    ]
}

place_batch_orders_response = order_client.place_batch_orders(param_map)
LogInfo.output("Place batch orders: ", place_batch_orders_response)
