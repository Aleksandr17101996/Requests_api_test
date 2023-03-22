import requests
from config import Base


class GrantUserAdminRole:
    url = Base.BASE_URL_V2
    email = Base.USER_EMAIL

    def put_admin_rights_user(self, user_id, auth):
        data = {
            "user_id": user_id
        }
        r = requests.put(self.url + self.email + "/make_admin", auth=auth, json=data)
        status_code = r.status_code
        body = r.json()
        return status_code, body
