import requests
from django.conf import settings

from api.celery import app
from celery.utils.log import get_task_logger


from api.address.producer import publish_metadata
from api.address.utils import build_google_maps_url


logger = get_task_logger(__name__)


@app.task
def get_longitude_latitude(body):
    google_api_key = settings.GOOGLE_API_KEY

    try:
        url = build_google_maps_url(body, google_api_key)

        response = requests.get(
            url,
            timeout=5
        )

        logger.info('Google Maps API Response with HTTP Status {}'.format(response.status_code))

        resp_json_payload = response.json()
        geo_location = resp_json_payload['results'][0]['geometry']['location']
        publish_metadata(geo_location)

    except requests.exceptions.HTTPError as http_error:
        return "An Http Error occurred:" + repr(http_error)

    except requests.exceptions.ConnectionError as connection_error:
        return "An Error Connecting to the API occurred:" + repr(connection_error)

    except requests.exceptions.Timeout as time_out_error:
        return "A Timeout Error occurred:" + repr(time_out_error)

    except requests.exceptions.RequestException as unknown_error:
        return "An Unknown Error occurred" + repr(unknown_error)
