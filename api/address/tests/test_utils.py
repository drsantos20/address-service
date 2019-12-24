from django.test import TestCase

from api.address.utils import build_google_maps_address
from api.address.validations import AddressURLFormatErrorException


class TestUtils(TestCase):
    def setUp(self):
        self.address = {
            'id': 1,
            'street': 'Alameda Santos 415',
            'city': 'São Paulo',
            'neighborhood': 'Jardim Paulista',
            'zip_code': '04319-000',
            'uf': 'SP'
        }

    def test_build_address_with_success(self):
        address = build_google_maps_address(self.address)

        self.assertEqual(
            address,
            'Alameda Santos 415, São Paulo, Jardim Paulista, SP'
        )

    def test_assert_error_given_a_wrong_address_without_street_field(self):
        with self.assertRaises(AddressURLFormatErrorException) as context:
            wrong_address = {
                'id': 1,
                'city': 'São Paulo',
                'neighborhood': 'Jardim Paulista',
                'zip_code': '04319-000',
                'uf': 'SP'
            }
            url = build_google_maps_address(wrong_address)

            self.assertIsNone(url)
            self.assertTrue('street is a required field' in context.exception)
