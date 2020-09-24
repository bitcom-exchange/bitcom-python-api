class OrderClient(object):

    def __init__(self, **kwargs):
        self.__kwargs = kwargs

    def place_new_order(self, param_map=None):
        if param_map is None:
            param_map = {}
        from bitcom.service.order.place_new_order import PlaceNewOrderService
        return PlaceNewOrderService(param_map).request(**self.__kwargs)

    def place_batch_orders(self, param_map=None):
        if param_map is None:
            param_map = {}
        from bitcom.service.order.place_batch_orders import PlaceBatchOrdersService
        return PlaceBatchOrdersService(param_map).request(**self.__kwargs)

    def cancel_orders(self, param_map=None):
        if param_map is None:
            param_map = {}
        from bitcom.service.order.cancel_orders import CancelOrdersService
        return CancelOrdersService(param_map).request(**self.__kwargs)

    def amend_orders(self, param_map=None):
        if param_map is None:
            param_map = {}
        from bitcom.service.order.amend_orders import AmendOrdersService
        return AmendOrdersService(param_map).request(**self.__kwargs)

    def amend_batch_orders(self, param_map=None):
        if param_map is None:
            param_map = {}
        from bitcom.service.order.amend_batch_orders import AmendBatchOrdersService
        return AmendBatchOrdersService(param_map).request(**self.__kwargs)

    def close_positions(self, param_map=None):
        if param_map is None:
            param_map = {}
        from bitcom.service.order.close_positions import ClosePositionsService
        return ClosePositionsService(param_map).request(**self.__kwargs)

    def get_open_orders(self, param_map=None):
        if param_map is None:
            param_map = {}
        from bitcom.service.order.get_open_orders import GetOpenOrdersService
        return GetOpenOrdersService(param_map).request(**self.__kwargs)

    def get_orders(self, param_map=None):
        if param_map is None:
            param_map = {}
        from bitcom.service.order.get_orders import GetOrdersService
        return GetOrdersService(param_map).request(**self.__kwargs)

    def get_stop_orders(self, param_map=None):
        if param_map is None:
            param_map = {}
        from bitcom.service.order.get_stop_orders import GetStopOrdersService
        return GetStopOrdersService(param_map).request(**self.__kwargs)

    def get_user_trades(self, param_map=None):
        if param_map is None:
            param_map = {}
        from bitcom.service.order.get_user_trades import GetUserTradesService
        return GetUserTradesService(param_map).request(**self.__kwargs)

    def get_estimated_margins(self, param_map=None):
        if param_map is None:
            param_map = {}
        from bitcom.service.order.get_estimated_margins import GetEstimatedMarginsService
        return GetEstimatedMarginsService(param_map).request(**self.__kwargs)