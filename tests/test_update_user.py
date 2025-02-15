from lib.http_methods import HttpClient
import allure

class TestUpdateUser:
    @allure.title("Проверка обновления данных юзера при отправке пут запроса")
    def test_update_user_info(self):
        update_user_request = HttpClient.put("/users/2",
                json={
                "name": "morpheus",
                "job": "zion resident"
            }
        )
        print(f"Роут: {update_user_request.url}")

        get_response = update_user_request.json()
        print(f"Тело ответа:{get_response}")

        get_status_code = update_user_request.status_code
        print(f"Статус код от сервера: {get_status_code}")

        assert get_status_code == 200, (
            f"Ожидаемый статус код: 200. Фактический статус код: {get_status_code}"
        )
        assert get_response is not None, "Пустой ответ от сервера"
