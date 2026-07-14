#!/usr/bin/env python3
"""Task 2: function that follows Next links"""

from bs4 import BeautifulSoup
import time
from urllib import parse
fetch_html = __import__('0-fetch_html').fetch_html
scrape_basic = __import__('1-scrape_basic').scrape_basic


def scrape_paginated(base_url):
    """function follows Next links
    base_url is the first page URL (https://quotes.toscrape.com/)
    Must detect and follow the <li class="next"><a href="…"> link dynamically
    Implement delays between requests (e.g. time.sleep)
    Combine results from all pages into one list
    Returns: the full list of quote dicts (same format as Task 1)
    """
    # step 0 prepare soup
    page = fetch_html(base_url)
    soup = BeautifulSoup(page, "html.parser")

    # step 1 find next? <li class="next"><a href="…">
    next = soup.find("li", class_='next')
    # print(f"next: {next}")
    text = []
    text += scrape_basic(base_url)
    if next is None:
        pass
    else:
        url = next.find('a').get('href')
        current_url = parse.urljoin(base_url, url)
        # print(f"current_url:  {current_url}")  # helper
        text += scrape_paginated(current_url)
    return text

