import requests
from django.conf import settings


def get_reverse_location(message):
    google_api_key = settings.GOOGLE_API_KEY

    # todo get the ID from address

    response = requests.get(
        'https://maps.googleapis.com/maps/api/geocode/json?address=Rua+Nelson+Fernandes+450+Cidade+Vargas+Sao+Paulo,+SP&key={}'.format(google_api_key))
    resp_json_payload = response.json()
    print(resp_json_payload)
    print(resp_json_payload['results'][0]['geometry']['location'])
