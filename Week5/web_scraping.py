"""WEB SCRAPING"""
from bs4 import BeautifulSoup
import requests
from urllib.parse import quote_plus
import time
import re

jobs_to_search = ["Data Scientist", "Analytics"] #Add more jobs to look for here
cities_to_search = ["Seattle, WA", "San Francisco, CA"] #Add more cities to search in here
distance = 50 #Radius in miles from city
posted = 30 #Number of days back to search

mapper = {"baseURL":"http://www.careerbuilder.com","job":"/jobs?keywords=", "loc":"&location=", "dist":"&radius=", "posted":"&posted="} #Can add more job sites here
                
queries = [mapper["baseURL"] + mapper["job"] + quote_plus(job) + mapper["loc"] + quote_plus(loc) + mapper["dist"] + str(distance) + mapper["posted"] + str(posted) for job in jobs_to_search for loc in cities_to_search]

#We'll use a set so we don't pull back the same job multiple times
job_links = set()
results = []

#Query for each combination of job and city
for query in queries:
  page_no = 1
  done = False
  while not done:
    print("Retrieving page {} of query {}...".format(page_no, query))
    #Send the request
    request = requests.get(query + "&page_number=" + str(page_no))
    #Pull out the response text
    text = request.text
    
    #Pass the response text to BeautifulSoup, parse using lxml parser
    soup = BeautifulSoup(text, "lxml")
    
    #Find all the elements that have a class of "jrp-job-list|job-title-click" and pull out the data-job-did (job id)
    jobsoup = soup.find_all(attrs = {"data-gtm" : re.compile(r"jrp-job-list\|job-title-click")})
    id_list = list(map(lambda x: mapper["baseURL"] + "/job/" + x["data-job-did"], jobsoup))
        
    job_links.update(id_list)
    
    #Find out how many pages there are total
    page = soup.find(class_ = "page-count").getText().strip().split()   
    final_page = int(page[-1])

    #If we reached the final page, we're done
    if page_no >= final_page:
      done = True
    #Otherwise, go to the next page and send another request
    else:
      page_no += 1
    
    #Here we will time-out for a second to avoid being blocked by the server
    time.sleep(1)

#%%
#Now that we have our list of job links, we can pull down the information for each job:
from nltk.corpus import stopwords
stop = set(stopwords.words("english"))

num = 0
results = []

for job_link in job_links:
  print("Downloading... {}% done".format(round(num/len(job_links)*100,2)))
  
  request = requests.get(job_link)
  text = request.text
  soup = BeautifulSoup(text, "lxml")
  soup = soup.find(class_ = "card")
  
  #There is no unique identifier on the title, but it is the first <h1> element, so we can just use find("h1")
  title = soup.find("h1").getText().strip()
  
  #The company and location are jammed together in this <h2>
  company_loc = soup.find("h2").getText().split("•")
  company = company_loc[0].strip()
  
  #Sometimes location is not given
  try:
    location = company_loc[1].strip()
  except:
    location = "N/A"
  
  posted = soup.find("h3").getText().strip()
  
  #Now let's get the job description
  description_text = soup.find(class_ = "small-12 columns item").getText()

  #Everything that isn't a letter or number is turned into a blank space, and convert the result to lower case
  description_text = re.sub(r"[^A-z|0-9]+", " ", description_text).lower()
  
  #split on blank spaces
  tokens = description_text.split()
  #Only allow words which are not stopwords
  tokens = [token for token in tokens if token not in stop]
  #Rejoin the words into a single string
  tokens = " ".join(tokens[2:])
  
  results.append({"title":title, "company":company, "location":location,"posted":posted,"description":tokens})  
  
  num += 1
  time.sleep(1)
  
#%%
#Now let's do some analysis!
import pandas as pd
mydf = pd.DataFrame(results)
mydf.to_csv("results.csv")
