from celery import shared_task
from django_redis import get_redis_connection
from playwright.async_api import async_playwright
import uuid

@shared_task
async def get_reviews(session_id):
    async with async_playwright() as playwright:
        # Retrieve the page URL from the Redis cache using the session ID
        redis_conn = get_redis_connection()
        url = redis_conn.get(session_id).decode('utf-8')
        if not url:
            raise Exception("URL not found in Redis cache")
        
        browser = await playwright.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto(url)

        print('Task 3 is running')

        # scrape details of a selected product
        # ...

        await browser.close()

        # Clear cache
        redis_conn.delete(session_id)
        redis_conn.flushdb()

        return {'task3 return message': 'task3 completed'}
