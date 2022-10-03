"""
amc_api.py: 
Scraping AMC API from: https://www.stockdata.org/
using Python
"""

import webbrowser

import requests
from requests.exceptions import HTTPError
from requests import get

api_key = input("API Key: ")
url = (f"https://api.stockdata.org/v1/data/eod?"
        "symbols=AMC&api_token={api_key}")

r = requests.get(url)
data = r.raw.read()

print(data)
