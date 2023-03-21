import requests
from requests.auth import HTTPBasicAuth

email = 'qatester@mail.com'
base_url = f"https://hr.recruit.liis.su/qa0/v1/api/{email}/"


def get_posts():                                                                                                        #Функция выводит все посты пользователя
    r = requests.get(base_url + 'posts')
    status_code = r.status_code
    body = r.json()
    return status_code, body


def post_posts(title, content):                                                                                         #Функция добавляет новый пост пользователя, принимает на вход заголовок и контент
    data = {
        "title": title,
        "content": content
    }
    r = requests.post(base_url + 'posts', auth=HTTPBasicAuth('QAtester', '123'), json=data)
    status_code = r.status_code
    result = r.json()
    return status_code, result


def get_new_posts(post_id):                                                                                             #Функция выводит пост пользователя, принимая на вход id поста
    r = requests.get(base_url + 'post/' + post_id)
    status_code = r.status_code
    body = r.json()
    return status_code, body


def put_post(post_id, title, content):                                                                                  #Функция изменяет пост пользователя, принимает на вход id поста, название и контент
    data = {
        "title": title,
        "content": content
    }
    r = requests.put(base_url + 'post/' + post_id, auth=HTTPBasicAuth('QAtester', '123'), json=data)
    status_code = r.status_code
    body = r.json()
    return status_code, body


def delete_post(post_id):                                                                                               #Функция удаляет пост пользователя принимая на вход id поста
    r = requests.delete(base_url + 'post/' + post_id, auth=HTTPBasicAuth('QAtester', '123'))
    status_code = r.status_code
    headers = r.headers
    return status_code, headers
