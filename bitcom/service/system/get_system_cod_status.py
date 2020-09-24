from bitcom.connection.restapi_sync_client import RestApiSyncClient
from bitcom.constant import HttpMethod


class GetSystemCodStatusService:

    def __init__(self, params):
        self.params = params

    def request(self, **kwargs):
        channel = "/v1/system/cancel_only_status"

        return RestApiSyncClient(**kwargs).request_process(HttpMethod.GET_PRIVATE, channel, self.params)


