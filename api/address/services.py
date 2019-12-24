import requests
import googlemaps

from api.celery import app
from celery.utils.log import get_task_logger


from api.address.producer import send_geo_location_to_queue
from api.address.utils import build_google_maps_address
from api.settings import GOOGLE_API_KEY

logger = get_task_logger(__name__)


@app.task(autoretry_for=(Exception,), retry_kwargs={'max_retries': 5, 'countdown': 2})
def get_longitude_latitude(address_message):

    try:
        address = build_google_maps_address(address_message)
        google_maps = googlemaps.Client(key=GOOGLE_API_KEY)
        google_maps_response = google_maps.geocode(address)

        geo_location = google_maps_response[0].get('geometry').get('location')

        logger.info('Google Maps API Response with the following geometry {}'.format(geo_location))
        send_geo_location_to_queue(address_id=address_message['id'], geo_location=geo_location)

    except requests.exceptions.HTTPError as http_error:
        return 'An Http Error occurred:' + repr(http_error)

    except requests.exceptions.ConnectionError as connection_error:
        return 'An Error Connecting to the API occurred:' + repr(connection_error)

    except requests.exceptions.Timeout as time_out_error:
        return 'A Timeout Error occurred:' + repr(time_out_error)

    except requests.exceptions.RequestException as unknown_error:
        return 'An Unknown Error occurred' + repr(unknown_error)
