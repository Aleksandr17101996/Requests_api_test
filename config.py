from enum import Enum


class Base:
    BASE_URL_V1 = f"https://hr.recruit.liis.su/qa0/v1/api/"
    BASE_URL_V2 = f"https://hr.recruit.liis.su/qa0/v2/api/"
    USER_NAME_ADMIN = "admin"
    USER_PASSWORD_ADMIN = "123"
    USER_NAME = "QAtester"
    USER_PASSWORD = "123"
    USER_EMAIL = "qatester@mail.com"
    INCORRECT_PASSWORD = "012"


class GlobalErrorMessages(Enum):
    WRONG_STATUS_CODE = "Полученный статус код не равен ожидаемому"
    WRONG_QUANTITY = "Колличество записей в ответе не соответсвует ожидаемому"
    WRONG_BODY = "Содержимое в теле ответа не соответсвует ожидаемому"
