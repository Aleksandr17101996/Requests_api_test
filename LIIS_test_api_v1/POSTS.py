import requests
from config import Base


class Posts(Base):
    url = Base.BASE_URL_V1
    email = Base.USER_EMAIL

    def get_post(self):
        r = requests.get(self.url + self.email + "/posts")
        status_code = r.status_code
        body = r.json()
        return status_code, body

    def post_posts(self, title, content, auth):
        data = {
            "title": title,
            "content": content
        }
        r = requests.post(self.url + self.email + "/posts", auth=auth, json=data)
        status_code = r.status_code
        body = r.json()
        return status_code, body

    def get_new_post(self, post_id):
        r = requests.get(self.url + self.email + "/post/" + post_id)
        status_code = r.status_code
        body = r.json()
        return status_code, body

    def put_post(self, post_id, title, content, auth):
        data = {
            "title": title,
            "content": content
        }
        r = requests.put(self.url + self.email + '/post/' + post_id, auth=auth, json=data)
        status_code = r.status_code
        body = r.json()
        return status_code, body

    def delete_post(self, post_id, auth):
        r = requests.delete(self.url + self.email + '/post/' + post_id, auth=auth)
        status_code = r.status_code
        return status_code
