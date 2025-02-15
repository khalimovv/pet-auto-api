# lib/http_methods.py
import requests
from config.config import BASE_URL

class HttpClient:
    BASE_URL = BASE_URL

    @classmethod
    def get(cls, path: str, **kwargs):
        """Отправка GET запроса по указанному пути"""
        url = f"{cls.BASE_URL}{path}"
        response = requests.get(url, **kwargs)
        return response

    @classmethod
    def post(cls, path: str, **kwargs):
        """Отправка POST запроса по указанному пути"""
        url = f"{cls.BASE_URL}{path}"
        response = requests.post(url, **kwargs)
        return response

    @classmethod
    def put(cls, path: str, **kwargs):
        """Отправка PUT запроса по указанному пути"""
        url = f"{cls.BASE_URL}{path}"
        response = requests.put(url, **kwargs)
        return response

    @classmethod
    def delete(cls, path: str, **kwargs):
        """Отправка DELETE запроса по указанному пути"""
        url = f"{cls.BASE_URL}{path}"
        response = requests.delete(url, **kwargs)
        return response
