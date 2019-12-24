import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api.settings')

app = Celery('api', include=['api.address.consumer'])
app.config_from_object('django.conf:settings', namespace='CELERY')


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
