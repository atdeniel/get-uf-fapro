import unittest
from unittest.mock import patch, MagicMock

from utils.beautiful_soup import scrape_website
from bs4 import BeautifulSoup

import requests
import importlib

class TestBeautifulSoup(unittest.TestCase):

    @patch('utils.beautiful_soup.requests.get')
    @patch('utils.beautiful_soup.getattr')
    def test_scrape_website(self, mock_getattr, mock_requests_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = '<html><body><div id="content">23.273,57</div></body></html>'
        mock_requests_get.return_value = mock_response
        
        mock_getattr.return_value = MagicMock(return_value='23.273,57')

        url = 'https://google.com'
        parameters = {'day': '12', 'month': '12', 'year': '2023'}
        
        result = scrape_website(
            url,
            'sii_soup',
            'find_value_for_day',
            parameters
        )
        (status, value) = tuple(result.values())
        
        mock_requests_get.assert_called_once_with(url)
        self.assertEqual(value, '23.273,57')

    @patch('utils.beautiful_soup.requests.get')
    @patch('utils.beautiful_soup.getattr')
    def test_scrape_website_failure(self, mock_getattr, mock_requests_get):

        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_requests_get.return_value = mock_response

        mock_getattr.return_value = MagicMock(return_value='23.273,57')
        
        
        result = scrape_website(
            'https://test.com',
            'sii_soup', 'find_value_for_day',
            {'day': '12', 'month': '12', 'year': '2023'}
        )
        (status, value) = tuple(result.values())
        
        self.assertEqual(status, False)

    def test_not_function_found(self):

        result = scrape_website(
            'https://test.com',
            'no_module', 'no_function',
            {'day': '12', 'month': '12', 'year': '2023'}
        )
        (status, value) = tuple(result.values())

        self.assertEqual(status, False)


if __name__ == '__main__':
    unittest.main()