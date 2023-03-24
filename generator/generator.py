import random

from data.data import Person
from faker import Faker

faker_en = Faker('en_EN')
Faker.seed()


def generated_person():
    yield Person(
        user_name=faker_en.last_name_female(),
        password=random.randint(10, 80),
        email=faker_en.email(),
    )