from configparser import ConfigParser

config = ConfigParser()
config.read(r'C:\Users\99455\Desktop\Automation\Selenium\Api_python\congiguration\config.ini')


# 'raw string' means it is stored as it appears. For example, '\' is just a backslash instead of an escaping.
class ReadConfig:

    @staticmethod
    def list_users_url():
        list_user = config['common info']['list_users']
        return list_user

    @staticmethod
    def create_user_url():
        create_user = config['common info']['create_user']
        return create_user

    @staticmethod
    def update_user_url():
        update_user = config['common info']['update_user']
        return update_user

    @staticmethod
    def delete_user_url():
        delete_user = config['common info']['delete_user']
        return delete_user
