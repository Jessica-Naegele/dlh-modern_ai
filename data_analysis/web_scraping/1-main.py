#!/usr/bin/env python3
import json
fetch_html = __import__('0-fetch_html').fetch_html

scrape_basic = __import__('1-scrape_basic').scrape_basic
data = scrape_basic("https://quotes.toscrape.com/")
print(json.dumps(data[:2], indent=2))


#print(fetch_html("https://quotes.toscrape.com/"))