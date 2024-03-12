# Генерация json

import API.Steps.support_steps as support_steps
import allure


# ---- для PET ----
# JSON для метода POST/pet c обязательными параметрами
def create_json_pet_requires_params():
    with allure.step("JSON для метода POST /pet c обязательными параметрами"):
        request_post = {}
        request_post["name"] = support_steps.generate_random_letter_string(6)
        request_post["photoUrls"] = [support_steps.generate_pet_photourls(str(request_post["name"]))]
        print(f"request_post= {request_post}")
        return request_post


# JSON для метода POST/pet со всеми параметрами
def create_json_pet_all_params():
    with allure.step("JSON для метода POST/pet cо всеми параметрами"):
        request_post = {}
        request_post["name"] = support_steps.generate_random_letter_string(6)
        request_post["category"] = {}
        request_post["category"]["id"] = support_steps.generate_random_number_string(1)
        request_post["category"]["name"] = support_steps.generate_pet_subnamepet(str(request_post["name"]))
        request_post["photoUrls"] = [f'{support_steps.generate_pet_photourls(str(request_post["name"]))}.jpg']
        request_post["tags"] = [{}]
        request_post["tags"][0]["id"] = int(request_post["category"]["id"]) * 2
        request_post["tags"][0]["name"] = f'tag_{request_post["tags"][0]["id"]}_{request_post["name"]}'
        all_status = ["available", "pending", "sold"]
        request_post["status"] = support_steps.random_element_from_list(all_status)
        print(f"request_post= {request_post}")
        return request_post


# JSON для метода POST/pet если не заполнен обязательный параметр name
def create_json_pet_not_name():
    with allure.step("JSON для метода POST/pet если не заполнен обязательный параметр name"):
        request_post = {}
        request_post["name"] = []
        request_post["photoUrls"] = [support_steps.generate_pet_photourls(str(request_post["name"]))]
        print(f"request_post= {request_post}")
        return request_post


# JSON для метода POST/pet если не заполнен обязательный параметр photoUrls
def create_json_pet_not_photourls():
    with allure.step("JSON для метода POST/pet если не заполнен обязательный параметр photoUrls"):
        request_post = {}
        request_post["name"] = support_steps.generate_random_letter_string(6)
        request_post["photoUrls"] = ""
        print(f"request_post= {request_post}")
        return request_post


# JSON для метода PUT/pet со всеми параметрами
def update_json_pet_all_params(out_response):
    # используется только если в функции предусмотрен предшествующий вызов POST или GET с выводом всех параметров
    # !!! аргументы out_request, out_response из ранее отравленного запроса POST
    with allure.step("JSON для метода PUT /pet со всеми параметрами"):
        request_put = {}
        request_put["id"] = str(out_response.json()['id'])
        request_put["name"] = f"Super_{out_response.json()['name']}"
        request_put["category"] = {}
        request_put["category"]["id"] = int(out_response.json()['category']['id']) * 2
        request_put["category"]["name"] = f"category_{request_put['name']}"
        request_put["photoUrls"] = [f"foto_{request_put['name']}.jpg"]
        request_put["tags"] = [{}]
        request_put["tags"][0]["id"] = int(out_response.json()['tags'][0]['id']) * 2
        request_put["tags"][0]["name"] = f"tag_{request_put['name']}"
        all_status = ["available", "pending", "sold"]
        for s in all_status:
            if s == out_response.json()['status']:
                all_status.remove(s)
                request_put["status"] = support_steps.random_element_from_list(all_status)
        print("request_put= ", request_put)
        return request_put


# ---- для USER ----
# JSON для метода POST/user создания user-а/ов
def create_json_users(count):
    with allure.step("JSON для метода POST/user создания user-а/ов"):
        request_post = {}
        request_post["firstName"] = support_steps.generate_random_letter_string_capitalize(6)
        request_post["lastName"] = support_steps.generate_random_letter_string_capitalize(9)
        request_post["username"] = support_steps.generate_username(str(request_post['firstName']),
                                                                   str(request_post['lastName']))
        request_post["email"] = support_steps.generate_user_email(str(request_post['firstName']),
                                                                  str(request_post['lastName']))
        request_post["password"] = support_steps.generate_user_password(7)
        request_post["phone"] = support_steps.generate_user_phone()
        request_post["userStatus"] = support_steps.generate_random_number_string(1)
        if count == 1:
            # если count == 1 будет создан json одного user
            print(f"request_post= {request_post}")
            return request_post
        elif count > 1:
            # если count > 1 будет создан json на несколько user, по количеству count
            users = []
            for i in range(count):
                users.append(request_post)
            print(f"users= {users}")
            return users
        else:
            request_post = {}
            # если count = 0 json будет пустой
            print(f"request_post= {request_post}")
            return request_post


# JSON для метода PUT/user изменения user-а/ов
def update_json_users(from_req_post, elements_for_update: list):
    with allure.step("JSON для метода PUT/user изменения user-а/ов"):
        request_put = {}
        # request_put["id"] = from_res_post.json()['message']
        request_put["username"] = str(from_req_post['username'])
        if elements_for_update:
            for el in elements_for_update:
                if el == "firstName":
                    request_put[el] = f"Super{from_req_post[el].lower()}"
                    continue
                elif el == "lastName":
                    request_put[el] = f"Puper{from_req_post[el].lower()}"
                    continue
                elif el == "username":
                    request_put[el] = support_steps.generate_username(str(request_put['firstName']),
                                                                      str(request_put['lastName']))
                    continue
                elif el == "email":
                    request_put[el] = support_steps.generate_user_email(str(request_put['firstName']),
                                                                        str(request_put['lastName']))
                    continue
                elif el == "password":
                    request_put[el] = support_steps.generate_user_password(7)
                    continue
                elif el == "phone":
                    request_put[el] = support_steps.generate_user_phone()
                    continue
                elif el == "userStatus":
                    request_put[el] = support_steps.generate_random_number_string(1)
                else:
                    break
                print(f"request_put= {request_put}")
                return request_put
