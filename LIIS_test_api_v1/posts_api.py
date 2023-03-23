import requests
from config import Base


class Posts(Base):
    url = Base.BASE_URL_V1
    email = Base.USER_EMAIL

    """api библиотека для форума"""

    def get_post(self):

        """Метод делает запрос к API сервера и возвращает статус запроса и результат в формате
                      JSON с созданами постами, найденных по email"""

        r = requests.get(self.url + self.email + "/posts")
        status_code = r.status_code
        body = r.json()
        return status_code, body

    def post_posts(self, title, content, auth):

        """Метод отправляет (постит) на сервер данные поста и возвращает статус запроса
                    и результат в формате JSON с данными о добавленном посте"""

        data = {
            "title": title,
            "content": content
        }
        r = requests.post(self.url + self.email + "/posts", auth=auth, json=data)
        status_code = r.status_code
        body = r.json()
        return status_code, body

    def get_new_post(self, post_id):

        """Метод делает запрос к API сервера и возвращает статус запроса и результат в формате
                      JSON с созданным постом, найденных по id"""

        r = requests.get(self.url + self.email + "/post/" + post_id)
        status_code = r.status_code
        body = r.json()
        return status_code, body

    def put_post(self, post_id, title, content, auth):

        """Метод отправляет запрос на сервер о обновлении данных поста найденного по id
        и возвращает статус запроса и результат в формате JSON с данными уведомлениями о успешном обновлении"""

        data = {
            "title": title,
            "content": content
        }
        r = requests.put(self.url + self.email + '/post/' + post_id, auth=auth, json=data)
        status_code = r.status_code
        body = r.json()
        return status_code, body

    def delete_post(self, post_id, auth):

        """Метод отправляет на сервер запрос на удаление поста по указанному ID и возвращает
                статус запроса и результат в формате JSON с текстом уведомления о успешном удалении"""

        r = requests.delete(self.url + self.email + '/post/' + post_id, auth=auth)
        status_code = r.status_code
        return status_code
