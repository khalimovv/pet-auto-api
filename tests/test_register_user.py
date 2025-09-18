import allure
from lib.http_methods import HttpClient
from lib.logger import Logger


@allure.suite("User API")
@allure.feature("Регистрация пользователя")
@allure.story("Успешная регистрация при корректных данных")
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("smoke", "regression", "api")
class TestRegisterUser:

    @allure.title("Проверка регистрации юзера при отправке POST запроса")
    def test_register_user(self):
        with allure.step("Отправляем POST запрос на /register с валидными данными"):
            register_user = HttpClient.post(
                "/register",
                json={
                    "email": "eve.holt@reqres.in",
                    "password": "pistol"
                }
            )
            Logger.log_response(register_user)

        with allure.step("Проверяем статус код ответа"):
            get_status_code = register_user.status_code
            allure.attach(str(get_status_code), "HTTP Status Code", allure.attachment_type.TEXT)
            assert get_status_code == 200, f"Ожидали 200, получили {get_status_code}"

        with allure.step("Проверяем тело ответа"):
            get_response = register_user.json()
            allure.attach(str(get_response), "Response JSON", allure.attachment_type.JSON)
            assert get_response is not None, "Пустой ответ от сервера"

        with allure.step("Выводим информацию в консоль (для отладки)"):
            print(f"Роут: {register_user.url}")
            print(f"Статус код от сервера: {get_status_code}")
            print(f"Тело ответа: {get_response}")
