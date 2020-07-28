import logging
from logging.handlers import TimedRotatingFileHandler

default_file_path = "../log.txt"
handler = TimedRotatingFileHandler(default_file_path,
                                           when="d",
                                           interval=1,backupCount=5)
class Logger(object):
    logger = None
    def __init__(self, module):
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger = logging.getLogger()
        self.logger.setLevel("INFO")
        self.logger.addHandler(handler)

    def info(self, message):
        self.logger.info(message)

    def error(self, message, exception):
        self.logger.exception("{}\n{}".format(message,exception))


if __name__ == "__main__":
    logger = Logger(__name__)
    logger.info("Test")
    try:
        r = 1/0
    except Exception as ex:
        logger.error(ex)