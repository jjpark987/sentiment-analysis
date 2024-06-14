import asyncio
from ..celery import app
from playwright.async_api import async_playwright, Playwright

@app.task
def start_event_loop():
    asyncio.run(main())

async def main(search_query):
    async with async_playwright() as playwright:
        await run(playwright)

async def run(playwright: Playwright):
    chromium = playwright.chromium
    browser = await chromium.launch(headless=False)
    page = await browser.new_page()

    await page.goto("http://books.toscrape.com")

    await browser.close()
