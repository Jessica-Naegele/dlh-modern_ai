#!/usr/bin/env python3
"""function that fetches a web page and reutrns its HTML as text"""

import requests


def fetch_html(url, headers=None, timeout=10):
    """function fetching a webpage and returning its HTML as text
    url is the page to retrieve
    headers is an optional dict of HTTP headers (e.g. {"User-Agent": "…”})
    timeout is the number of seconds to wait before aborting
    Must raise an exception on any HTTP status ≥400
    Returns: the full HTML of the response as a string
    """
    response = requests.get(url, headers=headers, timeout=timeout)
    response.raise_for_status()
    html_text = response.text
    return html_text
