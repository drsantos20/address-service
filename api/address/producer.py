from celery.utils.log import get_task_logger
from django.conf import settings

from api.celery import app

from kombu import Connection, Exchange, Producer, Queue

from api.address.constants import (
    ADDRESS_EXCHANGE,
    ADDRESS_CUSTOMER_PRODUCER_ROUTING_KEY,
    ADDRESS_CUSTOMER_PRODUCER_QUEUE,
)

logger = get_task_logger(__name__)


@app.task
def send_geo_location_to_queue(address_id, geo_location):
    with Connection(settings.BROKER_URL) as connection:
        connection.connect()
        channel = connection.channel()

        exchange = Exchange(ADDRESS_EXCHANGE, type='direct')

        producer = Producer(
            channel=channel,
            routing_key=ADDRESS_CUSTOMER_PRODUCER_ROUTING_KEY,
            exchange=exchange,
        )
        queue = Queue(
            name=ADDRESS_CUSTOMER_PRODUCER_QUEUE,
            routing_key=ADDRESS_CUSTOMER_PRODUCER_ROUTING_KEY,
            exchange=exchange,
        )

        geo_location_from_address = geo_location
        geo_location_from_address.update({'id': address_id})

        queue.maybe_bind(connection)
        queue.declare()
        producer.publish(geo_location_from_address)
        connection.close()
