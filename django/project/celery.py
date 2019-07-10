import os
from celery import Celery

# set the default settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

app = Celery('mailape')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
