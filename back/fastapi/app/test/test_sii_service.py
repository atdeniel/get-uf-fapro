import unittest
from unittest.mock import patch
from services.sii_service import sii_service

class TestSiiService(unittest.TestCase):

    @patch('services.sii_service.scrape_website')
    def test_get_uf_by_date(self, mock_scrape_website):
        mock_scrape_website.return_value = {'status': True, 'value': '23.273,57'}
        dict_values = sii_service.get_uf_by_date('12-12-2022')
        tuple_values = tuple(dict_values.values())
        self.assertEqual(tuple_values[1], '23.273,57')


if __name__ == '__main__':
    unittest.main()


