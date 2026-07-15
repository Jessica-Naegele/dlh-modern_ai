#!/usr/bin/env python3
"""write a function opening a detail page for one product"""

import time
from selenium import webdriver


def scrape_product_detail(url, delay=2.0):
    """
    "title": the product title (the second <h4> inside .caption)
    "price": the price (text of the first <h4 class="price">)
    "description": the full description (text of
    <p class="description">)
    "rating": the number of stars (count of
    <p class="ws-icon ws-icon-star"> in .ratings)
    """
    # set up browser and browser options
    browser_options = webdriver.ChromeOptions()
    browser_options.add_argument("--headless")
    browser_options.add_argument("--window-size=1920,1080")
    browser_options.add_argument("--no-sandbox")
    browser_options.add_argument("--disable-dev-shm-usage")

    # access website
    driver = webdriver.Chrome(options=browser_options)
    driver.get(url)
    time.sleep(delay)

    # print(driver.page_source) # helfer

    # find details and store it in list
    product = []
    try:
        # product_cards = driver.find_elements("class name", "caption")
        # "title": the product title (the second <h4> inside .caption)
        title = driver.find_element(
            "css selector", ".caption h4:nth-of-type(2)"
            ).text.strip()
        # "price": the price (text of the first <h4 class="price">)
        price = driver.find_element("class name", "price").text
        # "description": the full description (text of
        # <p class="description">)
        description = driver.find_element(
            "class name", "description"
            ).text.strip()
        # "rating": the number of stars (count of
        # <p class="ws-icon ws-icon-star"> in .ratings)
        rating_element = driver.find_elements(
            "css selector", ".ratings .ws-icon-star"
            )
        rating = len(rating_element)

        # print(f"rating_element: {rating_element}")

        # store data
        product = {
            "title": title,
            "price": price,
            "description": description,
            "rating": rating
        }

        # print(product)
    finally:
        driver.quit()

    return product
