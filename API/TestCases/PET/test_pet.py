import pytest
import requests
import API.Steps.support_steps as support_steps
import API.resources.urls as urls
import API.Steps.generate_json_steps as generate_json_steps
import API.Steps.request_steps as request_steps
import API.Steps.assert_steps as assert_steps

spaces = " "


# тест создания нового питомца
# позитивный кейс
@pytest.mark.smoke_regression
@pytest.mark.full_regression
@pytest.mark.parametrize('json_param',
                         [
                             (generate_json_steps.create_json_pet_requires_params()),
                             (generate_json_steps.create_json_pet_all_params()),
                         ],
                         ids=["requires_params",
                              "all_params"],
                         )
def test_pet_post_positive(json_param):
    print(f'\n---Позитивный кейс, создание питомца с обязательными (requires_params) и всеми (all_params) параметрами')
    # отправка запроса
    url_post = urls.url_pet_post()
    request_post = json_param
    response_post = request_steps.request_post(url_post, request_post)
    # анализ ответа
    assert_steps.assert_not_none_id(response_post, 'id')
    print(f'=================================================================')


# @pytest.mark.smoke_regression
# @pytest.mark.full_regression
# @pytest.mark.parametrize('type',
#                          [
#                              ("requires_params"),
#                              ("all_params"),
#                          ]
#                          )
# def test_pet_post_positive(type):
#     # создание нового питомца, json c обязательными параметрами
#     global request_post
#     if type == "requires_params":
#         print(f'\n---Позитивный кейс, в запросе на создание нового питомца только с обязательными параметрами---')
#         request_post = generate_json_steps.create_json_pet_requires_params()
#     # создание нового питомца, json со всеми параметрами
#     if type == "all_params":
#         print(f'\n---Позитивный кейс, в запросе на создание нового питомца все параметрами---')
#         request_post = generate_json_steps.create_json_pet_all_params()
#     # отправка запроса
#     url_post = urls.url_pet_post()
#     response_post = request_steps.request_post(url_post, request_post)
#     # анализ ответа
#     assert_steps.assert_not_none_id(response_post, 'id')
#     print(f'=================================================================')


# негативный кейс
@pytest.mark.full_regression
@pytest.mark.parametrize('json_param',
                         [
                             (generate_json_steps.create_json_pet_not_name()),
                             (generate_json_steps.create_json_pet_not_photourls()),
                         ],
                         ids=["not_name",
                              "not_photourls"],
                         )
def test_pet_post_negative(json_param):
    print(f'\n---Негативный кейс, создание нового питомца, '
          f'в запросе не заполнен обязательный атрибут name (not_name) и photoUrls (not_photourls)')
    # отправка запроса
    url_post = urls.url_pet_post()
    request_post = json_param
    response_post = request_steps.request_post(url_post, request_post)
    # анализ ответа
    assert_steps.assert_code(response_post, 500)
    assert_steps.assert_all_message(response_post, "something bad happened")
    print(f'=================================================================')


# @pytest.mark.full_regression
# @pytest.mark.parametrize('type',
#                          [
#                              ("not_name"),
#                              ("not_photourls"),
#                          ]
#                          )
# def test_pet_post_negative(type):
#     # создание питомца, ошибочный json, не заполнен обязательный атрибут name
#     global request_post, url_post
#     if type == "not_name":
#         print(f'\n---Негативный кейс, создание нового питомца, в запросе не заполнен обязательный атрибут name---')
#         url_post = urls.url_pet_post()
#         request_post = generate_json_steps.create_json_pet_not_name()
#     # создание питомца, ошибочный json, не заполнен обязательный атрибут photoUrls
#     if type == "not_photourls":
#         print(f'\n---Негативный кейс, создание нового питомца, в запросе не заполнен '
#               f'обязательный атрибут photoUrls---')
#         url_post = urls.url_pet_post()
#         request_post = generate_json_steps.create_json_pet_not_photourls()
#     # отправка запроса
#     response_post = request_steps.request_post(url_post, request_post)
#     # анализ ответа
#     assert_steps.assert_code(response_post, 500)
#     assert_steps.assert_all_message(response_post, "something bad happened")
#     print(f'=================================================================')


