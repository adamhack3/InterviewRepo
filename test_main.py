import unittest

from main import fetch_addresses

class TestApi(unittest.TestCase):

    def test_main_response(self):

        addresses = fetch_addresses()

        assert isinstance(addresses, list), "Not returning dict!"
        assert "lines" in addresses[0].keys(), "Not returning address lines!"
    
