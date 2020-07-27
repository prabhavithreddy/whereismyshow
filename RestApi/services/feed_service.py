import requests
from utils.logger import Logger
from config.config_properties import *
from models.show import Show
class FeedService(object):
    logger = Logger(__name__)
    def get_titles(self, name):
        try:
            response = requests.get(config.Feed.format(name))
            headers = {
                'Content-type': 'application/json',
                'Accept': 'text/plain',
                'x-rapidapi-key': config.FeedKey
                }
            optimized = Show().getShows(response.json())
            try:
                db_response = requests.post(config.DataBaseService, json=optimized, headers = headers)
                if db_response.status_code != 200:
                    self.logger.info("DB service couldn't able to process this result.\n{}".format(json.dumps(optimized)))
            except Exception as ex:
                self.logger.error("DB service couldn't able to process this result.",ex)
            return optimized
        except Exception as ex:
            self.logger.error("Unable to get results",ex)
            return {}