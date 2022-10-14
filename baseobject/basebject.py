import requests
from utilities.readproperties import ReadConfig


class Baseobject(ReadConfig):

    @staticmethod
    def choose_method(method, link, data):
        choose_method = {"get": requests.get(link),
                         "post": requests.post(link, data),
                         "put": requests.put(link, data),
                         "delete": requests.delete(link)
                         }
        return choose_method[method]

    def html_method(self, method, link, data=None):
        get_method = self.choose_method(method, link, data)
        return get_method
