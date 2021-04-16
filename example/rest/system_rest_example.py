from bitcom.client.system_client import SystemClient
from bitcom.utils import *
from bitcom.constant import *

system_client = SystemClient(url=USER1_HOST, access_key=USER1_ACCESS_KEY, secret_key=USER1_SECRET_KEY)
timestamp_response = system_client.get_system_timestamp()
LogInfo.output("Get server timestamp: ", timestamp_response)

version_response = system_client.get_system_version()
LogInfo.output("Get API version: ", version_response)

cod_status_response = system_client.get_system_cod_status()
LogInfo.output("Get cancel-only status after system maintenance: ", cod_status_response)
