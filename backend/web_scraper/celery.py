import os
from celery import Celery
from django.conf import settings

# This sets the DJANGO_SETTINGS_MODULE environment variable to 'backend.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

# Create a Celery instance named 'web_scraper'
app = Celery('web_scraper')

# Configure the Celery app using the Django settings
app.config_from_object('django.conf:settings', namespace='CELERY')

# Auto-discover Celery tasks in the Django project's INSTALLED_APPS
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

# Set the broker URL
app.conf.broker_url = 'redis://localhost:6379/0'

# Timezone for Celery
app.conf.timezone = 'UTC'

# Enables broker connection retries on startup
app.conf.broker_connection_retry_on_startup = True

# Method that outputs information about current task
@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
