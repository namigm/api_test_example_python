import json
from baseobject.basebject import Baseobject


class CreateUser(Baseobject):

    def create_user(self):
        body = open(r'C:\Users\99455\Desktop\Automation\Selenium\Api_python\payload\createUser_payload.json', 'r')
        response = self.html_method('post', self.create_user_url(), data=json.load(body))
        response_json = response.json()
        assert response_json['name'] == "morpheus" \
               and response_json['job'] == "leader" \
               and response.status_code == 201
