"""
amc_parser.py: 
Parsing scraped AMC API data using Python
"""

import json

#opening AMC json data
with open("AMC_data.json", "r") as infile:
  amc_data = json.load(infile)
