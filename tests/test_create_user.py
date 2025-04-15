import allure
from lib.http_methods import HttpClient
from lib.logger import Logger


class TestCreateUser:
    @allure.title("Проверка создания юзера при отправке пост запроса")
    def test_create_user(self):
        send_create_request_user = HttpClient.post(
            "/users",
            json={
                "name": "morpheus",
                "job": "leader"
            }
        )
        print(f"Роут: {send_create_request_user.url}")

        get_json = send_create_request_user.json()
        print(f"Тело ответа: {get_json}")

        Logger.log_response(send_create_request_user)


        get_status_code = send_create_request_user.status_code
        print(f"Статус код от сервера: {get_status_code}")

        assert get_status_code == 201, (
            f"Ожидаемый статус код: 201. Фактический статус код: {get_status_code}"
        )
        assert get_json is not None, "Пустой ответ от сервера"
