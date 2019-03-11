import logging
import datetime


class Logger:
    def __init__(self):
        logging.basicConfig(
            filename='%s.log' % (datetime.datetime.now().strftime("%Y-%m-%d")),
            level=logging.DEBUG
        )

    def error(self, message):
        logging.error(message)
