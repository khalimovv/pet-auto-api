from lib.http_methods import HttpClient
import allure

class TestSingleResource:
    @allure.title("Проверка существования ресурса при отправке гет запроса")
    def test_get_single_resource(self):
        send_single_resource_request = HttpClient.get("/unknown/2")
        print(f"Роут: {send_single_resource_request.url}")

        get_single_resource_json = send_single_resource_request.json()
        print(f"Тело ответа:{get_single_resource_json}")

        get_response_status_code = send_single_resource_request.status_code
        print(f"Статус код от сервера: {get_response_status_code}")

        assert get_response_status_code == 200, (
            f"Ожидаемый статус код: 200. Фактический статус код: {get_response_status_code}"
        )
        assert get_single_resource_json is not None, "Пустой ответ от сервера"
