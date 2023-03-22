from LIIS_test_api_v1.posts_api import Posts
from config import Base
from requests.auth import HTTPBasicAuth


class TestPosts(Posts):
    auth_user = HTTPBasicAuth(Base.USER_NAME, Base.USER_PASSWORD)

    def test_get_posts(self):
        status_code, body = self.get_post()
        last_id = body[-1]['id']
        assert status_code == 200, "Статус кода не соответсвует"
        assert len(body) >= 0, "Посты не найдены"
        return str(last_id)

    def test_post_posts(self):
        title = "Заголовок поста"
        content = "Контент поста"
        status_code, body = self.post_posts(title, content, self.auth_user)
        assert status_code == 201, "Статус кода не соответсвует"
        assert body["title"] == title, "Заголовок поста в теле ответа не верен"
        assert body["content"] == content, "Контент поста не верен"

    def test_get_new_post(self):
        post_id = self.test_get_posts()
        status_code, body = self.get_new_post(post_id)
        assert status_code == 200, "Статус кода не соответсвует"
        assert body["id"] == int(post_id), "Тело ответа имеет не верный id"

    def test_put_post(self):
        update_title = "Обновленный заголовок поста"
        update_content = "Обновленный контент поста"
        post_id = self.test_get_posts()
        status_code, body = self.put_post(post_id, update_title, update_content, self.auth_user)
        assert status_code == 200, "Статус кода не соответсвует"
        assert body["message"] == "updated", "Содержимое заголовка не обновилось"

    def test_delete_post(self):
        post_id = self.test_get_posts()
        status_code = self.delete_post(post_id, self.auth_user)
        assert status_code == 204, "Статус кода не соответсвует"
