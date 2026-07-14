#!/usr/bin/env python3
"""
function that pulls quotes from embedded JSON-LD on a page
"""

import json
from bs4 import BeautifulSoup
fetch_html = __import__('0-fetch_html').fetch_html


def extract_jsonld(url):
    """TASK 4
    url is the Quotes List endpoint (e.g. "https://quotes.toscrape.com/")
    Use fetch_html() to fetch the HTML
    Locate all <script type="application/ld+json">
    blocks and parse each with json.loads()
    From each JSON‑LD object of "@type": "Quote", extract:
    "text": the quote text (.get("text"))
    "author": the author’s name (.get("author",
    {}).get("name"))
    "tags": keywords, (p.s. split into a list if provided as a
    comma-separated string)
    """
    # fetch the data
    page = fetch_html(url)
    soup = BeautifulSoup(page, "html.parser")
    # print(f"soup: {soup}")

    data = soup.find_all("script", type="application/ld+json")
    # print(f"data: {data}")

    t = []
    for quote in data:
        raw_json_str = quote.string
        json_data = json.loads(raw_json_str)
        cur_quote = {
            "text": json_data.get("text"),
            "author": json_data.get("author", {}).get("name"),
            "tags": json_data.get('keywords')
        }
        t.append(cur_quote)

    return t
