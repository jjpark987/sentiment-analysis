import os
from django.conf import settings
from celery import Celery

# This sets the DJANGO_SETTINGS_MODULE environment variable to 'backend.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
# Create a Celery instance named 'web_scraper'
app = Celery('web_scraper')
# Configure the Celery app using the Django settings
app.config_from_object('django.conf:settings', namespace='CELERY')
# Auto-discover Celery tasks in the Django project's INSTALLED_APPS
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

# Method that outputs information about current task
@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
