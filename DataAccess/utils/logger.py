import logging
import time
from logging.handlers import TimedRotatingFileHandler


class Logger(object):
    default_file_path = "../log.txt"
    logger = None
    def __init__(self, module):

        handler = TimedRotatingFileHandler(self.default_file_path,
                                           when="d",
                                           interval=1,
                                           backupCount=5)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        root = logging.getLogger()
        root.setLevel("INFO")
        root.addHandler(handler)

    def info(self, message):
        logging.info(message)

    def error(self, message, exception):
        logging.exception("{}\n{}".format(message,exception))


if __name__ == "__main__":
    logger = Logger(__name__)
    logger.info("Test")
    try:
        r = 1/0
    except Exception as ex:
        logger.error(ex)