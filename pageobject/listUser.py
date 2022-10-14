from baseobject.basebject import Baseobject


class ListUser(Baseobject):

    def list_user(self, test_input, expected):
        response = self.html_method('get', self.list_users_url(), timeout=1)
        assert response.json()[test_input] == expected
        assert response.status_code == 200, "listUser_status code is does not matched"









