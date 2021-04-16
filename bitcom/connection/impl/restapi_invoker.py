import json
import requests

session = requests.Session()


def check_response(response):
    code = response.status_code


def call_sync(request, is_checked=False):
    if request.method == "GET":
        response = session.get(request.host + request.url, headers=request.header)
        if is_checked is True:
            return response.text
        try:
            dict_data = json.loads(response.text, encoding="utf-8")
        except Exception as ex:
            print("recv error: ", response.text, "\nexception: ", ex)
            return
        return dict_data

    elif request.method == "POST":
        response = session.post(request.host + request.url, data=json.dumps(request.post_body), headers=request.header)
        try:
            dict_data = json.loads(response.text, encoding="utf-8")
        except Exception as ex:
            print("recv error: ", response.text, "\nexception: ", ex)
            return
        return dict_data
