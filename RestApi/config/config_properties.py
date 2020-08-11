import os
import json
from aws.parameter_store import *
from base.base_class import BaseClass

class ConfigProperties(BaseClass):

    Environment:str = None
    Message:str = None
    Feed:str = None
    FeedKey:str = None
    DataBaseService:str = None
    GetProviders:str = None

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
            self.Message = config["Message"] or "Welcome to RestApi"
            self.Feed = config['Feed']
            self.FeedKey = config['FeedKey']
            self.DataBaseService = config['DataBaseService']
            self.GetProviders = config['GetProviders']

        else:
            self.Message = get_parameter("/Prod/RestApi/Message") or "Welcome to RestApi"
            self.Feed = get_parameter('/Prod/RestApi/Feed')
            self.FeedKey = get_parameter('/Prod/RestApi/FeedKey')
            self.DataBaseService = get_parameter('/Prod/RestApi/DataBaseService')
            self.GetProviders = get_parameter('/Prod/RestApi/GetProviders')

        if not self.Message:
            raise ValueError("Message is required in the config file.")
        if not self.Feed:
            raise ValueError("Feed is required in the config file.")
        if not self.DataBaseService:
            raise ValueError("DataBaseService is required in the config file.")


config = ConfigProperties("config.json")
#config = ConfigProperties(r"..\config.json")

if __name__ == "__main__":
    print(ConfigProperties(r"..\config.json"))