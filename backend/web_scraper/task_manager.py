from celery import chain
from .celery_tasks.start_playwright import start_event_loop
from .celery_tasks.get_products import search_for_products
# from .celery_tasks.get_details import find_product_details
# from .celery_tasks.get_reviews import find_product_reviews

class ScraperTaskManager:
    # def __init__(self, search_query=None, product_id=None):
    #     self.search_query = search_query
    #     self.product_id = product_id

    def start_scraper(self):
        return chain(
            start_event_loop.s() |
            search_for_products.s()
        ).apply_async()
    
        # return chain(
        #     start_event_loop.s() | 
        #     search_for_products.s() | 
        #     find_product_details.s() | 
        #     find_product_reviews.s()
        # ).apply_async()
