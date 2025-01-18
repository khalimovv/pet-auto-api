import requests

class HttpMethods:
    @staticmethod
    def post(url: str, json: dict = None, headers: dict = None, files: dict = None):
        return HttpMethods._send(url, json, headers, 'POST', files)

    @staticmethod
    def get(url: str, data: dict = None, headers: dict = None,):
        return HttpMethods._send(url, data, headers)

