from LIIS_test_api_v1.posts_api import Posts
from config import Base
from requests.auth import HTTPBasicAuth


class TestPosts(Posts):
    auth_user = HTTPBasicAuth(Base.USER_NAME, Base.USER_PASSWORD)
    auth_user_incorrect_pass = HTTPBasicAuth(Base.USER_EMAIL, Base.INCORRECT_PASSWORD)

    def test_get_posts(self):
        """ Проверяем что  на запрос о получении данных о всех постах пользователя возвращается
         не пустой список и статус кода 200, а так же возвращаем id последего поста.
                В случае если список равен нулю, отправляем запрос на создание поста"""

        status_code, body = self.get_post()
        if len(body) == 0:
            self.test_post_posts()
            status_code, body = self.get_post()
            assert status_code == 200, "Статус кода не соответсвует ожидаемому"
            assert len(body) > 0, "В списке нет добавленных постов"
            return str(body[-1]['id'])
        else:
            assert status_code == 200, "Статус кода не соответсвует ожидаемому"
            assert len(body) > 0, "В списке нет добавленных постов"
            return str(body[-1]['id'])

    def test_post_posts(self):
        """ Проверяем что  при отправке запроса на сервер с авторизацией существующего польователя
               о добавлении поста  возвращается статус кода 201, а так же заголовок и тело поста
               идентичные с отправленными"""

        title = "Заголовок поста"
        content = "Тело поста"
        status_code, body = self.post_posts(title, content, self.auth_user)
        assert status_code == 201, "Статус кода не соответсвует ожидаемому"
        assert body["title"] == title, "Заголовок поста в теле ответа не идентичен отправленному"
        assert body["content"] == content, "Тело поста в ответе не идентичен отправленному"

    def test_get_new_post(self):
        """ Проверяем что  на запрос о получении данных о посте  пользователя найденого по id возвращается
                 статус кода 200 и id поста в теле ответа идентичен с id по которому осуществлялся поиск"""

        post_id = self.test_get_posts()
        status_code, body = self.get_new_post(post_id)
        assert status_code == 200, "Статус кода не соответсвует ожидаемому"
        assert body["id"] == int(post_id), "Тело ответа имеет id который не соответсвует ожидаемому"

    def test_put_post(self):
        """ Проверяем что  на запрос о обнавление данных в посте пользователя, найденого по id поста, возвращается
                         статус кода 200 и в теле ответа содержатся данные о успешном обновлении поста"""

        update_title = "Обновленный заголовок поста"
        update_content = "Обновленное тело поста"
        post_id = self.test_get_posts()
        status_code, body = self.put_post(post_id, update_title, update_content, self.auth_user)
        assert status_code == 200, "Статус кода не соответсвует ожидаемому"
        assert body["message"] == "updated", "Содержимое поста не обновилось"

    def test_delete_post(self):
        """ Проверяем что при отправке запроса на удаление поста найденного по id, возвращается статус кода 204"""

        post_id = self.test_get_posts()
        status_code = self.delete_post(post_id, self.auth_user)
        assert status_code == 204, "Статус кода не соответсвует ожидаемому"

    def test_post_posts_invalid_user(self):
        """ Проверяем что  при отправке запроса на сервер с авторизацией польователя с неверным паролем
         о добавлении поста возвращается статус кода 401, возвразщается обработанная ошибка с описанием """

        title = "Заголовок поста(неправильный пароль)"
        content = "Текст поста(неправильный пароль)"
        status_code, body = self.post_posts(title, content, self.auth_user_incorrect_pass)
        assert status_code == 401, "Статус кода не соответсвует ожидаемому"
        assert body["message"] == "Could not verify your login!", "Ошибка не обработана"

    def test_put_post_invalid_user(self):
        """ Проверяем что запроса на сервер с авторизацией польователя с неверным паролем
                 о обновлении поста возвращается статус кода 401, возвразщается обработанная ошибка с описанием """

        update_title = "Обновленный заголовок поста(Неправильный пароль)"
        update_content = "Обновленное тело поста(Неправильный пароль)"
        post_id = self.test_get_posts()
        status_code, body = self.put_post(post_id, update_title, update_content, self.auth_user_incorrect_pass)
        assert status_code == 401, "Статус кода не соответсвует ожидаемому"
        assert body["message"] == "Could not verify your login!", "Ошибка не обработана"

    def test_delete_post_invalid_user(self):
        """ Проверяем что при отправке запроса на удаление поста найденного по id,
            пользователем с непраильныим паролем, возвращается статус кода 401"""
        post_id = self.test_get_posts()
        status_code = self.delete_post(post_id, self.auth_user_incorrect_pass)
        assert status_code == 401, "Статус кода не соответсвует ожидаемому"