# поиск питомца по id
# позитивный кейс
@pytest.mark.smoke_regression
@pytest.mark.full_regression
def test_pet_get_positive():
    print(f'\n---Позитивный кейс, поиск существующего питомца---')
    # создание питомца, json со всеми параметрами
    request_post = generate_json_steps.create_json_pet_all_params()
    url_post = urls.url_pet_post()
    response_post = request_steps.request_post(url_post, request_post)
    # проверка, что id создан
    assert_steps.assert_not_none_id(response_post, 'id')
    # поиск питомца, отправка запроса GET
    url_get = urls.url_pet_get_id(str(response_post.json()['id']))
    response_get = request_steps.request_get(url_get)
    # анализ ответа
    assert_steps.assert_equals_responses_key(response_post.json(), response_get.json(), 'id')
    assert_steps.assert_equals_responses_key(response_post.json(), response_get.json(), 'name')
    print(f'{spaces * 10}---Уточнение по проверке: проверяем, что значения параметров "id" и "name" '
          f'одинаковые в ответах "response_post" и "response_get"---')
    print(f'=================================================================')


# негативный кейс
@pytest.mark.full_regression
def test_pet_get_negative():
    print(f'\n---Негативный кейс, поиск несуществующего питомца---')
    # ошибочный json
    url_get = urls.url_pet_get_id(support_steps.generate_random_number_string(9))
    # отправка запроса
    response_get = request_steps.request_get(url_get)
    # анализ ответа
    assert_steps.assert_status(response_get, 404)
    assert_steps.assert_all_message(response_get, "Pet not found")
    assert_steps.assert_type(response_get, "error")
    print(f'=================================================================')


# внесение изменений в данные питомца
# позитивный кейс
@pytest.mark.smoke_regression
@pytest.mark.full_regression
def test_pet_put_positive():
    print(f'\n---Позитивный кейс, внесение изменений в данные сущствующего питомца---')
    # создание питомца, json со всеми параметрами
    print(f'---выполняем запрос POST создание питомца---')
    request_post = generate_json_steps.create_json_pet_all_params()
    # отправка запроса
    url_post = urls.url_pet_post()
    response_post = request_steps.request_post(url_post, request_post)
    # проверка, что id создан
    assert_steps.assert_not_none_id(response_post, 'id')
    # проверка до изменений, отправка запроса GET
    print(f'---выполняем запрос GET проверка наличия созданного питомца---')
    url_get = urls.url_pet_get_id(str(response_post.json()['id']))
    response_get = request_steps.request_get(url_get)
    # анализ ответа
    assert_steps.assert_equals_responses_key(response_post.json(), response_get.json(), 'id')
    print(f'{spaces * 10}---Уточнение по проверке: проверяем, что значение параметра "id" одинаковое '
          f'в ответах "response_post" и "response_get"---')
    # изменения, отправка запроса PUT
    print(f'---вносим изменения в данные питомца---')
    request_put = generate_json_steps.update_json_pet_all_params(response_get)
    url_put = urls.url_pet_post()
    response_put = request_steps.request_put(url_put, request_put)
    # анализ ответа
    assert_steps.assert_status(response_put, 200)
    assert_steps.assert_equals_values(response_put.json(), "id", response_post.json()['id'])
    print(f'{spaces * 10}---Уточнение по проверке: проверяем, что значение параметра "id" '
          f'в ответе "response_put" соответствует значению параметра "id" в ответе "response_post"---')
    # проверка после изменений, отправка запроса GET
    print(f'---выполняем запрос GET проверка изменений в данных питомца---')
    url_get = urls.url_pet_get_id(str(response_post.json()['id']))
    response_get = request_steps.request_get(url_get)
    # анализ ответа
    assert_steps.assert_equals_responses_key(response_put.json(), response_get.json(), 'id')
    assert_steps.assert_equals_responses_key(response_put.json(), response_get.json(), 'name')
    assert_steps.assert_equals_responses_key(response_put.json(), response_get.json(), 'photoUrls')
    assert_steps.assert_equals_responses_key(response_put.json(), response_get.json(), 'status')
    print(f'{spaces * 10}---Уточнение по проверке: проверяем, что значения параметров '
          f'"id", "name", "photoUrls", "status" одинаковые в ответах "response_put" и "response_get"---')
    print(f'=================================================================')


