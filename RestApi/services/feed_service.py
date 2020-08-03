import threading

import requests
from flask import jsonify

from services.mock_service import MockService
from utils.logger import Logger
from config.config_properties import *
from models.show import Show
class FeedService(object):
    logger = Logger(__name__)
    def get_titles(self, name):
        try:
            feed_headers = {'x-rapidapi-key': config.FeedKey}
            response = requests.get(config.Feed.format(name), verify="certificates/feed.cer", headers = feed_headers)
            headers = {
                'Content-type': 'application/json',
                'Accept': 'text/plain',
                }
            optimized = Show().getShows(response.json())
            db_thread = threading.Thread(target=self.post_to_db, args=[optimized])
            db_thread.daemon = True
            db_thread.start()
            return optimized
        except Exception as ex:
            self.logger.error("Unable to get results",ex)
            return {}

    def get_titles_test(self, name):
        try:
            try:
                optimized = Show().getShows(MockService().getData())
                #self.post_to_db(optimized)
            except Exception as ex:
                self.logger.error("DB service couldn't able to process this result.",ex)
            return optimized
        except Exception as ex:
            self.logger.error("Unable to get results",ex)
            return {}

    def post_to_db(self, titles):
        headers = {
            'Content-type': 'application/json',
            'Accept': 'text/plain',
        }
        db_response = requests.post(config.DataBaseService, json=titles, headers=headers)
        if db_response.status_code != 200:
            self.logger.info("DB service couldn't able to process this result.\n{}".format(json.dumps(titles)))
        else:
            self.logger.info(db_response.json())

if __name__ == "__main__":
    feed_service = FeedService()
    print(feed_service.get_titles_test("Test"))