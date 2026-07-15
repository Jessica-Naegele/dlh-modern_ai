#!/usr/bin/env python3
"""Function that scrolls and extracts products from an infinite-scroll page"""

import time
from selenium import webdriver


def scroll_and_scrape(url, scroll_pause=2.0):
    """Opens an infinite scroll page in headless Chrome, scrolls to the bottom,
    extracts unique product cards, and returns them in a list of dicts.
    """
    # Set up optimized headless browser options
    browser_options = webdriver.ChromeOptions()
    browser_options.add_argument("--headless=new")
    # Modern headless mode (faster & more stable)
    browser_options.add_argument("--window-size=1920,1080")
    browser_options.add_argument("--no-sandbox")
    browser_options.add_argument("--disable-dev-shm-usage")
    browser_options.add_argument("--disable-gpu")
    # Speeds up startup in headless/Docker environments

    driver = webdriver.Chrome(options=browser_options)

    scrape_products = []
    seen_identifiers = set()

    try:
        driver.get(url)
        time.sleep(scroll_pause)

        # --- PHASE 1: SCROLL UNTIL NO NEW PRODUCTS LOAD ---
        last_product_count = 0
        scroll_attempts = 0
        max_scroll_attempts = 25  # Safety cap to prevent sandbox timeouts

        while scroll_attempts < max_scroll_attempts:
            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);"
                )
            time.sleep(scroll_pause)

            # Check how many cards have loaded so far
            current_cards = driver.find_elements("css selector", ".thumbnail")
            current_product_count = len(current_cards)

            # If the count didn't increase, we have loaded all items
            if (
                current_product_count == last_product_count
                and current_product_count > 0
            ):
                break

            last_product_count = current_product_count
            scroll_attempts += 1

        # --- PHASE 2: EXTRACT UNIQUE PRODUCTS ---
        product_cards = driver.find_elements("css selector", ".thumbnail")

        for card in product_cards:
            # Title
            title_element = card.find_element("css selector", "a.title")
            title = title_element.get_attribute("title")

            # Price
            price = card.find_element("css selector", "h4.price").text

            # Description
            description = card.find_element(
                "css selector", "p.description"
                ).text

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
