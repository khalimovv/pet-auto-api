import allure
from lib.http_methods import HttpClient
from lib.logger import Logger


@allure.suite("User API")
@allure.feature("Создание пользователя")
@allure.story("Успешное создание пользователя")
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("api", "post", "regression", "smoke")
class TestCreateUser:

    @allure.title("Проверка создания пользователя при отправке POST запроса")
    def test_create_user(self):
        with allure.step("Отправляем POST запрос на /users с данными пользователя"):
            send_create_request_user = HttpClient.post(
                "/users",
                json={
                    "name": "morpheus",
                    "job": "leader"
                }
            )
            Logger.log_response(send_create_request_user)
            allure.attach(send_create_request_user.url, "Request URL", allure.attachment_type.TEXT)

        with allure.step("Проверяем статус код ответа"):
            get_status_code = send_create_request_user.status_code
            allure.attach(str(get_status_code), "HTTP Status Code", allure.attachment_type.TEXT)
            assert get_status_code == 201, (
                f"Ожидаемый статус код: 201. Фактический статус код: {get_status_code}"
            )

        with allure.step("Проверяем тело ответа"):
            get_json = send_create_request_user.json()
            allure.attach(str(get_json), "Response JSON", allure.attachment_type.JSON)
            assert get_json is not None, "Пустой ответ от сервера"

        with allure.step("Выводим информацию в консоль (для отладки)"):
            print(f"Роут: {send_create_request_user.url}")
            print(f"Статус код от сервера: {get_status_code}")
            print(f"Тело ответа: {get_json}")
