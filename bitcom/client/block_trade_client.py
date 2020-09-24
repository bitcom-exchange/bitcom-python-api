class BlockTradeClient(object):

    def __init__(self, **kwargs):
        self.__kwargs = kwargs

    def place_new_block_trade_order(self, param_map=None):
        if param_map is None:
            param_map = {}
        from bitcom.service.block_trade.place_block_trade_order import PlaceNewBlockTradeOrderService
        return PlaceNewBlockTradeOrderService(param_map).request(**self.__kwargs)

    def query_block_trades(self, param_map=None):
        if param_map is None:
            param_map = {}
        from bitcom.service.block_trade.query_block_trades import QueryBlockTradesService
        return QueryBlockTradesService(param_map).request(**self.__kwargs)

    def query_block_trades_by_platform(self, param_map=None):
        if param_map is None:
            param_map = {}
        from bitcom.service.block_trade.query_block_trades_by_platform import QueryBlockTradesByPlatformService
        return QueryBlockTradesByPlatformService(param_map).request(**self.__kwargs)