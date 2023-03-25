from LISS_test_api_v2.api_posts import Posts
from requests.auth import HTTPBasicAuth
from config import Base, GlobalErrorMessages
from generator.generator import generate_random_string, generate_random_id


class TestPosts(Posts):
    auth_user = HTTPBasicAuth(Base.USER_NAME, Base.USER_PASSWORD)
    auth_admin = HTTPBasicAuth(Base.USER_NAME_ADMIN, Base.USER_PASSWORD_ADMIN)
    auth_user_incorrect_pass = HTTPBasicAuth(Base.USER_EMAIL, Base.INCORRECT_PASSWORD)

    def test_get_posts(self):
        """ Проверяем что  на запрос о получении данных о всех постах пользователя возвращается
            не пустой список и статус кода 200, а так же возвращаем id последего поста.
            В случае если список равен нулю, отправляем запрос на создание поста"""

        status_code, body = self.get_posts()
        if len(body) == 0:
            self.test_post_posts_user()
            status_code, body = self.get_posts()
            assert status_code == 200, GlobalErrorMessages.WRONG_STATUS_CODE.value
            assert len(body) > 0, GlobalErrorMessages.WRONG_QUANTITY.value
            return str(body[-1]['id'])
        else:
            assert status_code == 200, GlobalErrorMessages.WRONG_STATUS_CODE.value
            assert len(body) > 0, GlobalErrorMessages.WRONG_QUANTITY.value
            return str(body[-1]['id'])

    def test_post_posts_user(self):
        """ Проверяем что  при отправке запроса на сервер с авторизацией существующего польователя
            о добавлении поста  возвращается статус кода 201, а так же заголовок и тело поста
            идентичные с отправленными"""

        name = generate_random_string(5)
        content = generate_random_string(12)
        status_code, body = self.post_post(name, content, self.auth_user)
        assert status_code == 201, GlobalErrorMessages.WRONG_STATUS_CODE.value
        assert body["name"] == name, GlobalErrorMessages.WRONG_BODY.value
        assert body["content"] == content, GlobalErrorMessages.WRONG_BODY.value

    def test_get_post_user(self):
        """ Проверяем что  на запрос о получении данных о посте  пользователя найденого по id возвращается
            статус кода 200 и id поста в теле ответа идентичен с id по которому осуществлялся поиск"""

        post_id = self.test_get_posts()
        status_code, body = self.get_post(post_id)
        assert status_code == 200, GlobalErrorMessages.WRONG_STATUS_CODE.value
        assert body["id"] == int(post_id), GlobalErrorMessages.WRONG_BODY.value

    def test_put_post_user(self):
        """ Проверяем что  на запрос о обнавление данных в посте пользователя, найденого по id поста, возвращается
            статус кода 200 и в теле ответа содержатся данные о успешном обновлении поста"""

        update_title = generate_random_string(4)
        update_content = generate_random_string(10)
        post_id = self.test_get_posts()
        status_code, body = self.put_post(post_id, update_title, update_content, self.auth_user)
        assert status_code == 200, GlobalErrorMessages.WRONG_STATUS_CODE.value
        assert body["message"] == "updated", GlobalErrorMessages.WRONG_BODY.value

    def test_delete_post_user(self):
        """ Проверяем что при отправке запроса на удаление поста найденного по id, возвращается статус кода 204"""

        post_id = self.test_get_posts()
        status_code, headers = self.delete_post(post_id, self.auth_user)
        assert status_code == 204
        assert headers["Content-Type"] == "application/json"

    def test_get_post_pagination(self):
        """
                    """

        numbers_page = "2"
        status_code, body = self.get_post_pagination(numbers_page)
        assert status_code == 200

    def test_put_post_admin(self):
        """
                    """

        update_title = generate_random_string(4)
        update_content = generate_random_string(10)
        post_id = self.test_get_posts()
        status_code, body = self.put_post(post_id, update_title, update_content, self.auth_admin)
        assert status_code == 200, GlobalErrorMessages.WRONG_STATUS_CODE.value
        assert body["message"] == "updated", GlobalErrorMessages.WRONG_BODY.value

    def test_delete_post_admin(self):

        """           """

        post_id = self.test_get_posts()
        status_code, headers = self.delete_post(post_id, self.auth_admin)
        assert status_code == 204
        assert headers["Content-Type"] == "application/json"

    def test_post_posts_invalid_user(self):
        """ Проверяем что  при отправке запроса на сервер с авторизацией польователя с неверным паролем
            о добавлении поста возвращается статус кода 401, возвразщается обработанная ошибка с описанием """

        title = generate_random_string(4)
        content = generate_random_string(10)
        status_code, body = self.post_post(title, content, self.auth_user_incorrect_pass)
        assert status_code == 401
        assert body["message"] == "Could not verify your login!"

    def test_put_post_invalid_user(self):
        """ Проверяем что запроса на сервер с авторизацией польователя с неверным паролем
            о обновлении поста возвращается статус кода 401, возвразщается обработанная ошибка с описанием """

        update_title = generate_random_string(4)
        update_content = generate_random_string(10)
        post_id = self.test_get_posts()
        status_code, body = self.put_post(post_id, update_title, update_content, self.auth_user_incorrect_pass)
        assert status_code == 401
        assert body["message"] == "Could not verify your login!"

    def test_delete_post_invalid_user(self):
        """ Проверяем что при отправке запроса на удаление поста найденного по id,
            пользователем с непраильныим паролем, возвращается статус кода 401"""
        post_id = self.test_get_posts()
        status_code, headers = self.delete_post(post_id, self.auth_user_incorrect_pass)
        assert status_code == 401
        assert headers["Content-Type"] == "application/json"

    def test_put_non_existent_post(self):
        """ Проверяем что  на запрос о обнавление данных в несуществующем посте c авторизацией пользователя,
            возвращается статус кода 404 и в теле ответа содержатся данные о ошибке"""

        update_title = generate_random_string(4)
        update_content = generate_random_string(10)
        status_code, body = self.put_post(generate_random_id(), update_title, update_content, self.auth_user)
        assert status_code == 404, GlobalErrorMessages.WRONG_STATUS_CODE.value
        assert body["message"] == "Post not found", GlobalErrorMessages.WRONG_VALIDATION.value

    def test_delete_non_existent_post(self):
        """ Проверяем что  на запрос о удалении несуществующего поста с авторизацией модератора
            возвращается статус кода 404"""

        status_code, headers = self.delete_post(generate_random_id(), self.auth_admin)
        assert status_code == 404, GlobalErrorMessages.WRONG_STATUS_CODE.value
        assert headers["Content-Type"] == "application/json"