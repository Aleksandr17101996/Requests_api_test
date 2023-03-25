POST_SCHEMA = {
    "type": "object",
    "properties": {
        "id": {"type": "number"},
        "name": {"type": "string"},
        "content": {"type": "string"},
        "author": {"type": "number"}
    },
    "required": ["id"]
}

POSTS_SCHEMA = {
    "type": "array",
    "properties": {
        "id": {"type": "number"},
        "title": {"type": "string"},
        "name": {"type": "string"},
        "author": {"type": "number"}
    },
    "required": ["id"]
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

COMMENTS_SCHEMA = {
    "type": "array",
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