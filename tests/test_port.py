import unittest

import requests

from settings import settings
from tests.utils.decorator import Decorator


class TestPort(unittest.TestCase):
    """
    Tests that the ports & redirects for the Zeppelin Service are as expected
    """

    def test_port_80_open(self):
        """
        Test that port 80 is open
        Returns:
            bool: True if it else, or False otherwise
        """
        response = requests.get(settings.ZEPPELIN_URL)
        self.assertEqual(response.status_code, 200)

    def test_port_443_open(self):
        """
        Test that port 443 is open
        Returns:
            bool: True if it else, or False otherwise
        """

        response = requests.get(settings.ZEPPELIN_URL)
        self.assertEqual(response.status_code, 200)

    def test_redirect_to_https(self):
        """
        Test that the service redirects correctly

        Returns:
            bool: True if it else, or False otherwise
        """

        response = requests.get(
            Decorator.decorate_http(settings.DOMAIN), allow_redirects=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.url, Decorator.decorate_https(settings.DOMAIN))

    def test_redirect_to_https_with_path(self):
        """
        Test that the service redirects correctly with path

        Returns:
            bool: True if it else, or False otherwise
        """

        response = requests.get(
            Decorator.decorate_http(settings.DOMAIN) + "#/?ref=%2F",
            allow_redirects=True,
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.url, Decorator.decorate_https(settings.DOMAIN) + "#/?ref=%2F"
        )


if __name__ == "__main__":
    unittest.main()
