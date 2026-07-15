#!/usr/bin/env python3
"""function that opens a static product category page
returning a list of product dictionary"""

import time
from selenium import webdriver


def scrape_products_list(url):
    """
    result: lists of product dictionaroes
    "title": the product’s name (from the title attribute of the
    <a> tag)
    "price": the product’s price (text of the <h4 class="price">
    element)
    "description": the product’s description (text of the
    <p class="description">)
    "rating": the number of stars
    (<p data-rating="rating_value"> under .ratings)
    """
    """
    options = webdriver.chrome.options
    # modern headless mode
    options.add_argument("--headless=new")
    # real desktop viewport
    options.add_argument("--window-size=1920,1080")
    # needed in many containers
    options.add_argument("--no-sandbox")
    # avoid / dev/shm crashes in Docker
    """
    # define options
    browser_options = webdriver.ChromeOptions()
    browser_options.headless = True
    # define 1920 1080 window
    browser_options.add_argument("--window-size=1920,1080")
    browser_options.add_argument("--no-sandbox")
    # prevents memory crashes
    browser_options.add_argument("--disable-dev-shm-usage")
    

    # open a driver
    driver = webdriver.Chrome(options=browser_options)
    driver.get(url)
    time.sleep(5)
    # how to treat cookies


    # print(driver.page_source) # helfer
    
    products = []
    try:
        # find all product cards on the page
        product_cards = driver.find_elements("class name", "thumbnail")

        #print(product_cards)
        # need to loop through one by one
        for card in product_cards:
            # Title: find the <a> tag with class "title" and get its "tittle attribute"
            title_element = card.find_element("class name", "title")
            title = title_element.get_attribute("title")
            # price <h4 class="price">
            price = card.find_element("class name", "price").text
            # description <p class="description">
            description = card.find_element("class name", "description").text
            # rating: element under class ".ratings" & data-rating attribute
            # needs CSS selector
            rating_element = card.find_element("css selector", ".ratings p[data-rating]")
            rating_value = rating_element.get_attribute("data-rating")
            rating = int(rating_value) if rating_value else 0

            # store data
            products.append( {
                "title": title,
                "price": price,
                "description": description,
                "rating": rating
            })

    finally:
        driver.quit()



        # div class="product-wrapper card-body">
        # <a href="/test-sites/e-commerce/static/product/33" class="title" title="ThinkPad T540p" itemprop="name"> ThinkPad T540p
        #  <p class="description card-text" itemprop="description">15.6", Core i5-4200M, 4GB, 500GB, Win7 Pro 64bit</p>
        #   <h4 class="price float-end card-title pull-right" itemprop="offers" itemscope="" itemtype="https://schema.org/Offer">
        # <span itemprop="price">$739.99</span>
        # <meta itemprop="priceCurrency" content="USD">
        # print(product) # helper

    return products