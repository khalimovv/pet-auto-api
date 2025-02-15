from lib.http_methods import HttpClient
import allure

class TestDeleteUserInfo:
    @allure.title("Проверка удаления юзера при отправке делит запроса")
    def test_delete_user_info(self):
        delete_user_info_request = HttpClient.delete("/users/2")
        print(f"Роут: {delete_user_info_request.url}")

        get_status_code = delete_user_info_request.status_code
        print(f"Статус код от сервера: {get_status_code}")

        assert get_status_code == 204, (
            f"Ожидаемый статус код: 204. Фактический статус код: {get_status_code}"
        )
