from api.address.validations import AddressURLFormatErrorException


def build_google_maps_address(address_message):
    address = ''
    if not address_message.get('street'):
        raise AddressURLFormatErrorException('street is a required field')
    street = address_message['street']

    address += street

    if not address_message.get('city'):
        raise AddressURLFormatErrorException('city is a required field')
    city = address_message['city']

    address += ', ' + city

    if not address_message.get('neighborhood'):
        raise AddressURLFormatErrorException('neighborhood is a required field')
    neighborhood = address_message['neighborhood']

    address += ', ' + neighborhood

    if not address_message.get('uf'):
        raise AddressURLFormatErrorException('uf is a required field')
    uf = address_message['uf']

    address += ', ' + uf

    return address
