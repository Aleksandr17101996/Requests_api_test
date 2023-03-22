from LIIS_test_api_v1.comments_api import Comments
from config import Base
from requests.auth import HTTPBasicAuth


class TestComments(Comments):
    auth_user = HTTPBasicAuth(Base.USER_NAME, Base.USER_PASSWORD)

    def test_get_comments(self):
        status_code, body = self.get_comments()
        id_comment = body["id"]
        assert status_code == 200, "Статус кода не соответсвует"
        assert len(body) >= 0
        return id_comment

    def test_post_comments(self):
        title = "Это заголовок коментария"
        content = "Это текст коментария из python"
        post_id = "8645"
        status_code, body = self.posts_comment(title, content, post_id, self.auth_user)
        assert status_code == 201, "Статус кода не соответсвует"
        assert body["title"] == title
        assert body["content"] == content

    def test_get_comment(self):
        post_id = self.test_get_comments()
        status_code, body = self.get_comment(post_id)
        assert status_code == 200, "Статус кода не соответсвует"
        assert "title" in body
