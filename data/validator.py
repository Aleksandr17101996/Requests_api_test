from jsonschema import validate
from data.schemas.schemas_v2 import POST_SCHEMA, COMMENT_SCHEMA, NEW_USER_SCHEMA


class ValidatePost:
    def array_validation(self, response):
        for item in response:
            validate(item, POST_SCHEMA)

    def dict_validation(self, response):
        validate(response, POST_SCHEMA)


class ValidateComment:
    def array_validation(self, response):
        for item in response:
            validate(item, COMMENT_SCHEMA)

    def dict_validation(self, response):
        validate(response, COMMENT_SCHEMA)


class ValidateNewUser:

    def user_validation(self, response):
        validate(response, NEW_USER_SCHEMA)
