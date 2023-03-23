from LIIS_test_api_v1.comments_api import Comments
from config import Base
from requests.auth import HTTPBasicAuth
from LIIS_test_api_v1.tests.posts_test import TestPosts

tp = TestPosts()


class TestComments(Comments):
    auth_user = HTTPBasicAuth(Base.USER_NAME, Base.USER_PASSWORD)
    post_id = tp.test_get_posts()

    def test_get_comments(self):
        status_code, body = self.get_comments()
        id_comment = body[-1]['id']
        assert status_code == 200, "Статус кода не соответсвует"
        assert len(body) >= 0
        return str(id_comment)

    def test_post_comments(self):
        title = "Это заголовок коментария"
        content = "Это текст коментария из python"
        post_id = self.post_id
        status_code, body = self.posts_comment(title, content, post_id, self.auth_user)
        assert status_code == 201, "Статус кода не соответсвует"
        assert body["title"] == title
        assert body["content"] == content

    def test_get_comment(self):
        comment_id = self.test_get_comments()
        status_code, body = self.get_comment(comment_id)
        assert status_code == 200, "Статус кода не соответсвует"
        assert "title" in body

    def test_put_comment(self):
        comment_id = self.test_get_comments()
        title = "Это обновленный заголовок комментария!"
        content = "Это обновленный текст комментария!"
        status_code, body = self.put_comment(comment_id, title, content, self.auth_user)
        assert status_code == 200, "Статус кода не соответсвует"
        assert body["message"] == "updated"

    def test_delete_comment(self):
        comment_id = self.test_get_comments()
        status_code, headers = self.delete_comment(comment_id, self.auth_user)
        assert status_code == 204, "Статус кода не соответсвует"
        assert headers["Content-Type"] == "application/json"
