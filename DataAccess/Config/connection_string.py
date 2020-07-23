from Config.config_properties import *
import urllib.parse
class ConnectionStrings:
    def __init__(self):
        pass

    def get_sql_alchemy_con_string(self):
        return '{0}://{1}:{2}@{3}:{4}/{5}'.format(config.Dialect,
                                                  config.UserName,
                                                  urllib.parse.quote_plus(config.Password),
                                                  config.Server,
                                                  config.Port,
                                                  config.DataBase)
