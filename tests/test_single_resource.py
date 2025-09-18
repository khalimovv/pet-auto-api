import allure
from lib.http_methods import HttpClient
from lib.logger import Logger


@allure.suite("Resources API")
@allure.feature("Получение ресурса")
@allure.story("Проверка существования ресурса")
@allure.severity(allure.severity_level.NORMAL)
@allure.tag("regression", "api", "get")
class TestSingleResource:

    @allure.title("Проверка существования ресурса при отправке GET запроса")
    def test_get_single_resource(self):
        with allure.step("Отправляем GET запрос на /unknown/2"):
            send_single_resource_request = HttpClient.get("/unknown/2")
            Logger.log_response(send_single_resource_request)
            allure.attach(send_single_resource_request.url, "Request URL", allure.attachment_type.TEXT)

        with allure.step("Проверяем статус код ответа"):
            get_response_status_code = send_single_resource_request.status_code
            allure.attach(str(get_response_status_code), "HTTP Status Code", allure.attachment_type.TEXT)
            assert get_response_status_code == 200, (
                f"Ожидаемый статус код: 200. Фактический статус код: {get_response_status_code}"
            )

        with allure.step("Проверяем тело ответа"):
            get_single_resource_json = send_single_resource_request.json()
            allure.attach(str(get_single_resource_json), "Response JSON", allure.attachment_type.JSON)
            assert get_single_resource_json is not None, "Пустой ответ от сервера"

        with allure.step("Выводим информацию в консоль (для отладки)"):
            print(f"Роут: {send_single_resource_request.url}")
            print(f"Статус код от сервера: {get_response_status_code}")
            print(f"Тело ответа: {get_single_resource_json}")
