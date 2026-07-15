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

    # Block images to save precious loading bandwidth and time
    prefs = {"profile.managed_default_content_settings.images": 2}
    options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(options=options)
    driver.set_page_load_timeout(15)

    scrape_products = []
    seen_identifiers = set()

    try:
        driver.get(url)

        # --- PHASE 1: ACTIVE-WAITING SCROLLING ---
        last_height = driver.execute_script(
            "return document.body.scrollHeight"
        )

        while True:
            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);"
            )

            # Check page height every 0.1s up to the scroll_pause limit
            start_time = time.time()
            while time.time() - start_time < scroll_pause:
                new_height = driver.execute_script(
                    "return document.body.scrollHeight"
                )
                if new_height > last_height:
                    break
                time.sleep(0.1)

            new_height = driver.execute_script(
                "return document.body.scrollHeight"
            )
            if new_height == last_height:
                break
            last_height = new_height

        # --- PHASE 2: BULK EXTRACTION (LIGHTNING FAST) ---
        # We fetch all elements of each type in single, bulk queries
        titles = driver.find_elements("css selector", ".thumbnail a.title")
        prices = driver.find_elements("css selector", ".thumbnail h4.price")
        descs = driver.find_elements(
            "css selector", ".thumbnail p.description"
            )
        ratings_containers = driver.find_elements(
            "css selector", ".thumbnail .ratings"
        )

        # Iterate through the elements using their matched index
        for i in range(len(titles)):
            title = titles[i].get_attribute("title")
            price = prices[i].text
            description = descs[i].text

            # Count stars within the specific rating container
            stars = ratings_containers[i].find_elements(
                "css selector", ".ws-icon-star"
            )
            rating = len(stars)

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