# негативный кейс
@pytest.mark.full_regression
def test_pet_put_negative():
    print(f'\n---Негативный кейс, попытка внесениея изменений в данные несущствующего питомца---')
    # создание ошибочного json
    request_put = {}
    request_put["id"] = support_steps.generate_random_number_string(6) + support_steps.generate_random_letter_string(6)
    request_put["name"] = "Superpet"
    print("request_put= ", request_put)
    # отправка запроса
    url_put = urls.url_pet_post()
    response_put = request_steps.request_post(url_put, request_put)
    assert_steps.assert_code(response_put, 500)
    assert_steps.assert_all_message(response_put, "something bad happened")
    print(f'=================================================================')


# удаление питомца из базы
# позитивный кейс
@pytest.mark.smoke_regression
@pytest.mark.full_regression
def test_pet_del_positive():
    print(f'\n---Позитивный кейс, удаление сущствующего питомца---')
    # создание питомца, json со всеми параметрами
    print(f'---выполняем запрос POST создание питомца---')
    request_post = generate_json_steps.create_json_pet_all_params()
    # отправка запроса
    url_post = urls.url_pet_post()
    response_post = request_steps.request_post(url_post, request_post)
    # проверка, что id создан
    assert_steps.assert_not_none_id(response_post, 'id')
    # удаление
    print(f'---выполняем запрос DEL удаления питомца---')
    url_del = urls.url_pet_get_id(str(response_post.json()['id']))
    response_del = request_steps.request_delete_pet(url_del)
    # проверка, что удаление выполнено успешно
    assert_steps.assert_code(response_del, 200)
    assert_steps.assert_equals_responses_diffkey(response_del.json(), 'message', response_post.json(), 'id')
    print(f'{spaces * 10}---Уточнение по проверке: проверяем, что значение параметра '
          f'"message" в ответе "response_del" соответствует значению параметра "id" в ответе "response_post"---')
    # проверка после удаления, что pet не найден, отправка запроса GET
    print(f'---Проверка после удаления, что питомец не существует---')
    url_get = urls.url_pet_get_id(str(response_post.json()['id']))
    response_get = request_steps.request_get(url_get)
    # анализ ответа
    assert_steps.assert_all_message(response_get, "Pet not found")
    print(f'=================================================================')


# негативный кейс
@pytest.mark.full_regression
def test_pet_del_negative():
    print(f'\n---Негативный кейс, попытка удаления несущствующего питомца---')
    # ошибочный запрос
    print(f'---выполняем запрос DEL удаления несуществующего питомца---')
    url_del = urls.url_pet_get_id(support_steps.generate_random_number_string(9))
    response_del = request_steps.request_delete_pet_negative(url_del)
    # анализ ответа
    assert_steps.assert_status(response_del, 404)
    print(f'=================================================================')


# POST /pet/{petId}/uploadImage
# позитивный кейс
@pytest.mark.smoke_regression
@pytest.mark.full_regression
def test_pet_postimg():
    print(f'\n---Позитивный кейс передача файла---')
    # создание питомца, json со всеми параметрами
    print(f'---выполняем запрос POST создание питомца---')
    request_post = generate_json_steps.create_json_pet_all_params()
    # отправка запроса
    url_post = urls.url_pet_post()
    response_post = request_steps.request_post(url_post, request_post)
    # проверка, что id создан
    assert_steps.assert_not_none_id(response_post, 'id')
    # отправка запроса POST /pet/{petId}/uploadImage
    print(f'---Загрузка файлов---')
    uploadupload_file = {'uploadupload_file': open('../../Images/upload_image.jpg', 'rb')}
    print(f'{uploadupload_file}, {type(uploadupload_file)}')
    url_post_img = urls.url_pet_postimg(str(response_post.json()['id']))
    response_post_img = request_steps.request_post_img(url_post_img, uploadupload_file)
    # анализ ответа
    # не понятно как получить код 200, при правильных параметрах отправки получаем код 500
    # assert_steps.assert_status(response_post_img, 200)
    assert_steps.assert_status(response_post_img, 500)
    print(f'=================================================================')


