from django.conf import settings
from kombu import Connection, Exchange, Producer, Queue
from celery.utils.log import get_task_logger


from api.celery import app

logger = get_task_logger(__name__)


@app.task
def publish_metadata(message):
    connection = Connection(settings.BROKER_URL)
    connection.connect()
    channel = connection.channel()

    exchange = Exchange('example-exchange', type='direct')

    producer = Producer(
        channel=channel,
        routing_key='address-detail',
        exchange=exchange,
    )
    queue = Queue(
        name='order-address-queue',
        routing_key='address-detail',
        exchange=exchange,
    )

    logger.info('Starting Producer to Send Geo Location to {} queue'.format(queue.name))

    queue.maybe_bind(connection)
    queue.declare()
    producer.publish(message)
