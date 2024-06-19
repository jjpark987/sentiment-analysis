import asyncio
import uuid
from celery import shared_task
from playwright.async_api import async_playwright, Playwright
from ..browser_page import browser_page

@shared_task
def start_event_loop():
    return asyncio.run(main())

async def main():
    async with async_playwright() as playwright:
        return await run(playwright)

async def run(playwright: Playwright):
    chromium = playwright.chromium
    browser = await chromium.launch(headless=False)
    page = await browser.new_page()

    await page.goto("http://books.toscrape.com")

    await page.wait_for_timeout(3000)

    key = str(uuid.uuid4())
    browser_page[key] = (browser, page)

    return key
