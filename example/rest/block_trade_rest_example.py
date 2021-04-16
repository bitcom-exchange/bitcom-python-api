from bitcom.client.block_trade_client import BlockTradeClient
from bitcom.utils import *
from bitcom.constant import *

block_trade_client = BlockTradeClient(url=USER1_HOST, access_key=USER1_ACCESS_KEY, secret_key=USER1_SECRET_KEY)


param_map = {
    "currency": "ETH",
    'bt_source': 'paradigm',
    'label': 'uuid-3',
    'role': 'maker',
    'counterparty': '51140',
    'trades': [
        {
            'instrument_id': 'ETH-19SEP20-10875-C',
            'price': '0.025',
            'qty': '12',
            'side': 'sell'
        }
    ]
}

place_new_block_trade_order_response = block_trade_client.place_new_block_trade_order(param_map)
LogInfo.output("Place new block trade orders: ", place_new_block_trade_order_response)

param_map = {
    "currency": "ETH",
    'bt_source': 'paradigm',
    'label': 'uuid-3',
    'instrument_id': 'ETH-19SEP20-10875-C',
}

query_block_trades_response = block_trade_client.query_block_trades(param_map)
LogInfo.output("Query block trade orders: ", query_block_trades_response)

param_map = {
    "currency": "ETH",
    'bt_source': 'paradigm',
    'label': 'uuid-3',
    'instrument_id': 'ETH-19SEP20-10875-C',
}

query_block_trades_response = block_trade_client.query_block_trades_by_platform(param_map)
LogInfo.output("Query block trade orders by platform: ", query_block_trades_response)
