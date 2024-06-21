from celery import shared_task
from playwright.async_api import async_playwright
from django_redis import get_redis_connection
import uuid
import random
from playwright_stealth import stealth_async

@shared_task
async def get_products(search_query):
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=False)
        page = await browser.new_page()
        await stealth_async(page)

        await page.goto("https://www.amazon.com/Logitech-Wireless-Mouse-M185-Swift/product-reviews/B004YAVF8I/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews")

        # Generate a unique session ID
        session_id = str(uuid.uuid4())

        await browser.close()

        # Store the page URL in the Redis cache using the session ID as the key
        get_redis_connection().set(session_id, page.url)

        # Return the session ID for subsequent tasks
        return session_id
