from celery import shared_task
from django_redis import get_redis_connection
import uuid

@shared_task
async def get_details(cache_key):
    # Retrieve browser and page objects from Redis using the cache key
    connection = get_redis_connection()
    browser, page = connection.get(cache_key)

    # scrape details of a selected product
    # ...

    # Generate a unique key for cache entry
    cache_key = f"playwright_objects_{uuid.uuid4()}"

    # Store browser and page objects in Redis cache
    get_redis_connection().set(cache_key, (browser, page))

    # Return the cache key for subsequent tasks
    return cache_key
