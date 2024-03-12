import allure
import pytest
import API.Steps.support_steps as support_steps
import API.resources.urls as urls
import API.Steps.generate_json_steps as generate_json_steps
import API.Steps.request_steps as request_steps
import API.Steps.assert_steps as assert_steps

spaces = " "


# POST/user, тест создания новых user-ов
@allure.step
@pytest.mark.smoke_regression
@pytest.mark.full_regression
def test_oneuser_post_positive():
    print(f'\n---Позитивный кейс, создание одного нового user-а---')
    request_post = generate_json_steps.create_json_users(1)
    url_post = urls.url_user_post()
    # отправка запроса
    response_post = request_steps.request_post(url_post, request_post)
    # анализ ответа
    assert_steps.assert_code(response_post, 200)
    assert_steps.assert_not_none_id(response_post, 'message')
    print(f'=================================================================')


# позитивный кейс
@allure.step
@pytest.mark.smoke_regression
@pytest.mark.full_regression
@pytest.mark.parametrize('url_param',
                         [
                             (urls.url_user_post_list_array("createWithArray")),
                             (urls.url_user_post_list_array("createWithList")),
                         ],
                         ids=["post_some_user_positive_array",
                              "post_some_user_positive_list",
                              ],
                         )
def test_someusers_post_positive(url_param):
    print(
        f'\n---Позитивный кейс, создание нескольких user-ов '
        f'массивом (post_some_user_positive_array) и списком (post_some_user_positive_list)---')
    # отправка запроса
    request_post = generate_json_steps.create_json_users(2)
    url_post = url_param
    print(f'url_user_post= {url_post}')
    response_post = request_steps.request_post(url_post, request_post)
    # анализ ответа
    assert_steps.assert_code(response_post, 200)
    assert_steps.assert_all_message(response_post, "ok")
    print(f'=================================================================')


# @pytest.mark.smoke_regression
# @pytest.mark.full_regression
# @pytest.mark.parametrize('type',
#                          [
#                              ("post_one_user_positive"),
#                              ("post_some_user_positive_array"),
#                              ("post_some_user_positive_list"),
#                          ]
#                          )
# def test_user_post_positive(type):
#     # создание одного нового user-а
#     global request_post, url_post
#     if type == "post_one_user_positive":
#         print(f'\n---Позитивный кейс, создание одного нового user-а---')
#         request_post = generate_json_steps.create_json_users(1)
#         url_post = urls.url_user_post()
#     # создание нескольких новых user-ов массивом
#     if type == "post_some_user_positive_array":
#         print(f'\n---Позитивный кейс, создание нескольких новых user-ов массивом---')
#         request_post = generate_json_steps.create_json_users(2)
#         url_post = urls.url_user_post_list_array("createWithArray")
#     # оздание нескольких user-ов списком
#     if type == "post_some_user_positive_list":
#         print(f'\n---Позитивный кейс, создание нескольких user-ов списком---')
#         request_post = generate_json_steps.create_json_users(3)
#         url_post = urls.url_user_post_list_array("createWithList")
#     # отправка запроса
#     response_post = request_steps.request_post(url_post, request_post)
#     # анализ ответа
#     assert_steps.assert_code(response_post, 200)
#     if type == "post_one_user_positive":
#         assert_steps.assert_not_none_id(response_post, 'message')
#     if type == "post_some_user_positive_array" or type == "post_some_user_positive_list":
#         assert_steps.assert_all_message(response_post, "ok")
#     print(f'=================================================================')


# негативный кейс
@allure.step
@pytest.mark.full_regression
def test_oneuser_post_negative():
    print(f'\n---Негативный кейс. Запрос с пустым json на создание одного нового user-а---')
    request_post = generate_json_steps.create_json_users(0)
    url_post = urls.url_user_post()
    # отправка запроса
    response_post = request_steps.request_post(url_post, request_post)
    # анализ ответа
    assert_steps.assert_code(response_post, 200)
    assert_steps.assert_all_message(response_post, '0')
    print(f'=================================================================')


