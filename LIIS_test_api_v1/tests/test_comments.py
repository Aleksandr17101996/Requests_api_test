from LIIS_test_api_v1.api_comments import get_comments, post_comment


def test_get_comments():
    status_code, body = get_comments()
    print(body)
    assert status_code == 200, "Статус кода не соответсвует"
    assert len(body) >= 0, "Колличество коментариев больше нуля"

def test_post_comment():
    post = "123"
    status_code, body = post_comment("ЗаголовокКоментария", "КонтентКоментария", post)
    print(status_code, body)
