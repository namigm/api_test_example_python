from pageobject.createUser import CreateUser


class Test002CreateUser(CreateUser):
    def test_create_user(self):
        self.create_user()
