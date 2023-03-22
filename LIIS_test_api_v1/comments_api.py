import requests
from config import Base


class Comments(Base):
    url = Base.BASE_URL_V1
    email = Base.USER_EMAIL

    def get_comments(self):
        r = requests.get(self.url + self.email + "/comments")
        status_code = r.status_code
        body = r.json()
        return status_code, body

    def posts_comment(self, title, content, post_id, auth):
        data = {
            "title": title,
            "content": content,
            "post": post_id
        }
        r = requests.post(self.url + self.email + "/comments", auth=auth, json=data)
        status_code = r.status_code
        body = r.json()
        return status_code, body

    def get_comment(self, id_comment):
        r = requests.get(self.url + self.email + "/comment/" + id_comment)
        status_code = r.status_code
        body = r.json()
        return status_code, body

    def put_comment(self, id_comment, title, content, auth):
        data = {
            "title": title,
            "content": content
        }
        r = requests.put(self.url + self.email + "/comment/" + id_comment, auth=auth, json=data)
        status_code = r.status_code
        body = r.json()
        return status_code, body

    def delete_comment(self, id_comment, auth):
        r = requests.delete(self.url + self.email + id_comment, auth=auth)
        status_code = r.status_code
        headers = r.headers
        return status_code, headers



