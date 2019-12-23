import unittest
from unittest import mock
from unittest.mock import Mock

from api.address.producer import publish_metadata
from api.celery import app


class TestProducer(unittest.TestCase):

    def setUp(self):
        app.conf.update(CELERY_ALWAYS_EAGER=True)

    @mock.patch('api.address.producer.publish_metadata')
    def test_send_geo_location(self, mock_utils):
        geo_location = {'lat': -23.67832, 'lng': -46.6021609, 'id': 184}

        producer = Mock()
        producer.loads(publish_metadata(address_id='1', geo_location=geo_location))

        producer.loads.assert_called()
        producer.loads.assert_called_once()