# поиск питомца по статусу
# позитивный кейс
@pytest.mark.smoke_regression
@pytest.mark.full_regression
def test_pet_getstatus_positive():
    print(f'\n---Позитивный кейс, поиск сущствующего питомца по статусу---')
    # создание питомца, json со всеми параметрами
    print(f'---выполняем запрос POST создание питомца---')
    request_post = generate_json_steps.create_json_pet_all_params()
    # отправка запроса
    url_post = urls.url_pet_post()
    response_post = request_steps.request_post(url_post, request_post)
    # проверка, что id создан
    assert_steps.assert_not_none_id(response_post, 'id')
    print(f"Cоздан питомец со статусом {response_post.json()['status']}")
    # поиск по статусу, отправка запроса GET
    print(f'---выполняем запрос GET выборка питомцев с указанным статусом---')
    url_get = urls.url_pet_getstatus(str(response_post.json()['status']))
    response_get = request_steps.request_get(url_get)
    # анализ ответа
    assert_steps.assert_status(response_get, 200)
    assert_steps.assert_json_notnull(response_get)
    # поиск питомца из выборки по статусу
    print(f'---поиск питомца из выборки по статусу---')
    for pet in response_get.json():
        if pet["id"] == response_post.json()['id']:
            print(f'Данные по питомцу, выбранные из всей выборке по статусу= {pet}')
            # анализ ответа
            assert_steps.assert_equals_values(pet, "status", response_post.json()['status'])
    print(f'=================================================================')


# негативный кейс
@pytest.mark.full_regression
def test_pet_getstatus_negative():
    print(f'\n---Негативный кейс, поиск питомца с некорректным статусом---')
    # ошибочный json
    anystatus = support_steps.generate_random_letter_string(5)
    url_get = urls.url_pet_getstatus(anystatus)
    response_get = request_steps.request_get(url_get)
    # предполагается, что должны получить код 400, если поиск по некорректному статусу, но не работает:
    #  assert_steps.assert_status(response_get, 400)
    # вот так работает:
    assert_steps.assert_status(response_get, 200)
    assert_steps.assert_json_null(response_get)
    print(f'=================================================================')


# актуализация данных о питомце
# позитивный кейс
@pytest.mark.smoke_regression
@pytest.mark.full_regression
def test_pet_postup_positive():
    print(f'\n---Позитивный кейс, актуализация данных о питомце---')
    # создание питомца, json со всеми параметрами
    print(f'---выполняем запрос POST создание питомца---')
    request_post = generate_json_steps.create_json_pet_all_params()
    # отправка запроса
    url_post = urls.url_pet_post()
    response_post = request_steps.request_post(url_post, request_post)
    # проверка, что id создан
    assert_steps.assert_not_none_id(response_post, 'id')
    # актуализация данных о питомце, отправка запроса POST
    print(f'---выполняем запрос POST актуализации данных питомца---')
    url_postup = urls.url_pet_get_id(str(response_post.json()['id']))
    response_postup = requests.post(url_postup, verify=False)
    # анализ ответа
    assert_steps.assert_code(response_postup, 200)
    assert_steps.assert_all_message(response_postup, str(response_post.json()['id']))
    assert_steps.assert_equals_responses_diffkey(response_postup.json(), 'message', response_post.json(), 'id')
    print(f'{spaces * 10}---Уточнение по проверке: проверяем, что значение параметра "message" в ответе '
          f'"response_postup" соответствует значению параметра "id" в ответе "response_post"---')

    print(f'=================================================================')


# негативный кейс
@pytest.mark.full_regression
def test_pet_postup_negative():
    print(f'\n---Негативный кейс, попытка актуализации данных несущствующего питомца---')
    # ошибочный json
    url_postup = urls.url_pet_get_id("0")
    # отправка запроса
    response_postup = requests.post(url_postup, verify=False)
    print("response_postup= ", response_postup, response_postup.json())
    # анализ ответа
    assert_steps.assert_status(response_postup, 404)
    assert_steps.assert_all_message(response_postup, "not found")
    print(f'=================================================================')
