from LIIS_test_api_v1.sign_in import NewUser
from generator.generator import generated_person


class TestNewUser(NewUser):

    def test_add_new_user(self):
        """Тест содержит позитивный тестовый сценарий выполняя запрос на регистрацию пользователя
           с валидными данными, которые сгенерированы автоматически"""

        person_info = next(generated_person())
        email = person_info.email
        password = person_info.password
        name = person_info.user_name
        status_code, body = self.sign_in_new_user(name, email, str(password))
        assert status_code == 201, "Статус кода не соответсвует ожидаемому"
        assert body["username"] == name, "Имя пользователя в ответе неверно"
        assert body["email"] == email, "Email пользователя в ответе не верен"
        assert int(body["id"]) > 0, "id не является числом"

    def test_add_existin_name_user(self):
        """ Тест содержит негативный тестовый сценарий выполняя запрос на регистрацию пользователя
            с именем уже зарегестрированного пользователя, почта и пароль генерируются автоматически"""

        person_info = next(generated_person())
        email = person_info.email
        password = person_info.password
        user_name = "Alexandr"  # Имя Alexandr уже зарегестрированно в системе
        status_code, body = self.sign_in_new_user(user_name, email, str(password))
        assert status_code == 409, "Статус кода не соответсвует ожидаемому"
        assert body["message"] == "User with this username or email already exists"

    def test_add_existin_email_user(self):
        """Тест содержит негативный тестовый сценарий выполняя запрос на регистрацию пользователя
           с почтой уже зарегестрированного пользователя"""

        person_info = next(generated_person())
        name = person_info.user_name
        password = person_info.password
        user_email = "Alexandr@mail.com"  # Данная почта уже зарегестрированна в системе.
        status_code, body = self.sign_in_new_user(name, user_email, str(password))
        assert status_code == 409, "Статус кода не соответсвует ожидаемому"
        assert body["message"] == "User with this username or email already exists"

    def test_not_valid_password(self):
        """Тест содержит негативный тестовый сценарий выполняя запрос на регистрацию пользователя
           с паролем в формате int, и данными которые сгенерированы автоматически"""

        person_info = next(generated_person())
        email = person_info.email
        password = person_info.password
        name = person_info.user_name
        status_code, body = self.sign_in_new_user(name, email, password)
        assert status_code == 422, "Статус кода не соответсвует ожидаемому"
        assert body["password"][-1] == "Not a valid string.", "Ошибка не обработана"

