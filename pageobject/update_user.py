from baseobject.basebject import Baseobject
import json


class UpdateUser(Baseobject):

    def update_user(self):
        body = open(r"C:\Users\99455\Desktop\Automation\Selenium\Api_python\payload\updateUser_payload.json", "r")
        response = self.html_method('put', self.update_user_url(), data=json.load(body))
        response_json = response.json()
        assert response.status_code == 200
        assert response_json["job"] == "Azerconnect"
        assert response_json["updatedAt"]

