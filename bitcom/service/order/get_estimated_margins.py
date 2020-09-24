from bitcom.connection.restapi_sync_client import RestApiSyncClient
from bitcom.constant import HttpMethod


class GetEstimatedMarginsService:

    def __init__(self, params):
        self.params = params

    def request(self, **kwargs):
        channel = "/v1/margins"

        return RestApiSyncClient(**kwargs).request_process(HttpMethod.GET_PRIVATE, channel, self.params)