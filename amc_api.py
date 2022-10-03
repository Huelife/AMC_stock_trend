"""
amc_api.py: 
Scraping AMC API from: https://www.stockdata.org/
using Python
"""

import webbrowser

import json
import requests
from requests.exceptions import HTTPError
from requests import get

api_key = input("API Key: ")
link = ("https://api.stockdata.org/v1/data/eod?"
        "symbols=AMC&api_token={}".format(api_key))

for url in [link]:
  try:
    response = requests.get(url)
    json_data = response.json()
    response.raise_for_status()
  except HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
  except Exception as err:
    print(f"Other error occurred: {err}")
  else:
    print("Success!")
    json.dump(json_data, open("AMC_data.json", "w"))
    file.close()
