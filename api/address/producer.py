from celery.utils.log import get_task_logger
from django.conf import settings

from api.celery import app

from kombu import Connection, Exchange, Producer, Queue


logger = get_task_logger(__name__)


@app.task
def publish_metadata(address_id, geo_location):
    connection = Connection(settings.BROKER_URL)
    connection.connect()
    channel = connection.channel()

    exchange = Exchange('example-exchange', type='direct')

    producer = Producer(
        channel=channel,
        routing_key='geolocation',
        exchange=exchange,
    )
    queue = Queue(
        name='order-address-queue',
        routing_key='geolocation',
        exchange=exchange,
    )

    geo_location.update({'id': address_id})

    queue.maybe_bind(connection)
    queue.declare()
    producer.publish(geo_location)

