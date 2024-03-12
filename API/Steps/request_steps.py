# Функции для методов создания запросов
import allure
import requests


# ---- для PET ----
# отправка запроса и получение ответа для метода DEL
# url - эндпоинт
def request_delete_pet(url):
    with allure.step("отправка запроса и получение ответа для метода DEL в проекте PET"):
        response_del = requests.delete(url, verify=False)
        print("response_del= ", response_del, response_del.json())
        return response_del


def request_delete_pet_negative(url):
    with allure.step("отправка запроса и получение ответа для метода DEL в проекте PET для негативных кейсов"):
        response_del = requests.delete(url, verify=False)
        print("response_del= ", response_del)
        return response_del


# отправка запроса на передачу файлов и получение ответа для метода POST
# url - эндпоинт
def request_post_img(url, file):
    with allure.step("отправка запроса на передачу файлов и получение ответа для метода POST в проекте PET"):
        response_post_img = requests.post(url, files=file, verify=False)
        print("response_post_img= ", response_post_img)
        return response_post_img


# ---- для USER ----
# отправка запроса и получение ответа для метода DEL
# url - эндпоинт
def request_delete_user(url, request):
    with allure.step("отправка запроса и получение ответа для метода DEL в проекте USER"):
        response_del = requests.delete(url, json=request, verify=False)
        print("response_del= ", response_del, response_del.json())
        return response_del


def request_delete_user_negative(url, request):
    with allure.step("отправка запроса и получение ответа для метода DEL в проекте USER для негативных кейсов"):
        response_del = requests.delete(url, json=request, verify=False)
        print("response_del= ", response_del)
        return response_del


# ---- ОБЩИЕ ----
# отправка запроса и получение ответа для метода POST
# url - эндпоинт
# request - JSON
def request_post(url, request):
    with allure.step("отправка запроса и получение ответа для метода POST"):
        response_post = requests.post(url, json=request, verify=False)
        print("response_post= ", response_post, response_post.json())
        return response_post


# отправка запроса и получение ответа для метода GET
# url - эндпоинт
def request_get(url):
    with allure.step("отправка запроса и получение ответа для метода GET"):
        response_get = requests.get(url, verify=False)
        print("response_get= ", response_get, response_get.json())
        return response_get


def request_get_negative(url):
    with allure.step("отправка запроса и получение ответа для метода GET для негативных кейсов"):
        response_get = requests.get(url, verify=False)
        print("response_get= ", response_get)
        return response_get


# отправка запроса и получение ответа для метода PUT
# url - эндпоинт
def request_put(url, request):
    with allure.step("отправка запроса и получение ответа для метода PUT"):
        response_put = requests.put(url, json=request, verify=False)
        print("response_put= ", response_put, response_put.json())
        return response_put
