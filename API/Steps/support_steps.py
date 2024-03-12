# Вспомогательные шаги, генерация данных

import random
import string
import allure


# ----ОБЩИЕ----
# генерирует числа
def generate_random_number_string(length):
    result = ""
    for i in range(0, length):
        result += str(random.randint(0, 9))
    return result


# генерирует и прописные, и строчные буквы
def generate_random_letter_string(length):
    result = ""
    for i in range(0, length):
        result += str(random.choice(string.ascii_letters[random.randint(0, 5)]))
    return result


# генерирует только строчные буквы
def generate_random_letter_string_lower(length):
    result = ""
    for i in range(0, length):
        result += str(random.choice(string.ascii_lowercase[random.randint(0, 5)]))
    return result


# генерирует строку с заглавной первой буквой
def generate_random_letter_string_capitalize(length):
    result = generate_random_letter_string(length)
    return result.capitalize()


# случаный выбор элемента из списка
def random_element_from_list(el_list):
    return random.choice(el_list)


# ---- для USER ----
# генерирует пароль
def generate_user_password(length):
    result = ""
    for i in range(length):
        result += ''.join(random.choice(string.ascii_letters + string.digits))
    return result


# генерирует номер телефона
def generate_user_phone():
    phone = ''.join("+7-" + generate_random_number_string(3) + "-" + generate_random_number_string(
        3) + "-" + generate_random_number_string(2) + "-" + generate_random_number_string(2))
    return phone


# гененрирует username из firstname и lastname
def generate_username(firstname, lastname):
    username = firstname[0] + lastname
    return username


# гененрирует email из firstname и lastname
def generate_user_email(firstname, lastname):
    email = firstname[0].lower() + "_" + lastname.lower() + "@" + generate_random_letter_string(4) + ".com"
    return email


# ---- для PET ----
# генерирует name для разделов category и tags
def generate_pet_subnamepet(namepet):
    subnamepet = namepet + "ss"
    return subnamepet


# генерирует photoUrls
def generate_pet_photourls(namepet):
    photourls = "photo_" + namepet
    return photourls
