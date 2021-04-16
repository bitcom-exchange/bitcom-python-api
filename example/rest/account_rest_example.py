from bitcom.client.account_client import AccountClient
from bitcom.utils import *
from bitcom.constant import *

account_client = AccountClient(url=USER1_HOST, access_key=USER1_ACCESS_KEY, secret_key=USER1_SECRET_KEY)

param_map = {
    'currency': 'BTC'
}
accounts_response = account_client.get_accounts(param_map)
LogInfo.output("Get accounts: ", accounts_response)

param_map = {
    'currency': 'BTC',
    'instrument_id': 'BTC-PERPETUAL'
}
positions_response = account_client.get_user_positions(param_map)
LogInfo.output("Get user positions: ", positions_response)

param_map = {
    'currency': 'BTC',
    'instrument_id': 'BTC-PERPETUAL',
    'offset': 1,
    'limit': 5
}
transactions_response = account_client.get_user_transaction_logs(param_map)
LogInfo.output("Get user transaction logs: ", transactions_response)

param_map = {
    'currency': 'BTC',
    'offset': 1,
    'limit': 5
}
user_settlements_response = account_client.get_user_deliveries(param_map)
LogInfo.output("Get user deliveries: ", user_settlements_response)

param_map = {
    'currency': 'BTC',
    'instrument_id': 'BTC-PERPETUAL',
    'offset': 1,
    'limit': 5
}
user_settlements_response = account_client.get_user_settlements(param_map)
LogInfo.output("Get user settlements: ", user_settlements_response)

param_map = {
    'currency': 'BTC',
    'cod': True,
}
config_cod_response = account_client.config_cod(param_map)
LogInfo.output("Enable cod: ", config_cod_response)

param_map = {
    'currency': 'BTC',
}
get_cod_config = account_client.get_cod_config(param_map)
LogInfo.output("Get cod config: ", get_cod_config)

param_map = {
    'currency': 'BTC',
}
get_mmp_state = account_client.get_mmp_state(param_map)
LogInfo.output("Get mmp state: ", get_mmp_state)


param_map = {
    'currency': 'BTC',
    "window_ms": 20000,
    "frozen_period_ms": 30000,
    "qty_limit": "1000.00000000",
    "delta_limit": "1000.00000000"
}
update_mmp_response = account_client.update_mmp_config(param_map)
LogInfo.output("Update mmp configs: ", update_mmp_response)

param_map = {
    'currency': 'BTC',
}
reset_mmp_response = account_client.reset_mmp_state(param_map)
LogInfo.output("Reset mmp state: ", reset_mmp_response)
