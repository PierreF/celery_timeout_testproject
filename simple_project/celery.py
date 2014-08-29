from __future__ import absolute_import

import time
import os

from celery import Celery

from django.conf import settings

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'simple_project.settings')

app = Celery('proj')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(soft_time_limit=2, time_limit=3)
def take_time(delay=5):
    """ Request which took some time
    """
    print('Started on %s' % os.getpid())
    time.sleep(delay)
    print('Task finished on %s' % os.getpid())
