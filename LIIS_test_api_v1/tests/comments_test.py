from LIIS_test_api_v1.comments_api import Comments
from config import Base, GlobalErrorMessages
from requests.auth import HTTPBasicAuth
from LIIS_test_api_v1.tests.posts_test import TestPosts
from generator.generator import generate_random_string, generate_random_id
from jsonschema import validate

tp = TestPosts()


class TestComments(Comments):
    auth_user = HTTPBasicAuth(Base.USER_NAME, Base.USER_PASSWORD)
    auth_user_incorrect_pass = HTTPBasicAuth(Base.USER_EMAIL, Base.INCORRECT_PASSWORD)
    post_id = tp.test_get_posts()

    def test_get_comments(self):
        """ Проверяем что  на запрос о получении данных о всех комментариях пользователя возвращается
            не пустой список и статус кода 200, а так же возвращаем id последего комментария.
            В случае если список равен нулю, отправляем запрос на создание комментария"""

        status_code, body = self.get_comments()
        if len(body) == 0:
            self.test_post_comments()
            status_code, body = self.get_comments()
            assert status_code == 200, GlobalErrorMessages.WRONG_STATUS_CODE.value
            assert len(body) > 0, GlobalErrorMessages.WRONG_QUANTITY.value
            return str(body[-1]['id'])
        else:
            assert status_code == 200, GlobalErrorMessages.WRONG_STATUS_CODE.value
            assert len(body) > 0, GlobalErrorMessages.WRONG_QUANTITY.value
            return str(body[-1]['id'])

    def test_post_comments(self):
        """ Проверяем что  при отправке запроса на сервер с авторизацией существующего польователя
            о добавлении комментария к посту найденного по id,  возвращается статус кода 201,
            а так же заголовок и тело комментария идентичные с отправленными"""

        title = generate_random_string(5)
        content = generate_random_string(12)
        post_id = self.post_id
        status_code, body = self.posts_comment(title, content, post_id, self.auth_user)
        assert status_code == 201, GlobalErrorMessages.WRONG_STATUS_CODE.value
        assert body["title"] == title, GlobalErrorMessages.WRONG_BODY.value
        assert body["content"] == content, GlobalErrorMessages.WRONG_BODY.value
    def test_get_comment(self):
        """ Проверяем что  на запрос о получении данных о комментарии найденого по id возвращается
            статус кода 200 и id поста в теле ответа идентичен с id по которому осуществлялся поиск"""

        comment_id = self.test_get_comments()
        status_code, body = self.get_comment(comment_id)
        assert status_code == 200, GlobalErrorMessages.WRONG_STATUS_CODE.value
        assert body["id"] == int(comment_id), GlobalErrorMessages.WRONG_BODY.value

    def test_put_comment(self):
        """ Проверяем что  на запрос о обнавление данных в комментарии, найденого по id поста, возвращается
            статус кода 200 и в теле ответа содержатся данные о успешном обновлении комментария"""

        comment_id = self.test_get_comments()
        title = generate_random_string(5)
        content = generate_random_string(12)
        status_code, body = self.put_comment(comment_id, title, content, self.auth_user)
        assert status_code == 200, GlobalErrorMessages.WRONG_STATUS_CODE.value
        assert body["message"] == "updated", GlobalErrorMessages.WRONG_BODY.value

    def test_delete_comment(self):
        """ Проверяем что при отправке запроса на удаление комментария найденного по id, возвращается статус кода 204"""

        comment_id = self.test_get_comments()
        status_code, headers = self.delete_comment(comment_id, self.auth_user)
        assert status_code == 204, GlobalErrorMessages.WRONG_STATUS_CODE.value
        assert headers["Content-Type"] == "application/json", GlobalErrorMessages.WRONG_HEADERS.value

    def test_post_comment_someone_else_post(self):
        """ Проверяем что  при отправке запроса на сервер с авторизацией существующего польователя
            о добавлении комментария к несуществующему посту,  возвращается статус кода 404,
            и в теле ответа обработтаное описание ошибки  """

        title = generate_random_string(5)
        content = generate_random_string(12)
        status_code, body = self.posts_comment(title, content, generate_random_id(), self.auth_user)
        assert status_code == 404, GlobalErrorMessages.WRONG_STATUS_CODE.value
        assert body["message"] == "Post not found", GlobalErrorMessages.WRONG_VALIDATION.value

    def test_post_comment_invalid_user(self):
        """ Проверяем что  при отправке запроса на сервер с авторизацией польователя имеющего неправильный пароль
            о добавлении комментария к посту найденного по id,  возвращается статус кода 401,
            а так же тело ответа содержит информацию о обработанной ошибке"""

        title = generate_random_string(5)
        content = generate_random_string(12)
        post_id = self.post_id
        status_code, body = self.posts_comment(title, content, post_id, self.auth_user_incorrect_pass)
        assert status_code == 401, GlobalErrorMessages.WRONG_STATUS_CODE.value
        assert body["message"] == "Could not verify your login!", GlobalErrorMessages.WRONG_VALIDATION.value

    def test_put_comment_invalid_user(self):
        """ Проверяем что  на запрос о обнавление данных в комментарии, найденого по id поста,
            пользователем имеющего неправильныцй пароль, возвращается статус кода 401,
            а так же тело ответа содержит информацию о обработанной ошибке"""

        comment_id = self.test_get_comments()
        title = generate_random_string(5)
        content = generate_random_string(12)
        status_code, body = self.put_comment(comment_id, title, content, self.auth_user_incorrect_pass)
        assert status_code == 401, GlobalErrorMessages.WRONG_STATUS_CODE.value
        assert body["message"] == "Could not verify your login!", GlobalErrorMessages.WRONG_VALIDATION.value

    def test_delete_comment_invalid_user(self):
        """ Проверяем что при отправке запроса на удаление комментария найденного по id,
            пользователем имеющего неправильный пароль, возвращается статус кода 401"""

        comment_id = self.test_get_comments()
        status_code, headers = self.delete_comment(comment_id, self.auth_user_incorrect_pass)
        assert status_code == 401, GlobalErrorMessages.WRONG_STATUS_CODE.value
        assert headers["Content-Type"] == "application/json", GlobalErrorMessages.WRONG_HEADERS.value

    def test_put_non_existent_comment(self):
        """ Проверяем что  на запрос о обнавление данных в несуществующем комментарии,
            возвращается статус кода 404 и в теле ответа содержатся данные о ошибке"""

        title = generate_random_string(5)
        content = generate_random_string(12)
        status_code, body = self.put_comment(generate_random_id(), title, content, self.auth_user)
        assert status_code == 404, GlobalErrorMessages.WRONG_STATUS_CODE.value
        assert body["message"] == "Comment not found", GlobalErrorMessages.WRONG_VALIDATION

    def test_delete_non_existent_comment(self):
        """ Проверяем что при отправке запроса на удаление несуществующего комментария
            возвращается статус кода 404"""

        status_code, headers = self.delete_comment(generate_random_id(), self.auth_user)
        assert status_code == 404, GlobalErrorMessages.WRONG_STATUS_CODE.value
        assert headers["Content-Type"] == "application/json", GlobalErrorMessages.WRONG_HEADERS.value
