import os
import configparser
import json

class ConfigProperties(object):
    Welcome = None
    Environment = None

    Server = None
    UserName = None
    Password = None
    DataBase = None
    Driver = None
    Dialect = None
    Port = None

    def __init__(self, config_file):

        config = configparser.ConfigParser()
        if not os.path.exists(config_file):
            raise FileNotFoundError(config_file + 'not found.')
        config.read(config_file)

        if not config.has_section('DATABASE'):
            raise ValueError("DATABASE section doesn't exists in software.ini.")
        if not config.has_option('DATABASE', 'Server'):
            raise ValueError("Server is required under DATABASE section in software.ini.")
        if not config.has_option('DATABASE', 'UserName'):
            raise ValueError("UserName is required under DATABASE section in software.ini.")
        if not config.has_option('DATABASE', 'Password'):
            raise ValueError("Password is required under DATABASE section in software.ini.")
        if not config.has_option('DATABASE', 'DataBase'):
            raise ValueError("DataBase is required under DATABASE section in software.ini.")
        if not config.has_option('DATABASE', 'Port'):
            raise ValueError("Port is required under DATABASE section in software.ini.")
        if not config.has_option('DATABASE', 'driver'):
            raise ValueError("driver is required under DATABASE section in software.ini.")
        if not config.has_option('DATABASE', 'dialect'):
            raise ValueError("dialect is required under DATABASE section in software.ini.")

        self.Server = config['DATABASE']['Server']
        self.UserName = config['DATABASE']['UserName']
        self.Password = config['DATABASE']['Password']
        self.DataBase = config['DATABASE']['DataBase']
        self.Port = config['DATABASE']['Port']
        self.Driver = config['DATABASE']['driver']
        self.Dialect = config['DATABASE']['dialect']

        if not self.Server:
            raise ValueError("['DATABASE']['Server'] cannot be null or empty")
        if not self.UserName:
            raise ValueError("['DATABASE']['UserName'] cannot be null or empty")
        if not self.Password:
            raise ValueError("['DATABASE']['Password'] cannot be null or empty")
        if not self.DataBase:
            raise ValueError("['DATABASE']['DataBase'] cannot be null or empty")
        if not self.Port:
            raise ValueError("['DATABASE']['Port'] cannot be null or empty")
        if not self.Driver:
            raise ValueError("['DATABASE']['driver'] cannot be null or empty")
        if not self.Dialect:
            raise ValueError("['DATABASE']['dialect'] cannot be null or empty")

        self.Welcome = config['SETTINGS']['Welcome']
        self.Environment = config['SETTINGS']['Environment']

    def __repr__(self):
        dictionary = dict()
        dictionary['Environment'] = self.Environment
        dictionary['Server'] = self.Server
        dictionary['UserName'] = self.UserName
        dictionary['Password'] = self.Password
        dictionary['DataBase'] = self.DataBase
        dictionary['Driver'] = self.Driver
        dictionary['Dialect'] = self.Dialect
        dictionary['Port'] = self.Port
        return json.dumps(dictionary)

if __name__ == "__main__":
    config = ConfigProperties("..\software.ini")
    print(config)