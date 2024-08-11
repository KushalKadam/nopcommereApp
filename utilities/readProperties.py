import configparser

from pip._internal.configuration import Configuration

config = configparser.RawConfigParser()
config.read(".\\Configuration/config.ini") #.\\ represents current project directory

class ReadConfig():
    @staticmethod
    def getApplicationURL():
        url = config.get('common info', 'baseURL')
        return url

    @staticmethod
    def getUserEmail():
        username = config.get('common info', 'user_email')
        return username

    @staticmethod
    def getUserPassword():
        password = config.get('common info', 'password')
        return password