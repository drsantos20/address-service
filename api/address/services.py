import requests
from django.conf import settings

from api.address.utils import build_google_maps_url
from api.celery import app


@app.task
def get_longitude_latitude(body):
    google_api_key = settings.GOOGLE_API_KEY

    url = build_google_maps_url(body, google_api_key)

    response = requests.get(
        url
    )
    resp_json_payload = response.json()
    print(resp_json_payload)
    print(resp_json_payload['results'][0]['geometry']['location'])
