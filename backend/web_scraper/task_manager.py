from celery import chain
from .celery_tasks.get_products import get_products
from .celery_tasks.get_details import get_details
from .celery_tasks.get_reviews import get_reviews
from django_redis import get_redis_connection

class ScraperTaskManager:
    # def __init__(self, search_query=None, product_id=None):
    #     self.search_query = search_query
    #     self.product_id = product_id

    def start_scraper(self):
        # Call get_products without arguments (it doesn't require cachekey)
        cache_key = get_products.si()

        # Pass the retrieved cachekey directly within task references
        second_task = get_details.si(cache_key=cache_key)
        third_task = get_reviews.si(cache_key=cache_key)

        # Chain the tasks and apply them asynchronously
        return chain(cache_key | second_task | third_task).apply_async()
