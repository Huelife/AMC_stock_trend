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
link = ("https://api.stockdata.org/v1/data/eod?"
        "symbols=AMC&api_token={}".format(api_key))

response = requests.get(url)
