from api import settings
from api.address.validations import AddressURLFormatErrorException


def build_google_maps_url(body):
    if not body.get('street'):
        raise AddressURLFormatErrorException('street is a required field')
    street = body['street']

    if not body.get('city'):
        raise AddressURLFormatErrorException('city is a required field')
    city = body['city']

    if not body.get('neighborhood'):
        raise AddressURLFormatErrorException('neighborhood is a required field')
    neighborhood = body['neighborhood']

    if not body.get('uf'):
        raise AddressURLFormatErrorException('uf is a required field')
    uf = body['uf']

    street = street.replace(' ', '+')
    city = city.replace(' ', '+')
    neighborhood = neighborhood.replace(' ', '+')
    uf = uf.replace(' ', '+')
    google_api_key = settings.GOOGLE_API_KEY

    url = 'https://maps.googleapis.com/maps/api/geocode/json?address={}+{}+{}+{}&key={}'.format(
        street,
        neighborhood,
        city,
        uf,
        google_api_key
    )

    return url
