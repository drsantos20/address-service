from django.test import TestCase

from api.address.utils import build_google_maps_url
from api.address.validations import AddressURLFormatErrorException


class TestUtils(TestCase):
    def setUp(self):
        self.address = {
            'id': 1,
            'street': 'Alameda Santos, 415',
            'city': 'São Paulo',
            'neighborhood': 'Jardim Paulista',
            'zip_code': '04319-000',
            'uf': 'SP'
        }

    def test_build_url_with_success(self):
        url = build_google_maps_url(self.address)

        'get url until api KEY'
        url = url[:110]

        self.assertEqual(
            url,
            'https://maps.googleapis.com/maps/api/geocode/json?address=Alameda+Santos,+415+Jardim+Paulista+São+Paulo+SP&key'
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
            url = build_google_maps_url(wrong_address)

            self.assertIsNone(url)
            self.assertTrue('street is a required field' in context.exception)
