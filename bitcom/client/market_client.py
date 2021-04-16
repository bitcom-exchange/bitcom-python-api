class MarketClient(object):

    def __init__(self, **kwargs):
        self.__kwargs = kwargs

    def get_index(self, param_map=None):
        if param_map is None:
            param_map = {}
        from bitcom.service.market.get_index import GetIndexPriceService
        return GetIndexPriceService(param_map).request(**self.__kwargs)

    def get_instruments(self, param_map=None):
        if param_map is None:
            param_map = {}
        from bitcom.service.market.get_instruments import GetInstrumentsService
        return GetInstrumentsService(param_map).request(**self.__kwargs)

    def get_tickers(self, param_map=None):
        if param_map is None:
            param_map = {}
        from bitcom.service.market.get_tickers import GetTickersService
        return GetTickersService(param_map).request(**self.__kwargs)

    def get_orderbooks(self, param_map=None):
        if param_map is None:
            param_map = {}
        from bitcom.service.market.get_orderbooks import GetOrderBooksService
        return GetOrderBooksService(param_map).request(**self.__kwargs)

    def get_market_trades(self, param_map=None):
        if param_map is None:
            param_map = {}
        from bitcom.service.market.get_market_trades import GetMarketTradesService
        return GetMarketTradesService(param_map).request(**self.__kwargs)

    def get_klines(self, param_map=None):
        if param_map is None:
            param_map = {}
        from bitcom.service.market.get_klines import GetKlinesService
        return GetKlinesService(param_map).request(**self.__kwargs)

    def get_delivery_info(self, param_map=None):
        if param_map is None:
            param_map = {}
        from bitcom.service.market.get_delivery_info import GetDeliveryInfoService
        return GetDeliveryInfoService(param_map).request(**self.__kwargs)

    def get_market_summary(self, param_map=None):
        if param_map is None:
            param_map = {}
        from bitcom.service.market.get_market_summary import GetMarketSummaryService
        return GetMarketSummaryService(param_map).request(**self.__kwargs)

    def get_funding_rate(self, param_map=None):
        if param_map is None:
            param_map = {}
        from bitcom.service.market.get_funding_rate import GetFundingRateService
        return GetFundingRateService(param_map).request(**self.__kwargs)

    def get_funding_rate_history(self, param_map=None):
        if param_map is None:
            param_map = {}
        from bitcom.service.market.get_funding_rate_history import GetFundingRateHistoryService
        return GetFundingRateHistoryService(param_map).request(**self.__kwargs)

    def get_total_volume(self, param_map=None):
        if param_map is None:
            param_map = {}
        from bitcom.service.market.get_total_volume import GetTotalVolumeService
        return GetTotalVolumeService(param_map).request(**self.__kwargs)

    def get_currencies(self, param_map=None):
        if param_map is None:
            param_map = {}
        from bitcom.service.market.get_currencies import GetCurrenciesService
        return GetCurrenciesService(param_map).request(**self.__kwargs)
