from LISS_test_api_v2.api_posts import Posts
from requests.auth import HTTPBasicAuth
from config import Base, GlobalErrorMessages
from generator.generator import generate_random_string


class TestPosts(Posts):
    auth_user = HTTPBasicAuth(Base.USER_NAME, Base.USER_PASSWORD)
    auth_admin = HTTPBasicAuth(Base.USER_NAME_ADMIN, Base.USER_PASSWORD_ADMIN)
    auth_user_incorrect_pass = HTTPBasicAuth(Base.USER_EMAIL, Base.INCORRECT_PASSWORD)

    def test_post_posts(self):
        """ Проверяем что  при отправке запроса на сервер с авторизацией существующего польователя
            о добавлении поста  возвращается статус кода 201, а так же заголовок и тело поста
            идентичные с отправленными"""

        name = generate_random_string(5)
        content = generate_random_string(12)
        status_code, body = self.post_post(name, content, self.auth_user)
        assert status_code == 201, GlobalErrorMessages.WRONG_STATUS_CODE.value
        assert body["name"] == name, GlobalErrorMessages.WRONG_BODY.value
        assert body["content"] == content, GlobalErrorMessages.WRONG_BODY.value
