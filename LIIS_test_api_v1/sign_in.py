import requests

email = 'qatester@mail.com'
base_url = f"https://hr.recruit.liis.su/qa0/v1/api/{email}/"


def sign_in_new_user(username, user_email, password):                                                                   #Функция регистрации нового пользователя, принимает на вход имя, емайл, пароль и возвращает id пользователя.
    data = {
        "username": username,
        "email": user_email,
        "password": password
    }
    r = requests.post(base_url + "sign-in", json=data)
    status_code = r.status_code
    body = r.json()
    user_id = body["id"]
    return status_code, user_id
