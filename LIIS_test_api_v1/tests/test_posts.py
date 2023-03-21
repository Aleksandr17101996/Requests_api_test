from LIIS_test_api_v1.api_posts import get_posts, post_posts, get_new_posts, delete_post


#
def last_post_id():  # Функция находит и возвращает id последнего поста
    __, body = get_posts()
    last_id = body[-1]['id']
    return last_id


def test_get_posts():
    status, body = get_posts()
    assert status == 200, "Response code does not match"
    assert len(body) >= 0, "The number of posts is not equal to zero"


def test_post_posts():
    status, result = post_posts("Тратата", "Тутуту")
    assert status == 201, "Response code does not match"
    assert 'id' in result, "Response body does not contain id"


def test_get_new_posts():
    post_id = last_post_id()
    status_code, body = get_new_posts(str(post_id))
    assert status_code == 200, "Response code does not match"
    assert "id" in body, "Response body does not contain id"


def test_delete_post():
    post_id = last_post_id()
    status_code, headers = delete_post(str(post_id))
    assert status_code == 204
    assert 'Content-Type' in headers
