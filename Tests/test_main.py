from main import addresses_for_postcode

class TestSuite:

    def test_addresses_for_postcode(self):
        TEST_POSTCODE = "E8 3LH"
        addresses = addresses_for_postcode(TEST_POSTCODE)
        assert isinstance(addresses, list)
        assert "UPRN" in addresses[0].keys()


