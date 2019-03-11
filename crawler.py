import os
import gevent
import gevent.monkey

gevent.monkey.patch_all()

from injections import INJECTION_TYPES
from storage.Storage import Storage
from auth import Auth


class Crawler:
    browser = None
    storage = None

    def __init__(self):
        storage = Storage(name=os.environ.get('STORAGE_ENGINE'))
        self.storage = storage.get_storage()

    def run(self):
        auth = Auth()
        self.browser = auth.authenticate()

        jobs = [gevent.spawn(self.inject, url) for url in self.get_scrape_urls()]
        gevent.wait(jobs)

    def inject(self, url):
        self.browser.open(url)
        for key, value in INJECTION_TYPES.items():
            form = self.browser.select_form('form')
            form['id'] = value

            self.browser.submit_selected()
            # we assume that the presence of `pre` tag means we got some results
            results = self.browser.get_current_page().select('pre')

            for result in results:
                self.storage.set(key, str(result))

    @staticmethod
    def get_scrape_urls():
        """
        This can be retrieve from a storage engine or from a
        configuration file
        :return:
        """
        return [
            'http://localhost:11985/vulnerabilities/sqli/'
        ]
