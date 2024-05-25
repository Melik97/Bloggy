import os

from celery import Celery

from bloggy.settings import RABBIT_BROKER_URL


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bloggy.settings")
app = Celery(
    "bloggy",
    broker=RABBIT_BROKER_URL,
    broker_connection_retry_on_startup=True,
)
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks(["api"])


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

