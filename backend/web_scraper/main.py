import os
import asyncio
import urllib.parse
from pymongo import MongoClient
from playwright.async_api import async_playwright, Playwright
from typing import List

connection_string = f'mongodb+srv://jjpark987:{urllib.parse.quote_plus(os.environ.get('MONGODB_PWD'))}@sentimentanalysis.pnbmoui.mongodb.net/'
mongo_client = MongoClient(connection_string)
web_scraper_db = mongo_client.web_scraper

# create
def insert_product_doc():
    products_col = web_scraper_db.products
    test_doc = {
        'name': 'winter gloves',
        'type': 'test'
    }
    inserted_id = products_col.insert_one(test_doc).inserted_id
    print(inserted_id)

# read

# update


# async def run(playwright: Playwright, url: str):
#     chromium = playwright.chromium
#     browser = await chromium.launch()
#     page = await browser.new_page()
#     await page.goto("https://www.amazon.com/ref=nav_logo")

#     # 
    
#     # using a product id from the list of products
#     # go to the product site and scroll down to link 'see more reviews' and click it
#     # scrape the website for all the ratings and reviews
#         # may need to click on next page to get all reviews
#     # return a list of dictionaries each representing a review
#     await browser.close()

# async def main():
#     async with async_playwright() as playwright:
#         await run(playwright)

# async def search_products(url: str) -> List[dict]:
#     pass
#     # search for a product keyword on Amazon

# async def save(products: List[dict]):
#     pass
#     # save this to PyMongo: list of dictionaries each representing product

# async def to_api(products: List[dict]):
#     pass
#     # send to api

# asyncio.run(main())
