import requests
from config import Base


class AddNewUser:
    url = Base.BASE_URL_V2
    email = Base.USER_EMAIL

    def sign_in_new_user(self, user_name, email, password, first_name, middle_name, last_name):


        data = {
            "username": user_name,
            "email": email,
            "password": password,
            "first_name": first_name,
            "middle_name": middle_name,
            "last_name": last_name
        }
        r = requests.post(self.url + self.email + "/sign-in", json=data)
        status_code = r.status_code
        body = r.json()
        return status_code, body
