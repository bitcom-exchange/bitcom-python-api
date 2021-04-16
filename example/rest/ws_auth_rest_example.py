from bitcom.client.ws_auth_client import WsAuthClient
from bitcom.utils import *
from bitcom.constant import *

ws_client = WsAuthClient(url=USER1_HOST, access_key=USER1_ACCESS_KEY, secret_key=USER1_SECRET_KEY)

token_response = ws_client.get_ws_auth_token()
LogInfo.output("Get websocket token: ", token_response)
