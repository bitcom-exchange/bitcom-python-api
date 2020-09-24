from bitcom.connection.restapi_sync_client import RestApiSyncClient
from bitcom.constant import HttpMethod


class GetWsAuthToken:

    def __init__(self, params):
        self.params = params

    def request(self, **kwargs):
        channel = "/v1/ws/auth"

        return RestApiSyncClient(**kwargs).request_process(HttpMethod.GET_PRIVATE, channel, self.params)