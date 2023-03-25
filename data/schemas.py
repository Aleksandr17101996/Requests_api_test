POST_SCHEMA = {
    "type": "object",
    "properties": {
        "id": {"type": "number"},
        "title": {"type": "string"},
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
        "content": {"type": "string"},
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


