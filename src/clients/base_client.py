from dataclasses import dataclass

import requests


@dataclass
class Response:
    status_code: int
    text: str
    as_dict: object
    headers: dict
    ok: bool


class HttpRequestHandler:

    def get(self, url, headers):
        response = requests.get(url, headers = headers)
        return self.__get_responses(response)

    def post(self, url, payload, headers):
        response = requests.post(url, data=payload, headers=headers)
        return self.__get_responses(response)

    def delete(self, url, headers):
        response = requests.delete(url, headers=headers)
        return self.__get_responses(response)

    def __get_responses(self, response):
        status_code = response.status_code
        text = response.text

        try:
            as_dict = response.json()
        except:
            as_dict = {}

        headers = response.headers

        return Response(
            status_code, text, as_dict, headers, response.ok
        )


class BaseClient(HttpRequestHandler):

    def __init__(self, headers: {} = None):
        if headers is not None:
            self.headers = headers
        else:
            self.headers = {
                "Content-Type": "application/json",
                "Accept": "application/json"
            }
        self.request = super()