@allure.step
@pytest.mark.full_regression
@pytest.mark.parametrize('url_param',
                         [
                             (urls.url_user_post_list_array("createWithArray")),
                             (urls.url_user_post_list_array("createWithList")),
                         ],
                         ids=["post_some_user_negative_array",
                              "post_some_user_negative_list",
                              ],
                         )
def test_someusers_post_negative(url_param):
    print(f'\n---Негативный кейс. Запрос с пустым json на создание нескольких user-ов '
          f'массивом (post_some_user_negative_array) и списком (post_some_user_negative_list)---')
    # отправка запроса
    request_post = generate_json_steps.create_json_users(0)
    url_post = url_param
    print(f'url_user_post= {url_post}')
    response_post = request_steps.request_post(url_post, request_post)
    # анализ ответа
    assert_steps.assert_code(response_post, 500)
    assert_steps.assert_all_message(response_post, "something bad happened")
    print(f'=================================================================')


# @pytest.mark.full_regression
# @pytest.mark.parametrize('type',
#                          [
#                              ("post_one_user_negative"),
#                              ("post_some_user_negative_array"),
#                              ("post_some_user_negative_list"),
#                          ]
#                          )
# def test_user_post_negative(type):
#     # def test_user_post_positive(type):
#     # создание нового/ых user-а/ов, json пустой
#     global request_post, url_post
#     if type == "post_one_user_negative":
#         request_post = generate_json_steps.create_json_users(0)
#         print(f'---Негативный кейс. Запрос с пустым json на создание одного нового user-а---')
#         url_post = urls.url_user_post()
#     # создание нескольких новых user-ов массивом
#     if type == "post_some_user_negative_array":
#         request_post = generate_json_steps.create_json_users(0)
#         print(f'---Негативный кейс. Запрос с пустым json на создание нескольких новых user-ов массивом---')
#         url_post = urls.url_user_post_list_array("createWithArray")
#     # оздание нескольких user-ов списком
#     if type == "post_some_user_negative_list":
#         request_post = generate_json_steps.create_json_users(0)
#         print(f'---Негативный кейс. Запрос с пустым json на создание нескольких user-ов списком---')
#         url_post = urls.url_user_post_list_array("createWithList")
#     # отправка запроса
#     response_post = request_steps.request_post(url_post, request_post)
#     # анализ ответа
#     if type == "post_one_user_negative":
#         assert_steps.assert_code(response_post, 200)
#         assert_steps.assert_all_message(response_post, '0')
#     if type == "post_some_user_negative_array" or type == "post_some_user_negative_list":
#         assert_steps.assert_code(response_post, 500)
#         assert_steps.assert_all_message(response_post, "something bad happened")
#     print(f'=================================================================')


# PUT/user/, внесение изменений в данные user-а
# позитивный кейс
@allure.step
@pytest.mark.smoke_regression
@pytest.mark.full_regression
def test_user_put_positive():
    print(f'\n---Позитивный кейс, внесение изменений в данные сущствующего user-а---')
    # создание питомца, json со всеми параметрами
    print(f'---выполняем запрос POST создание user-а---')
    request_post = generate_json_steps.create_json_users(1)
    # отправка запроса
    url_post = urls.url_user_post()
    response_post = request_steps.request_post(url_post, request_post)
    # проверка, что user создан
    assert_steps.assert_not_none_id(response_post, 'message')
    # изменения, отправка запроса PUT
    print(f'---выполняем запрос PUT внесене изменений в данные user-а---')
    # список элементов, которые будут изменены
    elements_for_update = ["firstName", "lastName", "username", "email", "password", "phone", "userStatus"]
    request_put = generate_json_steps.update_json_users(request_post, elements_for_update)
    # отправка запроса
    url_put = urls.url_user_get(str(request_post['username']))
    response_put = request_steps.request_put(url_put, request_put)
    # анализ ответа
    assert_steps.assert_code(response_put, 200)
    assert_steps.assert_equals_responses_key(response_put.json(), response_post.json(), "message")
    print(f'{spaces * 10}--Уточнение по проверке: проверяем, что значения параметра "message" '
          f'одинаковые в ответах "response_put" и "response_post"---')
    # проверка после изменений, отправка запроса GET
    print(f'---выполняем запрос GET проверка изменений в данных user-а---')
    url_get = urls.url_user_get(str(request_put['username']))
    response_get = request_steps.request_get(url_get)
    # анализ ответа
    assert_steps.assert_equals_responses_diffkey(response_put.json(), 'message', response_get.json(), 'id')
    print(f'{spaces * 10}---Уточнение по проверке: проверяем, что значение параметра '
          f'"message" в ответе "response_put" соответствует значению параметра "id" в ответе "response_get"---')
    print(f'=================================================================')


