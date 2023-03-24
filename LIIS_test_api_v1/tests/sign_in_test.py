from LIIS_test_api_v1.sign_in import NewUser


class TestNewUser(NewUser):

    def test_add_new_user(self):
        """Метод содержит позитивный тестовый сценарий выполняя запрос на регистрацию пользователя
                       с валидными данными"""

        user_name = "Alexandr"
        user_email = "Alexandr@mail.com"
        user_password = "123"
        status_code, body = self.sign_in_new_user(user_name, user_email, user_password)
        assert status_code == 201, "Статус кода не соответсвует ожидаемому"
        assert body["username"] == user_name, "Имя пользователя в ответе неверно"
        assert body["email"] == user_email, "Email пользователя в ответе не верен"
        assert int(body["id"]) > 0, "id не является числом"

    def test_add_existin_name_user(self):
        """Метод содержит негативный тестовый сценарий выполняя запрос на регистрацию пользователя
                               с именем уже зарегестрированного пользователя"""

        user_name = "Alexandr"  # Имя Alexandr уже есть в системе
        user_email = "Alexandr@mail.com"  # Данный емайл рандомный
        user_password = "123"
        status_code, body = self.sign_in_new_user(user_name, user_email, user_password)
        assert status_code == 409, "Статус кода не соответсвует ожидаемому"
        assert body["message"] == "User with this username or email already exists"

    def test_add_existin_email_user(self):
        """Метод содержит негативный тестовый сценарий выполняя запрос на регистрацию пользователя
                               с почтой уже зарегестрированного пользователя"""

        user_name = "Alexandr"  # Имя рандомное
        user_email = "Alexandr@mail.com"  # Данный емайл уже зарегестрированн в системе
        user_password = "123"
        status_code, body = self.sign_in_new_user(user_name, user_email, user_password)
        assert status_code == 409, "Статус кода не соответсвует ожидаемому"
        assert body["message"] == "User with this username or email already exists"

