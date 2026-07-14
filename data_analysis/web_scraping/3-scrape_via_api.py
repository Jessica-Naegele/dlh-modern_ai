#!/usr/bin/env python3
"""fetches quote data from all the quotes API pages"""

import json
fetch_html = __import__('0-fetch_html').fetch_html


def scrape_via_api(base_url):
    """ TASK 3
    fetches quote data fromm API pages
    base_url is the root URL of the site (e.g. "https://quotes.toscrape.com")
    Build each page’s API endpoint starting from page one (/api/quotes?page=1)
    Use fetch_html() to retrieve the JSON payload
    From each page’s "quotes" array, extract:
    "text": the quote text
    "author": the author’s name
    "tags": the list of tags
    """
    # get data
    quotes = []
    page_number = 1

    # construct website
    url = f"{base_url}/api/quotes?page={page_number}"

    # fetch data
    t = fetch_html(url)
    # print(f"text: {text}") # helper
    data = json.loads(t)

    # calculate how often to move on
    i = 0
    while data['has_next']:
        i += 1
        url = f"{base_url}/api/quotes?page={i}"
        t = fetch_html(url)
        data = json.loads(t)

        # prepare data like regquested
        for quote in data["quotes"]:
            # print(f"quote: {quote}")

            cur_dict = {
                "text": quote['text'],
                "author": quote['author']['name'],
                "tags": quote['tags']
            }
            quotes.append(cur_dict)

    return quotes
