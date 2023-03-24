from dataclasses import dataclass


@dataclass
class Person:
    user_name: str = None
    password: int = None
    email: str = None
    first_name: str = None
    middle_name: str = None
    last_name: str = None
