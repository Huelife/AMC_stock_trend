"""
amc_parser.py: 
Parsing scraped AMC API data using Python
"""

import json
import pandas as pd

#opening AMC json data
with open("AMC_data.json", "r") as infile:
  amc_data = json.load(infile)

  #putting data in a dataframe
  df = pd.DataFrame(amc_data["data"])
