from jsonschema import validate
from data.schemas.scgemas_v2 import POST_SCHEMA


class Validate:
    def array_validation(self, response):
        for item in response:
            validate(item, POST_SCHEMA)

    def validate(self, response):
        validate(response, POST_SCHEMA)
