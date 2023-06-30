from typing import Dict

import requests


def _make_response(method: str, url: str, headers: Dict, params: Dict, timeout: int, success=200):
    response = requests.request(
        method,
        url,
        headers=headers,
        params=params,
        timeout=timeout
    )

    status_code = response.status_code
    if status_code == success:
        return response
    return status_code


def _get_current_weather(method: str, url: str, headers: Dict, params: Dict, format_weather: str = 'current',
                         timeout: int = 10, success=200, func=_make_response):
    url = '{0}/{1}.json'.format(url, format_weather)
    response = func(method, url, headers=headers, params=params, timeout=timeout)
    return response


def _get_history_weather(method: str, url: str, headers: Dict, params: Dict, format_weather: str = 'history',
                         timeout: int = 10, success=200, func=_make_response):
    url = '{0}/{1}.json'.format(url, format_weather)
    response = func(method, url, headers=headers, params=params, timeout=timeout)
    return response


class SiteApiInterface:

    @staticmethod
    def get_curr_weather():
        return _get_current_weather

    @staticmethod
    def get_history_weather():
        return _get_history_weather


if __name__ == '__main__':
    _make_response()
    _get_history_weather()
    _get_current_weather()

    SiteApiInterface()
