#!/usr/bin/env python3
"""Module to scroll and scrape products from an infinite-scroll page."""

import time
from selenium import webdriver


def scroll_and_scrape(url, scroll_pause=2.0):
    """Scrolls to the bottom of a page and extracts unique products."""
    # Set up optimized headless browser options
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    # Block images from loading to speed up page rendering
    prefs = {"profile.managed_default_content_settings.images": 2}
    options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(options=options)
    driver.set_page_load_timeout(15)

    scrape_products = []
    seen_identifiers = set()

    try:
        driver.get(url)

        # --- PHASE 1: ULTRA-FAST HEIGHT-BASED SCROLLING ---
        last_height = driver.execute_script(
            "return document.body.scrollHeight"
        )

        while True:
            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);"
            )
            # --- ACTIVE WAITING REPLACEMENT
            start_time = time.time()
            while time.time() - start_time < scroll_pause:
                new_height = driver.execute_script(
                    "return document.body.scrollHeight"
                )
                # If the height has increased, new products
                if new_height > last_height:
                    break
                time.sleep(0.1)

            new_height = driver.execute_script(
                "return document.body.scrollHeight"
            )
            # If the page height didn't change, we are at the bottom
            if new_height == last_height:
                break
            last_height = new_height

        # --- PHASE 2: EXTRACT UNIQUE PRODUCTS (ONCE) ---
        product_cards = driver.find_elements("css selector", ".thumbnail")

        for card in product_cards:
            # Title
            title_el = card.find_element("css selector", "a.title")
            title = title_el.get_attribute("title")

            # Price
            price = card.find_element("css selector", "h4.price").text

            # Description
            desc_el = card.find_element("css selector", "p.description")
            description = desc_el.text

            # Rating
            rating_elements = card.find_elements(
                "css selector", ".ratings .ws-icon-star"
            )
            rating = len(rating_elements)

            # Track unique items strictly by (title, price) pairs
            product_identifier = (title, price)
            if product_identifier not in seen_identifiers:
                seen_identifiers.add(product_identifier)
                scrape_products.append({
                    "title": title,
                    "price": price,
                    "description": description,
                    "rating": rating
                })

    finally:
        driver.quit()

    return scrape_products
