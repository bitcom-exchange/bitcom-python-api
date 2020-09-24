class AccountClient(object):

    def __init__(self, **kwargs):
        self.__kwargs = kwargs

    def get_accounts(self, param_map=None):
        if param_map is None:
            param_map = {}
        from bitcom.service.account.get_accounts import GetAccountsService
        return GetAccountsService(param_map).request(**self.__kwargs)

    def get_user_positions(self, param_map=None):
        if param_map is None:
            param_map = {}
        from bitcom.service.account.get_user_positions import GetUserPositionsService
        return GetUserPositionsService(param_map).request(**self.__kwargs)

    def get_user_transaction_logs(self, param_map=None):
        if param_map is None:
            param_map = {}
        from bitcom.service.account.get_user_transaction_logs import GetTransactionLogsService
        return GetTransactionLogsService(param_map).request(**self.__kwargs)

    def get_user_deliveries(self, param_map=None):
        if param_map is None:
            param_map = {}
        from bitcom.service.account.get_user_deliveries import GetUserDeliveriesService
        return GetUserDeliveriesService(param_map).request(**self.__kwargs)

    def get_user_settlements(self, param_map=None):
        if param_map is None:
            param_map = {}
        from bitcom.service.account.get_user_settlements import GetUserSettlementsService
        return GetUserSettlementsService(param_map).request(**self.__kwargs)

    def config_cod(self, param_map=None):
        if param_map is None:
            param_map = {}
        from bitcom.service.account.config_cod import ConfigCodService
        return ConfigCodService(param_map).request(**self.__kwargs)

    def get_cod_config(self, param_map=None):
        if param_map is None:
            param_map = {}
        from bitcom.service.account.get_cod_config import GetCodConfigService
        return GetCodConfigService(param_map).request(**self.__kwargs)

    def get_mmp_state(self, param_map=None):
        if param_map is None:
            param_map = {}
        from bitcom.service.account.get_mmp_state import GetMMPStateService
        return GetMMPStateService(param_map).request(**self.__kwargs)

    def update_mmp_config(self, param_map=None):
        if param_map is None:
            param_map = {}
        from bitcom.service.account.update_mmp_config import UpdateMMPConfigService
        return UpdateMMPConfigService(param_map).request(**self.__kwargs)

    def reset_mmp_state(self, param_map=None):
        if param_map is None:
            param_map = {}
        from bitcom.service.account.reset_mmp_state import ResetMMPStateService
        return ResetMMPStateService(param_map).request(**self.__kwargs)