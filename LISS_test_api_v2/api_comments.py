import requests
from config import Base


class Comments:
    url = Base.BASE_URL_V2
    email = Base.USER_EMAIL

    def post_comments(self, title, text, post_id, auth):
        data = {
            "title": title,
            "text": text,
            "post": post_id
        }
        r = requests.post(self.url + self.email + "/comments", auth=auth, json=data)
        status_code = r.status_code
        body = r.json()
        return status_code, body



