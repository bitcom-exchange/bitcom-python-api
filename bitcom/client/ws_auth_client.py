class WsAuthClient(object):

    def __init__(self, **kwargs):
        self.__kwargs = kwargs

    def get_ws_auth_token(self):
        from bitcom.service.ws.ws_auth import GetWsAuthToken
        return GetWsAuthToken({}).request(**self.__kwargs)
    #
    # def subscribe(self, param_map, callback, error_handler):
    #
    #     from bitcom.service.ws.ws_subscribe import SubscribeService
    #     SubscribeService(param_map).subscribe(callback, error_handler, **self.__kwargs)