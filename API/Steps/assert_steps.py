# Проверка утверждений. С помощью оператора assert проверяется, является ли условие истинным.
import allure

spaces = " "


# проверка утверждения, что значение укзанного параметра в ответе не пусто
# !!! использовать для проверки создания/сущестования объекта!!!
def assert_not_none_id(response, key):
    with allure.step("проверка утверждения, что значение укзанного параметра в ответе не пусто"):
        assert response.json()[key] is not None
        if key == "id" or key == "message":
            print(
                f'{spaces * 10}PASSED: значение "{key}" не пусто: {str(response.json()[key])}, объект создан/существует')
        else:
            pass


# проверка утверждения, что json-ответ пустой
def assert_json_null(response):
    with allure.step("проверка утверждения, что json-ответ пустой"):
        assert response.json() == []
        print("          PASSED: json-ответ пустой")


# проверка утверждения, что json-ответ не пустой
def assert_json_notnull(response):
    with allure.step("проверка утверждения, что json-ответ не пустой"):
        assert response.json() != []
        print("          PASSED: получен json-ответ")


# проверка утверждения, что значения указанного параметра в ответах равны (параметр один и тот же в двух ответах)
def assert_equals_responses_key(first, second, key):
    with allure.step(
            "проверка утверждения, что значения указанного параметра в ответах равны (параметр один и тот же в двух ответах)"):
        assert str(first[key]) == str(second[key])
        print(f'{spaces * 10}PASSED: значения "{key}" в ответах эквивалентны')


# проверка утверждения, что значения разных парамтеров в ответах равны
def assert_equals_responses_diffkey(firstresponse, firstkey, secondresponse, secondkey):
    with allure.step("проверка утверждения, что значения разных парамтеров в ответах равны"):
        assert str(firstresponse[firstkey]) == str(secondresponse[secondkey])
        print(
            f'{spaces * 10}PASSED: значения "{firstkey}" и "{secondkey}" в ответах эквивалентны')


# поверка соотетствия указанному значению
# !!!альтернативный метод для assert_equals_responses_key и assert_equals_responses_diffkey!!!
def assert_equals_values(result, key, value):
    with allure.step("поверка соотетствия указанному значению"):
        assert result[key] == value
        print(f'{spaces * 10}PASSED: значение "{key}" соответствует "{value}"')


# проверка статуса
def assert_status(response, status):
    with allure.step("проверка статуса"):
        assert str(response).__contains__(f"{status}") == True
        print(f'{spaces * 10}PASSED: получен ожидаемый статус "{status}"')


# проверка получения кода
def assert_code(response, code):
    with allure.step("проверка получения кода"):
        assert response.json()["code"] == code
        print(f'{spaces * 10}PASSED: получен ожидаемый код "{code}"')


# проверка сообщения, соответствие всей фразы сообщения
def assert_all_message(response, message):
    with allure.step("проверка сообщения, соответствие всей фразы сообщения"):
        assert response.json()["message"] == message
        print(f'{spaces * 10}PASSED: получено ожидаемое сообщение "{message}"')


# проверка сообщения, соответствие части фразы в сообщении
def assert_in_message(response, message):
    with allure.step("проверка сообщения, соответствие части фразы в сообщении"):
        assert message in response.json()["message"]
        print(f'{spaces * 10}PASSED: в полученном сообщении присутствует ожидаемое выражение: "{message}"')


# соответствие типа полученного сообщения
def assert_type(response, response_type):
    with allure.step("проверка утверждения, что значение укзанного параметра в ответе не пусто"):
        assert response.json()["type"] == response_type
        print(f'{spaces * 10}PASSED: получен ожидаемый тип ответа "{response_type}"')
