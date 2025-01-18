import requests



class TestGetSingleUser:
    def test_get_single_user(self):
        response = requests.get(url="https://reqres.in/api/users/2")
        print(f"Роут: {response.url}")

        get_response = response.json()
        print(f"Тело ответа:{get_response}")

        get_response_status_code = response.status_code
        print(f"Статус код от сервера: {get_response_status_code}")

        assert  response.status_code == 200, (f"Ожидаемый статус код: 200."
                                          f" Фактический статус код: {get_response_status_code}")

        assert get_response is not None, "Пустой ответ от сервера"



class TestSingleResource:
    def test_get_single_resource(self):
        send_single_resource_request = requests.get(url="https://reqres.in/api/unknown/2")
        print(f"Роут: {send_single_resource_request.url}")

        get_single_resource_json = send_single_resource_request.json()
        print(f"Тело ответа:{get_single_resource_json}")

        get_response_status_code = send_single_resource_request.status_code
        print(f"Статус код от сервера: {get_response_status_code}")



        assert get_response_status_code == 200, (f"Ожидаемый статус код: 200."
                                          f" Фактический статус код: {get_response_status_code}")

        assert get_single_resource_json is not None, "Пустой ответ от сервера"

class TestCreateUser:
    def test_create_user(self):
        send_create_request_user = requests.post(url='https://reqres.in/api/users',
                                                 json={
                                                     "name": "morpheus",
                                                     "job": "leader"
                                                 })
        print(f"Роут: {send_create_request_user.url}")

        get_json = send_create_request_user.json()
        print(f"Тело ответа:{get_json}")

        get_status_code = send_create_request_user.status_code
        print(f"Статус код от сервера: {get_status_code}")


        assert get_status_code == 201, (f"Ожидаемый статус код: 201. "
                                        f"Фактический статус код: {get_status_code}")

        assert get_json is not None, "Пустой ответ от сервера"


class TestUpdateUser:
    def test_update_user_info(self):
        update_user_request = requests.put(url='https://reqres.in/api/users/2',
                                           json={
                                               "name": "morpheus",
                                               "job": "zion resident"
                                           })
        print(f"Роут:{update_user_request.url}")

        get_response = update_user_request.json()
        print(f"Тело ответа:{get_response}")

        get_status_code = update_user_request.status_code
        print(f"Статус код от сервера: {get_status_code}")

        assert get_status_code == 200, (f"Ожидаемый статус код: 200. "
                                        f"Фактический статус код: {get_status_code}")

        assert get_response is not None, "Пустой ответ от сервера"



class TestDeleteUserInfo:
    def test_delete_user_info(self):

        delete_user_info_request = requests.delete(url="https://reqres.in/api/users/2")
        print(f"Роут: {delete_user_info_request.url}")


        get_status_code = delete_user_info_request.status_code
        print(f"Статус код от сервера: {get_status_code}")

        assert get_status_code == 204, (f"Ожидаемый статус код: 204. "
                                        f"Фактический статус код: {get_status_code}")


class TestRegisterUser:
    def test_register_user(self):
        register_user = requests.post(url="https://reqres.in/api/register", json={
            "email": "eve.holt@reqres.in",
            "password": "pistol"
        })
        print(f"Роут: {register_user.url}")


        get_response = register_user.json()
        print(f"Тело ответа:{get_response}")

        get_status_code = register_user.status_code
        print(f"Статус код от сервера: {get_status_code}")

        assert get_status_code == 200, (f"Ожидаемый статус код: 200. "
                                        f"Фактический статус код: {get_status_code}")

        assert get_response is not None, "Пустой ответ от сервера"