import os
import json
from aws.parameter_store import *
from Base.base_class import BaseClass

class ConfigProperties(BaseClass):

    Environment:str = None
    Message = None
    Server = None
    UserName = None
    Password = None
    DataBase = None
    Dialect = None
    Port = None

    def __init__(self, config_file):
        if not os.path.exists(config_file):
            raise FileNotFoundError(config_file + 'not found.')
        config = None
        with open(config_file, "r") as file:
            config = json.loads(file.read())

        if not config['Environment']:
            raise ValueError("Environment is required in the config file.")
        self.Environment = config["Environment"]

        if self.Environment.__eq__("dev"):
            self.Message = config["Message"] or "Welcome to DataAccess"
            self.Server = config['Server']
            self.UserName = config['UserName']
            self.Password = config['Password']
            self.DataBase = config['DataBase']
            self.Port = config['Port']
            self.Dialect = config['Dialect']

        else:
            self.Message = get_parameter("/Prod/Message") or "Welcome to DataAccess"
            self.Server = get_parameter('/Prod/DB/Server')
            self.UserName = get_parameter('/Prod/DB/UserName')
            self.Password = get_parameter('/Prod/DB/Password')
            self.DataBase = get_parameter('/Prod/DB/DataBase')
            self.Port = get_parameter('/Prod/DB/Port')
            self.Dialect = get_parameter('/Prod/DB/Dialect')

        if not self.Message:
            raise ValueError("Message is required in the config file.")
        if not self.Server:
            raise ValueError("Server is required in the config file.")
        if not self.UserName:
            raise ValueError("UserName is required in the config file.")
        if not self.Password:
            raise ValueError("Password is required in the config file.")
        if not self.DataBase:
            raise ValueError("DataBase is required in the config file.")
        if not self.Port:
            raise ValueError("Port is required in the config file.")
        if not self.Dialect:
            raise ValueError("dialect is required in the config file.")



#config = ConfigProperties("app.json")
config = ConfigProperties(r"..\app.json")

if __name__ == "__main__":
    print(ConfigProperties(r"..\app.json"))