from celery import shared_task
from ..browser_page import browser_page

@shared_task
async def search_for_products(key):
    browser, page = browser_page.get(key, (None, None))

    if not browser or not page:
        raise ValueError("Invalid key, browser or page not found.")

    await page.goto("https://books.toscrape.com/catalogue/category/books/horror_31/index.html")
    await page.wait_for_timeout(3000)

    return key