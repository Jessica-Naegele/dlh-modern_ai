#!/usr/bin/env python3
"""function that scrolls and extracts products"""

import time
from selenium import webdriver


def scroll_and_scrape(url, scroll_pause=2.0):
    """function scrolling and extracting all products
    - open infinite scroll page in headless Chrome
    - scroll to the bottom repeatedly, waiting scroll_pause 
    until page height stops increasing
    - find every div.thumbnail product card and extracts
      - title: < a class="title">
      - price (<h4 class = price")
      - description <p class=description>
      - rating <count number of <p class="ws-icon ws-icon-star"> under .ratings

      - skip duplicate products by tracking (title, price) pairs
      return a list of unique products dicts
      - use exectute script for scrolling    
    """
     # set up browser and browser options
    browser_options = webdriver.ChromeOptions()
    browser_options.add_argument("--headless")
    browser_options.add_argument("--window-size=1920,1080")
    browser_options.add_argument("--no-sandbox")
    browser_options.add_argument("--disable-dev-shm-usage")

    # access website
    driver = webdriver.Chrome(options=browser_options)
  

    # store list of products
    scrape_products = []
    seen_identifiers = set()

    try:
        driver.get(url)
        time.sleep(scroll_pause)
    
        last_height = driver.execute_script("return document.body.scrollHeight")
        while True:
            # scroll to the bottom to trigger next batch
            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);"
                )
            time.sleep(scroll_pause)

            # continue while
            new_height = driver.execute_script(
                "return document.body.scrollHeight"
                )
            if new_height == last_height:
                break  # Bottom reaced
            last_height = new_height
        
        # extract the info all in once
        product_cards = driver.find_elements("css selector", ".thumbnail")

        for card in product_cards:
            # Title: find the <a> tag with class "title"
            title_value = card.find_element("css selector", "a.title")
            title = title_value.get_attribute("title")
            # price <h4 class="price">
            price = card.find_element("css selector", "h4.price").text
            # description <p class="description">
            description = card.find_element(
                "css selector", "p.description"
                ).text
            # rating: element under class ".ratings"
            # needs CSS selector
            rating_element = card.find_elements("css selector",
                                            ".ratings .ws-icon-star")
            rating = len(rating_element)

            # store data
            product_identifier = (title, price)
            if product_identifier not in seen_identifiers:
                seen_identifiers.add(product_identifier)
                            
                scrape_products.append(
                    {
                    "title": title,
                    "price": price,
                    "description": description,
                    "rating": rating
                    }
                )
        
    finally:
        driver.quit()

    return scrape_products