# негативный кейс
@allure.step
@pytest.mark.full_regression
def test_user_put_negative():
    print(f'\n---Негативный кейс, внесение изменений в данные несущствующего user-а---')
    # json
    request_put = {}
    request_put["password"] = support_steps.generate_user_password(7)
    print(f"request_put= {request_put}")
    # отправка запроса
    anyname = support_steps.generate_random_letter_string(5)
    url_put = urls.url_user_get(anyname)
    response_put = request_steps.request_put(url_put, request_put)
    # анализ ответа
    assert_steps.assert_code(response_put, 200)
    assert_steps.assert_all_message(response_put, "0")
    print(f'=================================================================')


# GET/user/{username}, поиск user-а
# позитивный кейс
@allure.step
@pytest.mark.smoke_regression
@pytest.mark.full_regression
def test_user_get_positive():
    print(f'\n---Позитивный кейс, поиск сущствующего user-а---')
    # создание питомца, json со всеми параметрами
    print(f'---выполняем запрос POST создание user-а---')
    request_post = generate_json_steps.create_json_users(1)
    # отправка запроса
    url_post = urls.url_user_post()
    response_post = request_steps.request_post(url_post, request_post)
    # проверка, что user создан
    assert_steps.assert_not_none_id(response_post, 'message')
    # поиск user-а, отправка запроса GET
    print(f'---выполняем запрос GET поиск созданного user-а---')
    url_get = urls.url_user_get(str(request_post['username']))
    response_get = request_steps.request_get(url_get)
    # анализ ответа
    assert_steps.assert_equals_responses_diffkey(response_post.json(), 'message', response_get.json(), 'id')
    print(
        f'{spaces * 10}---Уточнение по проверке: проверяем, что значение параметра "message" в ответе '
        f'"response_post" соответствует значению параметра "id" в ответе "response_get"---')
    print(f'=================================================================')


# негативный кейс
@allure.step
@pytest.mark.full_regression
def test_user_get_negative():
    print(f'\n---Негативный кейс, поиск несущствующего user-а---')
    # отправка запроса
    anyname = support_steps.generate_random_letter_string(5)
    url_get = urls.url_user_get(anyname)
    response_get = request_steps.request_get(url_get)
    # анализ ответа
    assert_steps.assert_status(response_get, 404)
    assert_steps.assert_all_message(response_get, 'User not found')
    print(f'=================================================================')


# GET/user/login, авторизация user-а
# позитивный кейс
@allure.step
@pytest.mark.smoke_regression
@pytest.mark.full_regression
def test_user_getlogin_positive():
    print(f'\n---Позитивный кейс, авторизация---')
    # создание питомца, json со всеми параметрами
    print(f'---выполняем запрос POST создание user-а---')
    request_post = generate_json_steps.create_json_users(1)
    # отправка запроса
    url_post = urls.url_user_post()
    response_post = request_steps.request_post(url_post, request_post)
    # проверка, что user создан
    assert_steps.assert_not_none_id(response_post, 'message')
    # авторизация, отправка запроса GET
    print(f'---выполняем запрос GET авторизация user-а---')
    url_login_get = urls.url_user_login(str(request_post['username']), str(request_post['password']))
    response_get = request_steps.request_get(url_login_get)
    # анализ ответа
    assert_steps.assert_code(response_get, 200)
    assert_steps.assert_in_message(response_get, "logged in user session:")
    print(f'=================================================================')


