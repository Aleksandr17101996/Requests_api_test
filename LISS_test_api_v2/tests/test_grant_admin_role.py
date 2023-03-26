from LISS_test_api_v2.grant_user_admin_role import GrantUserAdminRole
from LISS_test_api_v2.tests.sign_in_test import TestNewUser
from requests.auth import HTTPBasicAuth
from config import Base, ErrorMessages

tu = TestNewUser()


class TestGrantUserAdminRole(GrantUserAdminRole):
    user_id = tu.test_add_new_user()
    auth_admin = HTTPBasicAuth(Base.USER_NAME_ADMIN, Base.USER_PASSWORD_ADMIN)

    def test_grant_admin_role(self):
        """Тест проверяет возможность предоставить пользователю права администратора"""

        status_code, body = self.put_admin_rights_user(self.user_id, self.auth_admin)
        assert status_code == 200, ErrorMessages.WRONG_STATUS_CODE.value
        assert body["message"] == "updated", ErrorMessages.WRONG_BODY.value
