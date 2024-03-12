# Константы запросов
import allure

main_url = "https://petstore.swagger.io/v2/"


# ---- для PET ----
def url_pet_post():
    print(f'url_pet_post= {main_url + "pet/"}')
    return main_url + "pet/"


def url_pet_get_id(pet_id):
    get_id = main_url + "pet/" + pet_id
    print(f'get_id= {get_id}')
    return get_id


def url_pet_postimg(pet_id):
    postimg = main_url + "pet/" + pet_id + "/uploadImage"
    print(f'postimg= {postimg}')
    return postimg


def url_pet_getstatus(status):
    getstatus = main_url + "pet/" + "findByStatus?status=" + status
    print(f'getstatus= {getstatus}')
    return getstatus


# ---- для USER ----
def url_user_post():
    print(f'url_user_post= {main_url + "user/"}')
    return main_url + "user/"


def url_user_get(username):
    user_get = main_url + "user/" + username
    print(f'user_get= {user_get}')
    return user_get


def url_user_post_list_array(list_array):
    user_post_list_array = main_url + "user/" + list_array + "/"
    print(f'user_post_list_array= {user_post_list_array}')
    return user_post_list_array


def url_user_login(name, password):
    user_login = main_url + "user/" + "login?username=" + name + "&password=" + password
    print(f'user_login= {user_login}')
    return user_login


def url_user_logout():
    user_logout = main_url + "user/logout"
    print(f'user_logout= {user_logout}')
    return user_logout


def url_user_del(username):
    user_del = main_url + "user/" + username
    print(f'user_del= {user_del}')
    return user_del
