class SystemClient(object):

    def __init__(self, **kwargs):
        self.__kwargs = kwargs

    def get_system_timestamp(self, param_map=None):
        if param_map is None:
            param_map = {}
        from bitcom.service.system.get_system_timestamp import GetSystemTimestampService
        return GetSystemTimestampService(param_map).request(**self.__kwargs)

    def get_system_version(self):
        from bitcom.service.system.get_system_version import GetSystemVersionService
        return GetSystemVersionService({}).request(**self.__kwargs)

    def get_system_cod_status(self, param_map=None):
        if param_map is None:
            param_map = {}
        from bitcom.service.system.get_system_cod_status import GetSystemCodStatusService
        return GetSystemCodStatusService(param_map).request(**self.__kwargs)
