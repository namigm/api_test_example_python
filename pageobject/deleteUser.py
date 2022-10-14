from baseobject.basebject import Baseobject


class DeleteUser(Baseobject):

    def delete_user(self):
        response = self.html_method('delete', self.delete_user_url())
        assert response.status_code == 204, "User not deleted"
