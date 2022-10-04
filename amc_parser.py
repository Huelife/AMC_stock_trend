"""
amc_parser.py: 
Parsing scraped AMC API data using Python:
creating a dataframe, sorting, editing, and
creating an XLSX(Excel) file with the data
"""

import json
import pandas as pd

#opening AMC json data
with open("AMC_data.json", "r") as infile:
  amc_data = json.load(infile)

  #putting data in a dataframe
  df = pd.DataFrame(amc_data["data"])

  #removing excess parts from date column
  df["date"] = df["date"].map(lambda x: str(x)[:-17])

  #sorting date column by ascending and reseting row count 1-250
  sort_df = df.sort_values(by="date", ascending=True).reset_index(drop=True)

  #changing column order to date > open > high > low > close > volume
  re_df = sort_df[["date","open","high","low","close","volume"]]

  #creating pandas excel using xlsxwriter
  writer = pd.ExcelWriter("AMC_data_sorted.xlsx", engine="xlsxwriter")

  #converting dataframe to an xlsxwriter excel
  re_df.to_excel(writer, sheet_name="AMC_Data")

  #creating excel file
  writer.save()
