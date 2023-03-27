from LISS_test_api_v2.sign_in import AddNewUser
from data.generator import generated_person
from config import ErrorMessages
from data.validator import ValidateNewUser


class TestNewUser(AddNewUser):
    v = ValidateNewUser()

    def test_add_new_user(self):
        """Тест содержит позитивный тестовый сценарий выполняя запрос на регистрацию пользователя
           с валидными данными, которые сгенерированы автоматически, валидируем ответ по json схеме
           и сверяем с отправленными данными, а так же возвращает id созданного пользователя"""

        person_info = next(generated_person())
        email = person_info.email
        password = person_info.password
        name = person_info.user_name
        first_name = person_info.first_name
        middle_name = person_info.middle_name
        last_name = person_info.last_name
        status_code, body = self.sign_in_new_user(name, email, str(password), first_name, middle_name, last_name)
        self.v.user_validation(body)
        assert status_code == 201, ErrorMessages.WRONG_STATUS_CODE.value
        assert body["username"] == name, ErrorMessages.WRONG_BODY.value
        assert body["email"] == email, ErrorMessages.WRONG_BODY.value
        assert int(body["id"]) > 0, ErrorMessages.WRONG_BODY.value
        assert body["first_name"] == first_name, ErrorMessages.WRONG_BODY.value
        assert body["middle_name"] == middle_name, ErrorMessages.WRONG_BODY.value
        assert body["last_name"] == last_name, ErrorMessages.WRONG_BODY.value
        return body["id"]

    def test_are_not_fields_new_user(self):
        """Тест содержит позитивный тестовый сценарий выполняя запрос на регистрацию пользователя
           с валидными данными, без обязательных полей, валидируем ответ по json схеме,
           сверяем между собой отправленные и полученные данные """

        person_info = next(generated_person())
        email = person_info.email
        password = person_info.password
        name = person_info.user_name
        status_code, body = self.sign_in_new_user(name, email, str(password), None, None, None)
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
        name = "Alexandr"  # Имя Alexandr уже зарегестрированно в системе
        status_code, body = self.sign_in_new_user(name, email, str(password), None, None, None)
        assert status_code == 409, ErrorMessages.WRONG_STATUS_CODE.value
        assert body["message"] == "User with this username or email already exists", ErrorMessages.WRONG_VALIDATE.value


    def test_add_existin_email_user(self):
        """Тест содержит негативный тестовый сценарий выполняя запрос на регистрацию пользователя
           с почтой уже зарегестрированного пользователя"""

        person_info = next(generated_person())
        email = "Alexandr@mail.com"  # Данная почта уже зарегестрированна в системе.
        password = person_info.password
        name = person_info.user_name
        first_name = None
        middle_name = None
        last_name = None
        status_code, body = self.sign_in_new_user(name, email, str(password), first_name, middle_name, last_name, )
        assert status_code == 409, ErrorMessages.WRONG_STATUS_CODE.value
        assert body["message"] == "User with this username or email already exists", ErrorMessages.WRONG_VALIDATE.value


    def test_not_valid_password(self):
        """Тест содержит негативный тестовый сценарий выполняя запрос на регистрацию пользователя
           с паролем в формате int, и данными которые сгенерированы автоматически"""

        person_info = next(generated_person())
        email = person_info.email
        password = person_info.password
        name = person_info.user_name
        status_code, body = self.sign_in_new_user(name, email, password, None, None, None)
        assert status_code == 422, ErrorMessages.WRONG_STATUS_CODE.value
        assert body["password"][-1] == "Not a valid string.", ErrorMessages.WRONG_VALIDATE.value
