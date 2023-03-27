from LIIS_test_api_v1.sign_in import NewUser
from data.generator import generated_person
from config import ErrorMessages
from jsonschema import validate
from data.schemas.schemas import NEW_USER_SCHEMA


class TestNewUser(NewUser):

    def test_add_new_user(self):
        """Тест содержит позитивный тестовый сценарий выполняя запрос на регистрацию пользователя
           с валидными данными, которые сгенерированы автоматически"""

        person_info = next(generated_person())
        email = person_info.email
        password = person_info.password
        name = person_info.user_name
        status_code, body = self.sign_in_new_user(name, email, str(password))
        validate(body, NEW_USER_SCHEMA)
        assert status_code == 201, ErrorMessages.WRONG_STATUS_CODE.value
        assert body["username"] == name, ErrorMessages.WRONG_BODY.value
        assert body["email"] == email, ErrorMessages.WRONG_BODY.value
        assert int(body["id"]) > 0, ErrorMessages.WRONG_BODY.value

    def test_add_existin_name_user(self):
        """ Тест содержит негативный тестовый сценарий выполняя запрос на регистрацию пользователя
            с именем уже зарегестрированного пользователя, почта и пароль генерируются автоматически"""

        person_info = next(generated_person())
        email = person_info.email
        password = person_info.password
        user_name = "Alexandr"  # Имя Alexandr уже зарегестрированно в системе
        status_code, body = self.sign_in_new_user(user_name, email, str(password))
        assert status_code == 409, ErrorMessages.WRONG_STATUS_CODE.value
        assert body["message"] == "User with this username or email already exists"

    def test_add_existin_email_user(self):
        """Тест содержит негативный тестовый сценарий выполняя запрос на регистрацию пользователя
           с почтой уже зарегестрированного пользователя"""

        person_info = next(generated_person())
        name = person_info.user_name
        password = person_info.password
        user_email = "Alexandr@mail.com"  # Данная почта уже зарегестрированна в системе.
        status_code, body = self.sign_in_new_user(name, user_email, str(password))
        assert status_code == 409, ErrorMessages.WRONG_STATUS_CODE.value
        assert body["message"] == "User with this username or email already exists"

    def test_not_valid_password(self):
        """Тест содержит негативный тестовый сценарий выполняя запрос на регистрацию пользователя
           с паролем в формате int, и данными которые сгенерированы автоматически"""

        person_info = next(generated_person())
        email = person_info.email
        password = person_info.password
        name = person_info.user_name
        status_code, body = self.sign_in_new_user(name, email, password)
        assert status_code == 422, ErrorMessages.WRONG_STATUS_CODE.value
        assert body["password"][-1] == "Not a valid string.", ErrorMessages.WRONG_VALIDATE.value
