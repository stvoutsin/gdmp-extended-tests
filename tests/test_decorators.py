import unittest
from tests.utils.decorator import Decorator


class TestDecorator(unittest.TestCase):
    #  Tests that decorate_http returns a valid HTTP URL for a valid input string
    def test_http_happy_path(self):
        result = Decorator.decorate_http("www.google.com")
        self.assertEqual(result, "http://www.google.com/")

    #  Tests that decorate_https returns a valid HTTPS URL for a valid input string
    def test_https_happy_path(self):
        result = Decorator.decorate_https("www.google.com")
        self.assertEqual(result, "https://www.google.com/")

    #  Tests that decorate_wss returns a valid WSS endpoint for a valid input string
    def test_wss_happy_path(self):
        result = Decorator.decorate_wss("www.example.com")
        self.assertEqual(result, "wss://www.example.com/ws")

    #  Tests that all decoration methods return an empty string when given an empty string input
    def test_empty_string_edge_case(self):
        with self.assertRaises(ValueError):
            result_http = Decorator.decorate_http("")
        with self.assertRaises(ValueError):
            result_https = Decorator.decorate_https("")
        with self.assertRaises(ValueError):
            result_wss = Decorator.decorate_wss("")

    #  Tests that all decoration methods return an empty string when given a string input with only whitespace characters
    def test_whitespace_string_edge_case(self):
        with self.assertRaises(ValueError):
            result_http = Decorator.decorate_http("   ")
        with self.assertRaises(ValueError):
            result_https = Decorator.decorate_https("   ")
        with self.assertRaises(ValueError):
            result_wss = Decorator.decorate_wss("   ")

    #  Tests that all decoration methods return a valid URL when given a string input with special characters
    def test_special_characters_edge_case(self):
        result_http = Decorator.decorate_http("www.example.com?param=value")
        result_https = Decorator.decorate_https("www.example.com#fragment")
        result_wss = Decorator.decorate_wss("www.example.com:8080")
        self.assertEqual(result_http, "http://www.example.com?param=value/")
        self.assertEqual(result_https, "https://www.example.com#fragment/")
        self.assertEqual(result_wss, "wss://www.example.com:8080/ws")
