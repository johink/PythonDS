"""JSON"""
import json

#The json library can easily convert between JSON and dict formatting:

#Remember that three quotes means a multiline string as well as multiline comments
jsonstring = """{
  "firstName": "John",
  "lastName": "Smith",
  "isAlive": true,
  "age": 25,
  "address": {
    "streetAddress": "21 2nd Street",
    "city": "New York",
    "state": "NY",
    "postalCode": "10021-3100"
  },
  "phoneNumbers": [
    {
      "type": "home",
      "number": "212 555-1234"
    },
    {
      "type": "office",
      "number": "646 555-4567"
    },
    {
      "type": "mobile",
      "number": "123 456-7890"
    }
  ],
  "children": [],
  "spouse": null
}"""

#json.loads() turns a JSON string into a Python dict
mydict = json.loads(jsonstring)
print(mydict["phoneNumbers"])

#%%

#Use json.dumps() to turn a Python data structure into a JSON object
#sort_keys will sort the keys in ascending order
#indent will add indentation to "pretty print" your JSON
print(json.dumps(mydict, sort_keys=True, indent=4))

#%%

#Let's get some JSON from the web!
#Reddit is a popular content aggregation website.  Reddit is designed to be very friendly
#to web-scraping.  Simply append "/.json" to the end of any Reddit URL, and you will
#retrieve the JSON used to populate the page.

import requests

response = requests.get("https://www.reddit.com/r/aww/.json")
text = response.text
print(text)

#%%

reddit_data = json.loads(text)

print(json.dumps(reddit_data, sort_keys=True, indent=4))

#%%

#Let's say we want to get the title of each post, and the user who posted it
#along with the time it was posted, the post's score, and the permalink to the post
post_list = []

for post in reddit_data["data"]["children"]:
    author = post.get("data").get("author")
    permalink = post.get("data").get("permalink")
    score = post.get("data").get("score")
    timestamp = post.get('data').get("created_utc")
    title = post.get("data").get("title")
    info = {"auth":author,"link":permalink,"score":score,"title":title,"time":timestamp}
    post_list.append(info)

print(post_list)

#%%

import pandas as pd
import sqlalchemy

engine = sqlalchemy.create_engine('mysql+mysqlconnector://root@localhost/test')

reddit_df = pd.DataFrame(post_list)

reddit_df.to_sql("redditinfo",engine)

#%%
#Getting data back using raw SQL query:

#The with statement creates a variable (in this case, a connection to your SQL server)
#for only the duration of its block, after which the variable is forgotten 
#(in this case, the connection to your SQL server is dropped)
with engine.connect() as con:

    rs = con.execute('SELECT auth, score FROM redditinfo WHERE score > 100')

    for row in rs:
        print(row)