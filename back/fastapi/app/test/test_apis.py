import unittest
from unittest.mock import patch, MagicMock

from utils.beautiful_soup import scrape_website
from bs4 import BeautifulSoup

import json

from routers.sii import get_uf
from functools import wraps

import requests
import importlib

class TestGetUF(unittest.IsolatedAsyncioTestCase):

    @patch('routers.sii.sii_service.get_uf_by_date')
    @patch('routers.sii.validate_date')
    async def test_get_uf_success(self, mock_validate_date, mock_get_uf_by_date):
        
        mock_get_uf_by_date.return_value = {'status': True, 'value': '28000'}
        response = await get_uf("19-03-2014")
        response_body = json.loads(response.body)
        self.assertEqual(response_body, {"date": "19-03-2014", "uf_value": '28000'})

    @patch('routers.sii.sii_service.get_uf_by_date')
    async def test_get_uf_failure(self, mock_get_uf_by_date):
        
        mock_get_uf_by_date.return_value = {'status': False, 'value': None}

        # Llamada a la función asíncrona get_uf y manejo de la excepción
        with self.assertRaises(Exception) as context:
            await get_uf("19-03-2014")

        self.assertEqual('500', str(context.exception.status_code))


if __name__ == '__main__':
    unittest.main()