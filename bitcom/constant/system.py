BIT_COM_ALPHA = "https://alpha.bitexch.dev"


class RestApiDefine:
    Url = BIT_COM_ALPHA


class HttpMethod:
    GET_PUBLIC = "GET_PUBLIC"
    GET_PRIVATE = "GET_PRIVATE"
    POST_PUBLIC = "POST_PUBLIC"
    POST_PRIVATE = "POST_PRIVATE"


def get_default_server_url(user_configured_url):
    if user_configured_url and len(user_configured_url):
        return user_configured_url
    else:
        return RestApiDefine.Url