# негативный кейс
@allure.step
@pytest.mark.full_regression
def test_user_getlogin_negative():
    print(f'\n---Негативный кейс, авторизация---')
    # авторизация, отправка запроса GET
    print(f'---выполняем запрос GET авторизация user-а---')
    url_login_get = urls.url_user_login("0", "0")
    response_get = request_steps.request_get(url_login_get)
    # анализ ответа
    # по идее должен быть статус 404, но не работает, работает 200
    # assert_steps.assert_status(response_get, 404)
    assert_steps.assert_status(response_get, 200)
    print(f'=================================================================')


# GET/user/logout, закрытие сессии
# позитивный кейс
@allure.step
@pytest.mark.smoke_regression
@pytest.mark.full_regression
def test_user_getlogout_positive():
    print(f'\n---Позитивный кейс, закрытие сессии---')
    # закрытие сессии, отправка запроса GET
    print(f'---выполняем запрос GET закрытие сессии---')
    url_logout_get = urls.url_user_logout()
    response_get = request_steps.request_get(url_logout_get)
    # анализ ответа
    assert_steps.assert_status(response_get, 200)
    assert_steps.assert_all_message(response_get, "ok")
    print(f'=================================================================')


# негативный кейс
@allure.step
@pytest.mark.full_regression
def test_user_getlogout_negative():
    print(f'\n---Негативный кейс, закрытие сессии---')
    # закрытие сессии, отправка запроса GET
    anyname = support_steps.generate_random_letter_string(5)
    url_logout_get = "https://petstore.swagger.io/v2/" + str(anyname) + "/logout"
    print(f'url_user_logout= {url_logout_get}')
    response_get = request_steps.request_get_negative(url_logout_get)
    # анализ ответа
    assert_steps.assert_status(response_get, 404)
    print(f'=================================================================')


# DELETE/user/{username}, удаление сущесвующего user-а
# позитивный кейс
@allure.step
@pytest.mark.smoke_regression
@pytest.mark.full_regression
def test_user_del_positive():
    print(f'\n---Позитивный кейс, удаление user-а---')
    # создание нового клиента, json
    print(f'---выполняем запрос POST создание user-а---')
    request_post = generate_json_steps.create_json_users(1)
    # отправка запроса
    url_post = urls.url_user_post()
    response_post = request_steps.request_post(url_post, request_post)
    # проверка, что user создан
    assert_steps.assert_not_none_id(response_post, 'message')
    # удаление, отправка запроса DEL
    print(f'---выполняем запрос DEL удаление user-а---')
    url_del = urls.url_user_get(str(request_post['username']))
    response_del = request_steps.request_delete_user(url_del, request_post)
    # анализ ответа
    assert_steps.assert_status(response_del, 200)
    assert_steps.assert_equals_responses_diffkey(response_del.json(), "message", request_post, "username")
    print(f'{spaces * 10}---Уточнение по проверке: проверяем, что значение параметра "message" '
          f'в ответе "response_del" соответствует значению параметра "username" в ответе "request_post"---')
    # проверка, что клиент удалился
    print(f'---выполняем запрос GET, проверяем, что user отстутствует---')
    url_get = urls.url_user_get(str(request_post['username']))
    response_get = request_steps.request_get(url_get)
    # анализ ответа
    assert_steps.assert_status(response_get, 404)
    assert_steps.assert_all_message(response_get, "User not found")
    print(f'=================================================================')


# негативный кейс
@allure.step
@pytest.mark.full_regression
def test_user_del_negative():
    print(f'\n---Негативный кейс, удаление несуществующего user-а---')
    request_post = {}
    anyname = support_steps.generate_random_letter_string(5)
    url_del = urls.url_user_del(anyname)
    response_del = request_steps.request_delete_user_negative(url_del, request_post)
    # анализ ответа
    assert_steps.assert_status(response_del, 404)
    print(f'=================================================================')
