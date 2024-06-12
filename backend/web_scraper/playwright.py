from playwright.async_api import async_playwright
import asyncio

async def test_async_method():
    try:
        for _ in range(3):  # Output something every 30 seconds for 2 minutes
            print('Playwright is running...')
            await asyncio.sleep(5)
    finally:
        print('Playwright has stopped.')

    # async with async_playwright() as playwright:
    #     chromium = playwright.chromium
    #     browser = await chromium.launch()
    #     page = await browser.new_page()
    #     # await page.goto("https://www.amazon.com/ref=nav_logo")
    #     await page.goto('https://www.google.com')
    