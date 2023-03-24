import requests
from config import Base


class NewUser:
    url = Base.BASE_URL_V1
    email = Base.USER_EMAIL

    def sign_in_new_user(self, username, user_email, password):
        """Метод отправляет запрос на сервер о добавлении нового пользователя в систему, и возвращает
               статус ответа и тело с данными о новом пользователе"""

        data = {
            "username": username,
            "email": user_email,
            "password": password
        }
        r = requests.post(self.url + self.email + "/sign-in", json=data)
        status_code = r.status_code
        body = r.json()

        return status_code, body
