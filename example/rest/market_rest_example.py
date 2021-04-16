from bitcom.client.market_client import MarketClient
from bitcom.utils import *
from bitcom.constant import *

market_client = MarketClient(url=USER1_HOST, access_key=USER1_ACCESS_KEY, secret_key=USER1_SECRET_KEY)

index_response = market_client.get_index()
LogInfo.output("Get index price: ", index_response)

param_map = {
    'currency': 'BTC',
    'category': 'future'
}
instruments_response = market_client.get_instruments(param_map)
LogInfo.output("Get instruments: ", instruments_response)

param_map = {
    'instrument_id': 'BTC-PERPETUAL',
}
tickers_response = market_client.get_tickers(param_map)
LogInfo.output("Get tickers: ", tickers_response)

param_map = {
    'instrument_id': 'BTC-PERPETUAL',
    'level': 5,
}
orderbook_response = market_client.get_orderbooks(param_map)
LogInfo.output("Get orderbooks: ", orderbook_response)

param_map = {
    'currency': 'BTC',
    'category': 'future',
    'instrument_id': 'BTC-PERPETUAL',
}
market_trade_response = market_client.get_market_trades(param_map)
LogInfo.output("Get market trades: ", market_trade_response)

param_map = {
    'instrument_id': 'BTC-PERPETUAL',
    'start_time': '1600654079021',
    'end_time': '1600656132026',
    'timeframe_min': '1',

}
kline_response = market_client.get_klines(param_map)
LogInfo.output("Get klines: ", kline_response)

param_map = {
    'currency': 'BTC',
}
delivery_info_response = market_client.get_delivery_info(param_map)
LogInfo.output("Get delivery info: ", delivery_info_response)

param_map = {
    'currency': 'BTC',
    'instrument_id': 'BTC-PERPETUAL',
}
market_summary_response = market_client.get_market_summary(param_map)
LogInfo.output("Get market summary: ", market_summary_response)

param_map = {
    'instrument_id': 'BTC-PERPETUAL',
}
funding_rate_response = market_client.get_funding_rate(param_map)
LogInfo.output("Get funding rate: ", funding_rate_response)

param_map = {
    'instrument_id': 'BTC-PERPETUAL',
    'start_time': 1610784000000,
    'end_time': 1610870400000,
    'history_type': "8H",
}
response = market_client.get_funding_rate_history(param_map)
LogInfo.output("Get funding rate history: ", response)

response = market_client.get_total_volume()
LogInfo.output("Get total volume: ", response)

response = market_client.get_currencies()
LogInfo.output("Get currencies: ", response)
