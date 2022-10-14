from pageobject.listUser import ListUser
import pytest


class Test001ListUsers(ListUser):


    @pytest.mark.parametrize("test_input,expected",
                             [("page", 2), ("per_page", 6), ("total", 12)])
    def test_user_list(self, test_input, expected):
        self.list_user(test_input, expected)