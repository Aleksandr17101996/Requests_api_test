import requests
from config import Base


class Posts:
    url = Base.BASE_URL_V2
    email = Base.USER_EMAIL

    """Библиотека api для работы с постами форума"""

    def get_post_pagination(self, number_page):
        params = {'page': number_page}
        r = requests.get(self.url + self.email + "/posts", params=params)
        status_code = r.status_code
        body = r.json()
        return status_code, body

    def get_posts(self):
        """Метод делает запрос к API сервера и возвращает статус запроса и результат в формате
           JSON с созданами постами, найденных по email"""

        r = requests.get(self.url + self.email + "/posts")
        status_code = r.status_code
        body = r.json()
        return status_code, body

    def post_post(self, name, content, auth):
        """Метод отправляет (постит) на сервер данные поста и возвращает статус запроса
           и результат в формате JSON с данными о добавленном посте"""

        data = {
            "name": name,
            "content": content
        }
        r = requests.post(self.url + self.email + "/posts", auth=auth, json=data)
        status_code = r.status_code
        body = r.json()
        return status_code, body

    def get_post(self, post_id):
        """Метод делает запрос к API сервера и возвращает статус запроса и результат в формате
           JSON с созданным постом, найденных по id"""

        r = requests.get(self.url + self.email + "/post/" + post_id)
        status_code = r.status_code
        body = r.json()
        return status_code, body

    def put_post(self, post_id, name, content, auth):
        """Метод отправляет запрос на сервер о обновлении данных поста найденного по id
           и возвращает статус запроса и результат в формате JSON с данными уведомлениями о успешном обновлении"""

        data = {
            "name": name,
            "content": content
        }
        r = requests.put(self.url + self.email + "/post/" + post_id, auth=auth, json=data)
        status_code = r.status_code
        body = r.json()
        return status_code, body

    def delete_post(self, post_id, auth):
        """Метод отправляет на сервер запрос на удаление поста по указанному ID и возвращает
           статус запроса и результат в формате JSON с текстом уведомления о успешном удалении"""

        r = requests.delete(self.url + self.email + "/post/" + post_id, auth=auth)
        status_code = r.status_code
        headers = r.headers
        return status_code, headers







