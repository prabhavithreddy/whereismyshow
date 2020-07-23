import os
import json

from Base.base_class import BaseClass

class ConfigProperties(BaseClass):
    
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
        
        if not config['Server']:
            raise ValueError("Server is required in the config file.")
        if not config['UserName']:
            raise ValueError("UserName is required in the config file.")
        if not config['Password']:
            raise ValueError("Password is required in the config file.")
        if not config['DataBase']:
            raise ValueError("DataBase is required in the config file.")
        if not config['Port']:
            raise ValueError("Port is required in the config file.")
        if not config['Dialect']:
            raise ValueError("dialect is required in the config file.")

        self.Server = config['Server']
        self.UserName = config['UserName']
        self.Password = config['Password']
        self.DataBase = config['DataBase']
        self.Port = config['Port']
        self.Dialect = config['Dialect']

config = ConfigProperties(r"..\app.json")

if __name__ == "__main__":
    print(ConfigProperties(r"..\app.json"))