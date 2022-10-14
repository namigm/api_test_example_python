from pageobject.deleteUser import DeleteUser


class Test004DeleteUser(DeleteUser):
    def test_delete_user(self):
        self.delete_user()
