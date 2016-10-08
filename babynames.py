"""NYC BABY NAMES"""
# https://data.cityofnewyork.us/api/views/25th-nujf/rows.json?accessType=DOWNLOAD
import requests
import json
import pandas as pd

response = requests.get("https://data.cityofnewyork.us/api/views/25th-nujf/rows.json?accessType=DOWNLOAD")
text = response.text

namedict = json.loads(text)

namedict.keys()

namedict["data"][0]

alist = []

for row in namedict["data"]:
    temp = {}
    temp["Year"] = int(row[8])
    temp["Gender"] = row[9]
    temp["Race"] = row[10]
    temp["Name"] = row[11]
    temp["Count"] = int(row[12])
    alist.append(temp)

namedf = pd.DataFrame(alist)

