import hashlib
import hmac
import time

from bitcom.connection.impl.restapi_invoker import call_sync
from bitcom.connection.impl.restapi_request import RestApiRequest
from bitcom.constant import *
from bitcom.exception.bitcom_api_exception import BitcomApiException
from bitcom.utils.url_params_builder import UrlParamsBuilder


def create_signature(__access_key, __secret_key, method, param, builder):
    pass


def get_timestamp():
    return str(int(round(time.time() * 1000)))


class RestApiSyncClient(object):

    def __init__(self, **kwargs):
        self.__access_key = kwargs.get("access_key", None)
        self.__secret_key = kwargs.get("secret_key", None)
        self.__server_url = kwargs.get("url", get_default_server_url(None))

    def __create_request_by_get(self, url, builder):
        request = RestApiRequest()
        request.method = "GET"
        request.host = self.__server_url
        request.header.update({'Content-Type': 'application/json'})
        request.url = url + builder.build_url()
        return request

    def __create_request_by_get_with_signature(self, url, builder):
        request = RestApiRequest()
        request.method = "GET"
        request.host = self.__server_url
        request.header.update({"Content-Type": "application/json"})
        request.header.update({"X-Bit-Access-Key": self.__access_key})
        sig = self.__get_signature(url, builder.param_map)
        builder.put_url("signature", sig)
        request.url = url + builder.build_url()
        return request

    def __create_request_by_post_with_signature(self, url, builder):
        request = RestApiRequest()
        request.method = "POST"
        request.host = self.__server_url
        sig = self.__get_signature(url, builder.post_map)
        builder.put_post("signature", sig)
        request.header.update({'Content-Type': 'application/json'})
        request.header.update({"X-Bit-Access-Key": self.__access_key})
        if len(builder.post_list):  # specify for case : /v1/order/batch-orders
            request.post_body = builder.post_list
        else:
            request.post_body = builder.post_map
        request.url = url + builder.build_url()
        return request

    def create_request(self, method, url, param_map):
        builder = UrlParamsBuilder()
        if method in [HttpMethod.GET_PUBLIC, HttpMethod.GET_PRIVATE]:
            for k, v in param_map.items():
                builder.put_url(k, v)
            builder.put_url("timestamp", get_timestamp())
        elif method in [HttpMethod.POST_PUBLIC, HttpMethod.POST_PRIVATE]:
            for k, v in param_map.items():
                builder.put_post(k, v)
            builder.put_post("timestamp", int(get_timestamp()))
        else:
            raise BitcomApiException(BitcomApiException.EXEC_ERROR,
                                     "[error] undefined HTTP method")

        if method == HttpMethod.GET_PUBLIC:
            request = self.__create_request_by_get(url, builder)
        elif method == HttpMethod.GET_PRIVATE:
            request = self.__create_request_by_get_with_signature(url, builder)
        elif method == HttpMethod.POST_PRIVATE:
            request = self.__create_request_by_post_with_signature(url, builder)
        elif method == HttpMethod.POST_PUBLIC:
            request = self.__create_request_by_post_with_signature(url, builder)
        else:
            raise BitcomApiException(BitcomApiException.INPUT_ERROR, "[Input] " + method + "  is invalid http method")

        return request

    def request_process(self, method, url, param_map):
        request = self.create_request(method, url, param_map)
        if request:
            return call_sync(request)

        return None

    def __encode_list(self, item_list):
        list_val = []
        for item in item_list:
            obj_val = self.__encode_object(item)
            list_val.append(obj_val)
        # list_val = sorted(list_val)
        output = '&'.join(list_val)
        output = '[' + output + ']'
        return output

    def __encode_object(self, param_map):
        sorted_keys = sorted(param_map.keys())
        ret_list = []
        for key in sorted_keys:
            val = param_map[key]
            if isinstance(val, list):
                list_val = self.__encode_list(val)
                ret_list.append(f'{key}={list_val}')
            elif isinstance(val, dict):
                # call encode_object recursively
                dict_val = self.__encode_object(val)
                ret_list.append(f'{key}={dict_val}')
            elif isinstance(val, bool):
                bool_val = str(val).lower()
                ret_list.append(f'{key}={bool_val}')
            else:
                general_val = str(val)
                ret_list.append(f'{key}={general_val}')

        sorted_list = sorted(ret_list)
        output = '&'.join(sorted_list)
        return output

    def __get_signature(self, api_path, param_map):
        str_to_sign = api_path + '&' + self.__encode_object(param_map)
        # print('str_to_sign = ' + str_to_sign)
        sig = hmac.new(self.__secret_key.encode('utf-8'), str_to_sign.encode('utf-8'),
                       digestmod=hashlib.sha256).hexdigest()
        return sig
