from LISS_test_api_v2.sign_in import AddNewUser
from data.generator import generated_person
from config import GlobalErrorMessages


class TestNewUser(AddNewUser):
    def test_add_new_user(self):
        """Тест содержит позитивный тестовый сценарий выполняя запрос на регистрацию пользователя
           с валидными данными, которые сгенерированы автоматически, возвращает id созданного пользователя"""

        person_info = next(generated_person())
        email = person_info.email
        password = person_info.password
        name = person_info.user_name
        first_name = person_info.first_name
        middle_name = person_info.middle_name
        last_name = person_info.last_name
        status_code, body = self.sign_in_new_user(name, email, str(password), first_name, middle_name, last_name, )
        assert status_code == 201, GlobalErrorMessages.WRONG_STATUS_CODE.value
        assert body["username"] == name, GlobalErrorMessages.WRONG_BODY.value
        assert body["email"] == email, GlobalErrorMessages.WRONG_BODY.value
        assert int(body["id"]) > 0, GlobalErrorMessages.WRONG_BODY.value
        assert body["first_name"] == first_name, GlobalErrorMessages.WRONG_BODY.value
        assert body["middle_name"] == middle_name, GlobalErrorMessages.WRONG_BODY.value
        assert body["last_name"] == last_name, GlobalErrorMessages.WRONG_BODY.value
        return body["id"]

    def test_are_not_fields_new_user(self):
        """Тест содержит позитивный тестовый сценарий выполняя запрос на регистрацию пользователя
           с валидными данными, без обязательных полей"""

        person_info = next(generated_person())
        email = person_info.email
        password = person_info.password
        name = person_info.user_name
        first_name = None
        middle_name = None
        last_name = None
        status_code, body = self.sign_in_new_user(name, email, str(password), first_name, middle_name, last_name, )
        assert status_code == 201, GlobalErrorMessages.WRONG_STATUS_CODE.value
        assert body["username"] == name, GlobalErrorMessages.WRONG_BODY.value
        assert body["email"] == email, GlobalErrorMessages.WRONG_BODY.value
        assert int(body["id"]) > 0, GlobalErrorMessages.WRONG_BODY.value
        assert body["first_name"] == first_name, GlobalErrorMessages.WRONG_BODY.value
        assert body["middle_name"] == middle_name, GlobalErrorMessages.WRONG_BODY.value
        assert body["last_name"] == last_name, GlobalErrorMessages.WRONG_BODY.value



