import allure
from lib.http_methods import HttpClient
from lib.logger import Logger


@allure.story("Проверка работоспособности API")
@allure.label("owner", "A.Khalimov")
@allure.title("Проверка CRUD операции на пользователе")
@allure.description("""
  В этом тесте проверяется работоспособность функциональности по CRUD-feature 
  с использованием валидных данных в запросе.
  Проверяется, что система корректно обрабатывает запрос и выводит соответствующую информацию в теле ответа
  и в базе данных.
""")
class TestGetSingleUser:
    @allure.title("Проверка существования юзера при отправке гет запроса")
    def test_get_single_user(self):
        response = HttpClient.get("/users/2")
        print(f"Роут: {response.url}")

        get_response = response.json()
        print(f"Тело ответа: {get_response}")

        Logger.log_response(response)


        get_response_status_code = response.status_code
        print(f"Статус код от сервера: {get_response_status_code}")

        assert response.status_code == 200, (
            f"Ожидаемый статус код: 200. Фактический статус код: {get_response_status_code}"
        )
        assert get_response is not None, "Пустой ответ от сервера"
