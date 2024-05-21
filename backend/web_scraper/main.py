import os
import asyncio
import pprint
import urllib.parse
from pymongo import MongoClient
from playwright.async_api import async_playwright, Playwright
from typing import List

# connection_string = f'mongodb+srv://jjpark987:{urllib.parse.quote_plus(os.environ.get('MONGODB_PWD'))}@sentimentanalysis.pnbmoui.mongodb.net/'
# mongo_client = MongoClient(connection_string)
# web_scraper_db = mongo_client.web_scraper
# products_col = web_scraper_db.products
# printer = pprint.PrettyPrinter()

# # create
# def insert_product_docs():
#     test_doc = {
#         'name': 'winter gloves',
#         'type': 'test'
#     }
#     inserted_id = products_col.insert_one(test_doc).inserted_id
#     print(inserted_id)

# # read
# def find_all_products():
#     products = products_col.find()

#     list(products)

#     # for product in products:
#     #     printer.pprint(product)       


async def search_for_product(keyword):
    pass

async def scrape_product_details(product_id):
    pass

async def scrape_reviews(product_id):
    pass

async def main():
    async with async_playwright() as playwright:
        chromium = playwright.chromium
        browser = await chromium.launch()
        page = await browser.new_page()
        await page.goto("https://www.amazon.com/ref=nav_logo")
        
        while True:
            keyword = await get_product_keyword()
            asyncio.create_task(search_for_product(keyword))
            
            # product_id = await get_product_id()
            # asyncio.create_task(scrape_product_details(product_id))

            # initiate = await get_analysis_request()
            # asyncio.create_task(scrape_reviews(initiate, product_id))

        await browser.close()

async def run(playwright: Playwright, keyword, product_id):
    

    # when frontend user enters a product keyword to search
    # how do i get keyword from frontend -> backend -> here?
    products = await search(page, keyword)
    await save_products(products)
    await to_api(products)
    
    # when frontend user selects a specific product from the list
    # same question how do i get the user's selection?
    product = await get_product_details(page, product_id)
    await save_product_details(product)

    # when frontend user executes the analysis
    # i need the indication from frontend to start the analysis
    reviews = await get_product_reviews(page)
    await save_product_reviews(reviews)

    


async def search(page, keyword) -> List[dict]:
    pass
    # search for a product keyword on Amazon
    # scrape the first five products
    # for each product scrape
        # name
        # image_url
        # seller
        # latest_price
    # return list of dict each representing product


async def save_products(products: List[dict]):
    pass
    # create or save this to PyMongo: each product is a new document in the products collection
    # make sure to also include
        # created_at or updated_at depending on if it already exists or not based on name and seller? (not too sure about this)

async def to_api(products: List[dict]):
    pass
    # send to api

async def get_product_details(product_id):
    pass
    # go to product site on Amazon
    # scrape details on that product
        # description
        # category
        # url

async def save_product_details(product):
    pass
    # update to PyMongo: use product_id to find doc in product collections
    # make sure updated_at is also updated

async def get_product_reviews(page):
    pass
    # go to the product site and scroll down to link 'see more reviews' and click it
    # scrape the website for all the reviews
        # rating
        # title
        # location
        # date
        # comment
        # helpfulness
    # may need to click on next page to get all reviews
    # return a list of dictionaries each representing a review

async def save_product_reviews(reviews):
    pass
    # create new docs on PyMongo: include the same product_id for each review
    # created_at 

# run the main coroutine to start the event loop
# generates a coroutine object from coroutine function
asyncio.run(main())
