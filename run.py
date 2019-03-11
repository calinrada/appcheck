import time as timer
import random

from env import read_env
from logger import Logger
from crawler import Crawler
from exception import AuthException

logger = Logger()
read_env()

# We run this continuously
while True:
    try:
        crawler = Crawler()
        crawler.run()

        rntime = random.randrange(30, 60, 5)
        logger.log('Sleeping for %s seconds ... ' % rntime)
        timer.sleep(rntime)

    except AuthException as e:
        logger.error('Authentication error: %s' % str(e))
    except AttributeError as e:
        logger.error('Attribute error: %s' % str(e))
    except Exception as e:
        logger.error('Unknown error: %s' % str(e))
