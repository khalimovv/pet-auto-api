"""
HTTP Methods Module
===================

Этот модуль предоставляет класс HttpClient для отправки HTTP-запросов (GET, POST, PUT, DELETE) к API,
используя базовый URL, определённый в конфигурационном файле. Все методы класса являются методами класса,
что позволяет использовать атрибут BASE_URL, определённый на уровне класса, для формирования полного URL.

Как работает:
--------------
1. BASE_URL импортируется из файла конфигурации (config/config.py) и присваивается атрибуту класса HttpClient.BASE_URL.
2. Методы get, post, put и delete формируют полный URL, объединяя BASE_URL и переданный путь (path).
3. Затем они вызывают соответствующую функцию из библиотеки requests с передачей дополнительных параметров (**kwargs),
   что позволяет гибко передавать заголовки, параметры запроса, данные в формате JSON и другие опции.
4. Каждый метод возвращает объект response, который содержит ответ от сервера.

Пример использования:
---------------------
Допустим, в файле конфигурации config/config.py у вас определён BASE_URL:
    BASE_URL = "https://reqres.in/api"

В тестах или в любом другом модуле вы можете сделать следующее:
    from lib.http_methods import HttpClient

    # Отправка GET запроса к "https://reqres.in/api/users/2"
    response = HttpClient.get("/users/2")

    # Отправка POST запроса с данными
    response = HttpClient.post("/users", json={"name": "morpheus", "job": "leader"})

Преимущества:
-------------
- Централизация базового URL: изменение BASE_URL в одном месте (файл конфигурации) автоматически затрагивает все запросы.
- Гибкость: использование **kwargs позволяет передавать любые дополнительные параметры запросов.
- Простота использования: методы HttpClient обеспечивают чистый и понятный интерфейс для отправки запросов.
"""

import requests
from config.config import BASE_URL

import requests
from config.config import BASE_URL

class HttpClient:
    BASE_URL = BASE_URL
    DEFAULT_HEADERS = {"x-api-key": "reqres-free-v1"}

    @classmethod
    def _request(cls, method, path, **kwargs):
        url = f"{cls.BASE_URL}{path}"
        kwargs["headers"] = {**cls.DEFAULT_HEADERS, **kwargs.get("headers", {})}
        return requests.request(method, url, **kwargs)

    @classmethod
    def get(cls, path, **kwargs):
        return cls._request("GET", path, **kwargs)

    @classmethod
    def post(cls, path, **kwargs):
        return cls._request("POST", path, **kwargs)

    @classmethod
    def put(cls, path, **kwargs):
        return cls._request("PUT", path, **kwargs)

    @classmethod
    def delete(cls, path, **kwargs):
        return cls._request("DELETE", path, **kwargs)
