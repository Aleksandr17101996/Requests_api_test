import requests
from requests.auth import HTTPBasicAuth

email = 'qatester@mail.com'
base_url = f"https://hr.recruit.liis.su/qa0/v1/api/{email}/"



def get_comments():
    r = requests.get(base_url + "comments")
    status_code = r.status_code
    body = r.json()
    return status_code, body


def post_comment(title, content, post):
    data = {
        "title": title,
        "content": content,
        "post": post
    }
    r = requests.post(base_url + "comments", auth=HTTPBasicAuth('QAtester', '123'), json=data)
    status_code = r.status_code
    body = r.json()
    return status_code, body


def get_comment(id_comment):
    r = requests.get(base_url + "comment/" + id_comment)
    status_code = r.status_code
    body = r.json()
    return status_code, body


def put_comment(id_comment, title, content):
    data = {
        "title": title,
        "content": content
    }
    r = requests.put(base_url + "comment/" + id_comment, auth=HTTPBasicAuth('QAtester', '123'), json=data)
    status_code = r.status_code
    body = r.json()
    return status_code, body


def delete_comment(id_comment):
    r = requests.delete(base_url + "comment/" + id_comment, auth=HTTPBasicAuth('QAtester', '123'))
    status_code = r.status_code
    body = r.json()
    return status_code, body
