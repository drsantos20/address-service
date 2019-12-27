import unittest
from unittest import mock
from unittest.mock import Mock

from api.address.producer import send_geo_location_to_queue
from api.celery import app


class TestProducer(unittest.TestCase):

    def setUp(self):
        app.conf.update(CELERY_ALWAYS_EAGER=True)

    @mock.patch('api.address.producer.send_geo_location_to_queue')
    def test_send_geo_location(self, mock_utils):
        geo_location = {'lat': -23.67832, 'lng': -46.6021609, 'id': 184}

        producer = Mock()
        producer.loads(send_geo_location_to_queue(address_id='1', geo_location=geo_location))

        producer.loads.assert_called()
        producer.loads.assert_called_once()
