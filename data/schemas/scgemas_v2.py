POST_SCHEMA = {
    "type": "object",
    "properties": {
        "id": {"type": "number"},
        "name": {"type": "string"},
        "content": {"type": "string"},
        "author": {"type": "number"},
        "publication_datetime": {"type": "string"}
    },
    "required": ["id", "name", "content", "author"]
}

COMMENT_SCHEMA = {
    "type": "object",
    "properties": {
        "id": {"type": "number"},
        "title": {"type": "string"},
        "content": {"type": "string"},
        "author": {"type": "number"},
        "post": {"type": "number"}
    },
    "required": ["id"]
}


NEW_USER_SCHEMA = {
    "type": "object",
    "properties": {
        "id": {"type": "number"},
        "username": {"type": "string"},
        "email": {"type": "string"},
        "password": {"type": "string"}
    },
    "required": ["id"]
}