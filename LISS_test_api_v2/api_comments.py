import requests
from config import Base


class Comments:
    url = Base.BASE_URL_V2
    email = Base.USER_EMAIL

    """Библиотека api для работы с комментариями к постам форума"""

    def post_comment(self, title, text, post_id, auth):
        """Метод отправляет (постит) на сервер коменнтарий к посту найденного по id и возвращает статус запроса
                     и результат в формате JSON с данными о добавленном комментарии"""

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
        """Метод делает запрос на сервера и возвращает статус запроса и результат в формате
                        JSON с добавленными коментариями пользователя, найденных по email"""

        r = requests.get(self.url + self.email + "/comments")
        status_code = r.status_code
        body = r.json()
        return status_code, body

    def get_comment(self, id_comment):
        """Метод делает запрос к API сервера и возвращает статус запроса и результат в формате
                                      JSON с добавленным комментарием, найденного по id"""

        r = requests.get(self.url + self.email + "/comment" + id_comment)
        status_code = r.status_code
        body = r.json()
        return status_code, body

    def put_comment(self, id_comment, title, text, auth):
        """Метод отправляет запрос на сервер о обновлении данных комментария к посту найденного по id
        и возвращает статус запроса и результат в формате JSON с данными уведомлениями о успешном обновлении"""

        data = {
            "title": title,
            "text": text
        }
        r = requests.put(self.url + self.email + "/comment/" + id_comment, auth=auth, json=data)
        status_code = r.status_code
        body = r.json()
        return status_code, body

    def get_comments_pagination(self, number_page):
        """Метод делает запрос к API сервера и возвращает статус запроса и результат в формате
            JSON с добавленным комментариями пользователя найденных по емайл на выбранной странице , """

        params = {
            "page": number_page
        }
        r = requests.get(self.url + self.email + "/comments", params=params)
        status_code = r.status_code
        body = r.json()
        return status_code, body

    def delete_comment(self, id_comment, auth):
        """Метод отправляет на сервер запрос на удаление комментария к посту по указанному ID и возвращает
                                статус запроса и результат в формате JSON с текстом уведомления о успешном удалении"""

        r = requests.delete(self.url + self.email + "/comment/" + id_comment, auth=auth)
        status_code = r.status_code
        body = r.json()
        return status_code, body
