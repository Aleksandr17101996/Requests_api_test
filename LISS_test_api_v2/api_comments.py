import requests
from config import Base


class Comments:
    url = Base.BASE_URL_V2
    email = Base.USER_EMAIL

    def post_comment(self, title, text, post_id, auth):
        data = {
            "title": title,
            "text": text,
            "post": post_id
        }
        r = requests.post(self.url + self.email + "/comments", auth=auth, json=data)
        status_code = r.status_code
        body = r.json()
        return status_code, body

    def get_comments(self):
        r = requests.get(self.url + self.email + "/comments")
        status_code = r.status_code
        body = r.json()
        return status_code, body

    def get_comment(self, id_comment):
        r = requests.get(self.url + self.email + "/comment" + id_comment)
        status_code = r.status_code
        body = r.json()
        return status_code, body

    def put_comment(self, id_comment, title, text, auth):
        data = {
            "title": title,
            "text": text
        }
        r = requests.put(self.url + self.email + "/comment/" + id_comment, auth=auth, json=data)
        status_code = r.status_code
        body = r.json()
        return status_code, body





