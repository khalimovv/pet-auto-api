import allure
from lib.http_methods import HttpClient
from lib.logger import Logger


@allure.suite("User API")
@allure.feature("Обновление пользователя")
@allure.story("Успешное обновление данных пользователя")
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("regression", "api", "put")
class TestUpdateUser:

    @allure.title("Проверка обновления данных юзера при отправке PUT запроса")
    def test_update_user_info(self):
        with allure.step("Отправляем PUT запрос на /users/2 с новыми данными"):
            update_user_request = HttpClient.put(
                "/users/2",
                json={
                    "name": "morpheus",
                    "job": "zion resident"
                }
            )
            Logger.log_response(update_user_request)
            allure.attach(update_user_request.url, "Request URL", allure.attachment_type.TEXT)

        with allure.step("Проверяем статус код ответа"):
            get_status_code = update_user_request.status_code
            allure.attach(str(get_status_code), "HTTP Status Code", allure.attachment_type.TEXT)
            assert get_status_code == 200, (
                f"Ожидаемый статус код: 200. Фактический статус код: {get_status_code}"
            )

        with allure.step("Проверяем тело ответа"):
            get_response = update_user_request.json()
            allure.attach(str(get_response), "Response JSON", allure.attachment_type.JSON)
            assert get_response is not None, "Пустой ответ от сервера"

        with allure.step("Выводим информацию в консоль (для отладки)"):
            print(f"Роут: {update_user_request.url}")
            print(f"Статус код от сервера: {get_status_code}")
            print(f"Тело ответа: {get_response}")
