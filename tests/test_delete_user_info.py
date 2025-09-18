import allure
from lib.http_methods import HttpClient
from lib.logger import Logger


@allure.suite("User API")
@allure.feature("Удаление пользователя")
@allure.story("Успешное удаление существующего пользователя")
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("regression", "api", "delete")
class TestDeleteUserInfo:

    @allure.title("Проверка удаления юзера при отправке DELETE запроса")
    def test_delete_user_info(self):
        with allure.step("Отправляем DELETE запрос на /users/2"):
            delete_user_info_request = HttpClient.delete("/users/2")
            Logger.log_response(delete_user_info_request)
            allure.attach(delete_user_info_request.url, "Request URL", allure.attachment_type.TEXT)

        with allure.step("Проверяем статус код ответа"):
            get_status_code = delete_user_info_request.status_code
            allure.attach(str(get_status_code), "HTTP Status Code", allure.attachment_type.TEXT)
            assert get_status_code == 204, (
                f"Ожидаемый статус код: 204. Фактический статус код: {get_status_code}"
            )

        with allure.step("Выводим информацию в консоль (для отладки)"):
            print(f"Роут: {delete_user_info_request.url}")
            print(f"Статус код от сервера: {get_status_code}")
