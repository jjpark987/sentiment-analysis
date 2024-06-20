from celery import shared_task
from playwright.async_api import async_playwright, Playwright
from django_redis import get_redis_connection
import uuid

@shared_task
async def get_products():
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=False)
        page = await browser.new_page()
        print('START_PLAYWRIGHT HAS STARTED AND IT IS WORKING RIGHT NOW')
        await page.goto("http://books.toscrape.com")

        await page.wait_for_timeout(3000)

        # code to search on Amazon
        # ...

        # Generate a unique key for cache entry
        cache_key = f"playwright_objects_{uuid.uuid4()}"

        # Store browser and page objects in Redis cache
        get_redis_connection().set(cache_key, (browser, page))

        # Return the cache key for subsequent tasks
        return cache_key
