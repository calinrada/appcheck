import mechanicalsoup
from exception import AuthException


class Auth:
    def authenticate(self):
        """
        Authenticate based on known credentials using the form
        from the login page
        :return browser:
        """
        browser = mechanicalsoup.StatefulBrowser(raise_on_404=True)
        browser.open(self.get_auth_url())

        login_data = self.get_login_data()

        form = browser.select_form('form')
        form['username'] = login_data['username']
        form['password'] = login_data['password']

        response = browser.submit_selected()

        if 'Logout' in response.text:
            return browser
        else:
            raise AuthException

    @staticmethod
    def get_login_data():
        """
        This can be retrieve from a storage engine or from a
        configuration file
        :return:
        """
        return {
            'username': 'admin',
            'password': 'password',
            'user_token': None
        }

    @staticmethod
    def get_auth_url():
        """
        This can be retrieve from a storage engine or from a
        configuration file
        :return:
        """
        return 'http://localhost:11985/login.php'
