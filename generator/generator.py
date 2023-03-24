import random
import string

from data.data import Person
from faker import Faker

faker_en = Faker('en_US')
Faker.seed()


def generated_person():
    yield Person(
        user_name=faker_en.last_name_female(),
        password=random.randint(100, 9999),
        email=faker_en.email(),
    )


def generate_random_string(length):
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(length))
    return rand_string


def generate_random_id():
    randon_id = random.randint(100000000, 9999999999)
    return str(randon_id)
