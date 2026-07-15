#!/usr/bin/env python3
"""function that opens a static product category page
returning a list of product dictionary"""

import time
from selenium import webdriver


def scrape_products(url):
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
    scrape_products = []
    try:
        # find all product cards on the page
        product_cards = driver.find_elements("class name", "thumbnail")

        # print(product_cards)
        # need to loop through one by one
        for card in product_cards:
            # Title: find the <a> tag with class "title" and get its attribute
            title_element = card.find_element("class name", "title")
            title = title_element.get_attribute("title")
            # price <h4 class="price">
            price = card.find_element("class name", "price").text
            # description <p class="description">
            description = card.find_element("class name", "description").text
            # rating: element under class ".ratings" & data-rating attribute
            # needs CSS selector
            rating_element = card.find_element("css selector",
                                               ".ratings p[data-rating]")
            rating_value = rating_element.get_attribute("data-rating")
            rating = int(rating_value) if rating_value else 0

            # store data
            scrape_products.append({
                "title": title,
                "price": price,
                "description": description,
                "rating": rating
            })

    finally:
        driver.quit()

    return scrape_products
