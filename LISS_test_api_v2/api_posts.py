import requests
from config import Base


class Posts:
    url = Base.BASE_URL_V2
    email = Base.USER_EMAIL

    def get_post_pagination(self, number_page):
        params = {
            "page": number_page
        }
        r = requests.get(self.url + self.email + "/posts", params=params)
        status_code = r.status_code
        body = r.json()
        assert status_code, body

    def get_posts(self):
        r = requests.get(self.url + self.email + "/posts")
        status_code = r.status_code
        body = r.json()
        return status_code, body