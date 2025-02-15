from lib.http_methods import HttpClient
import allure

class TestRegisterUser:
    @allure.title("Проверка регистрации юзера при отправке пост запроса")
    def test_register_user(self):
        register_user = HttpClient.post("/register",
            json={
                "email": "eve.holt@reqres.in",
                "password": "pistol"
            }
        )
        print(f"Роут: {register_user.url}")

        get_response = register_user.json()
        print(f"Тело ответа:{get_response}")

        get_status_code = register_user.status_code
        print(f"Статус код от сервера: {get_status_code}")

        assert get_status_code == 200, (
            f"Ожидаемый статус код: 200. Фактический статус код: {get_status_code}"
        )
        assert get_response is not None, "Пустой ответ от сервера"
