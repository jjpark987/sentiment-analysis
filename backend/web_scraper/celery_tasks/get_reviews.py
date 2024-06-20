from celery import shared_task
from django_redis import get_redis_connection

@shared_task
async def get_reviews(cache_key):
    # Retrieve browser and page objects from Redis using the cache key
    connection = get_redis_connection()
    browser, page = connection.get(cache_key)

    # scrape reviews from product page
    # ...

    await browser.close()

    connection.delete(cache_key)
