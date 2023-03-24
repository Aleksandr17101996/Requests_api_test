from dataclasses import dataclass


@dataclass
class Person:
    user_name: str = None
    password: int = None
    email: str = None
