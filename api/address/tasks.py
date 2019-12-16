from celery import shared_task
from celery.utils.log import get_task_logger

from django.conf import settings
from kombu import Connection, Exchange, Queue, Consumer
import socket

logger = get_task_logger(__name__)


@shared_task(queue='default')
def consumer_from_queue():
    connection = Connection(settings.BROKER_URL, heartbeat=10)
    connection.connect()

    exchange = Exchange('example-exchange', type='direct')

    queue = Queue(
        name='order-customer-queue',
        routing_key='address',
        exchange=exchange,
    )

    def process_message(body, message):
        logger.info('Message arrived with the following body {}'.format(body))
        message.ack()

    consumer = Consumer(connection, queues=queue, callbacks=[process_message], accept=["text/plain"])
    consumer.consume()

    def establish_connection():
        revived_connection = connection.clone()
        revived_connection.ensure_connection(max_retries=3)
        channel = revived_connection.channel()
        consumer.revive(channel)
        consumer.consume()
        return revived_connection

    def consume():
        new_connection = establish_connection()
        while True:
            try:
                new_connection.drain_events(timeout=2)
            except socket.timeout:
                new_connection.heartbeat_check()

    def run():
        logger.info('Starting consumer from address queue')
        while True:
            try:
                consume()
            except connection.connection_errors:
                logger.error('Something went wrong')
            finally:
                connection.close()

    run()


consumer_from_queue.delay()
