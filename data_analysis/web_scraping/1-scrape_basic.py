#!/usr/bin/env python3
"""function scraping first page of quotes"""

from bs4 import BeautifulSoup
fetch_html = __import__('0-fetch_html').fetch_html


def scrape_basic(url):
    """
    scarping first page
    Use fetch_html() to retrieve the HTML then parse it with BeautifulSoup
    Extract for each quote block:
    "text": the quote text
    "author": the quote’s author
    "tags": a list of tag strings
    You are not allowed to use regular expressions for this task
    """
    page = fetch_html(url)
    # parse the page
    soup = BeautifulSoup(page, "html.parser")
    res = []
    
    # find correct class = quote
    quotes = soup.find_all('div', class_='quote')

    for quote in quotes:
        
        res_dict = {
            "text" : quote.find('span', class_='text').text,  # span class="text"
            "author" : quote.find('small', class_='author').text,  # <small class="author
            "tags" : [tag.text for tag in quote.find_all('a', class_='tag')]  # div class="tags"
        }

        res.append(res_dict)
    
    return res
