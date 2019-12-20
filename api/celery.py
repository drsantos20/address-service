import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api.settings')

app = Celery('api', include=['api.address.tasks'])
app.config_from_object('django.conf:settings', namespace='CELERY')
# app.conf.task_routes = {'api.order.consumer.consumer_from_queue': {'queue:' 'order-customer-queue'}}


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
