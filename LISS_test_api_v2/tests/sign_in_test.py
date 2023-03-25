from LISS_test_api_v2.sign_in import AddNewUser
from generator.generator import generated_person
from config import GlobalErrorMessages


class TestNewUser(AddNewUser):
    def test_add_new_user(self):
        """Тест содержит позитивный тестовый сценарий выполняя запрос на регистрацию пользователя
           с валидными данными, которые сгенерированы автоматически"""

        person_info = next(generated_person())
        email = person_info.email
        password = person_info.password
        name = person_info.user_name
        first_name = person_info.first_name
        middle_name = person_info.middle_name
        last_name = person_info.last_name
        status_code, body = self.sign_in_new_user(name, email, str(password), first_name, middle_name, last_name,)
        assert status_code == 201, GlobalErrorMessages.WRONG_STATUS_CODE.value
        assert body["username"] == name, GlobalErrorMessages.WRONG_BODY.value
        assert body["email"] == email, GlobalErrorMessages.WRONG_BODY.value
        assert int(body["id"]) > 0, GlobalErrorMessages.WRONG_BODY.value
        assert body["first_name"] == first_name, GlobalErrorMessages.WRONG_BODY.value
        assert body["middle_name"] == middle_name, GlobalErrorMessages.WRONG_BODY.value
        assert body["last_name"] == last_name, GlobalErrorMessages.WRONG_BODY.value

    def test_add_existin_name_user(self):
        """ Тест содержит негативный тестовый сценарий выполняя запрос на регистрацию пользователя
            с именем уже зарегестрированного пользователя, почта и пароль генерируются автоматически"""




