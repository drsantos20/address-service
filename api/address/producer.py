from celery.utils.log import get_task_logger

from api.address.models.address import UserOrderAddress
from api.celery import app

logger = get_task_logger(__name__)


@app.task
def publish_metadata(address_id, geo_location):
    address = UserOrderAddress.objects.get(id=address_id)
    address.latitude = geo_location['lat']
    address.longitude = geo_location['lng']
    address.save()
