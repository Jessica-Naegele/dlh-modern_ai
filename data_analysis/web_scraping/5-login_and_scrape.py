#!/usr/bin/env python3
"""function that logs in and scrapes quotes"""

import requests
from bs4 import BeautifulSoup


def login_and_scrape(login_url, user, pwd):
    """TASK 5
    login_url is the login page
    GET the login form and extract the CSRF token from <input name="csrf_token">
    POST credential fields (username, password, csrf_token) back to login_url
    After successful login, GET the protected quotes page (https://quotes.toscrape.com/)
    Use BeautifulSoup to parse each <div class="quote"> and extract:
    "text": the quote text
    "author": the author’s name
    "tags": a list of tag strings
    """
    # create a session to maintain cookies
    session = requests.Session()

    # get login form and extract the CSRF token
    response = requests.get(login_url)
    response.raise_for_status()

    # <input type="hidden" name="csrf_token" value="jJgOuzpBfEvoliCsQUTSInWXbRkMDeyYarKdxGFPHhZwALtcNVqm"/>
    soup = BeautifulSoup(response.text, "html.parser")
    # print(f"soup: {soup}")
    token_element = soup.find("input", attrs={"name": "csrf_token", "type": "hidden"})
    csrf_token = token_element["value"]
    # print(f"csrf: {csrf_token}")

    # Post Login
    login_data = {
        'username': user,
        'password': pwd,
        'csrf_token': csrf_token
    }

    # perofrm login
    login_response = session.post(login_url, data=login_data)

    # request protected page
    protected_url = "https://quotes.toscrape.com/"
    authenticated_response = session.get(protected_url)

    soup = BeautifulSoup(authenticated_response.content, "html.parser")
    res = []

    # find correct class = quote
    quotes = soup.find_all('div', class_='quote')

    for quote in quotes:
        res_dict = {
            "text": quote.find('span', class_='text').text,
            # span class="text"
            "author": quote.find('small', class_='author').text,
            # <small class="author
            "tags": [tag.text for tag in quote.find_all('a', class_='tag')]
            # div class="tags"
        }

        res.append(res_dict)

    return res




