"""TWITTER TEXT MINING"""
import json
all_data = []
#Read in the file
with open("twitdata.txt") as file:
    for line in file:
        #Only read in the lines that are not blank
        if not line.isspace():
            all_data.append(json.loads(line))
        
#%%
#Let's look at the structure of a tweet:
print(json.dumps(all_data[0],sort_keys=True,indent=2))

"""RESULTS:
{
  "contributors": null,
  "coordinates": null,
  "created_at": "Sun Oct 02 15:52:10 +0000 2016",
  "entities": {
    "hashtags": [
      {
        "indices": [
          29,
          38
        ],
        "text": "INDvsJAX"
      }
    ],
    "symbols": [],
    "urls": [],
    "user_mentions": []
  },
  "favorite_count": 0,
  "favorited": false,
  "filter_level": "low",
  "geo": null,
  "id": 782609128082448384,
  "id_str": "782609128082448384",
  "in_reply_to_screen_name": null,
  "in_reply_to_status_id": null,
  "in_reply_to_status_id_str": null,
  "in_reply_to_user_id": null,
  "in_reply_to_user_id_str": null,
  "is_quote_status": false,
  "lang": "en",
  "place": null,
  "retweet_count": 0,
  "retweeted": false,
  "source": "<a href=\"http://twitter.com/download/android\" rel=\"nofollow\">Twitter for Android</a>",
  "text": "Is Andrew Luck in the game?  #INDvsJAX",
  "timestamp_ms": "1475423530966",
  "truncated": false,
  "user": {
    "contributors_enabled": false,
    "created_at": "Mon Feb 28 04:21:49 +0000 2011",
    "default_profile": false,
    "default_profile_image": false,
    "description": "Rocking to the beat of my drum set.",
    "favourites_count": 157,
    "follow_request_sent": null,
    "followers_count": 101,
    "following": null,
    "friends_count": 195,
    "geo_enabled": true,
    "id": 258640821,
    "id_str": "258640821",
    "is_translator": false,
    "lang": "en",
    "listed_count": 3,
    "location": "Houston, Tx",
    "name": "Edgar Castillo",
    "notifications": null,
    "profile_background_color": "131516",
    "profile_background_image_url": "http://abs.twimg.com/images/themes/theme14/bg.gif",
    "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme14/bg.gif",
    "profile_background_tile": true,
    "profile_banner_url": "https://pbs.twimg.com/profile_banners/258640821/1473977133",
    "profile_image_url": "http://pbs.twimg.com/profile_images/666518290441703424/H2Z_vVev_normal.jpg",
    "profile_image_url_https": "https://pbs.twimg.com/profile_images/666518290441703424/H2Z_vVev_normal.jpg",
    "profile_link_color": "009999",
    "profile_sidebar_border_color": "EEEEEE",
    "profile_sidebar_fill_color": "EFEFEF",
    "profile_text_color": "333333",
    "profile_use_background_image": true,
    "protected": false,
    "screen_name": "ecashtillo",
    "statuses_count": 2080,
    "time_zone": "Central Time (US & Canada)",
    "url": null,
    "utc_offset": -18000,
    "verified": false
  }
}
"""

#%%

import json
#Let's dig into a more meaty dataset:  All tweets containing "#debate" during the second presidential debate
all_data = []
#Read in the file: https://drive.google.com/open?id=0B651fVCo040CNWM5MTdhWW5FMXc
with open("c:/users/john/desktop/python course/tweets.txt") as file:
    for line in file:
        #Only read in the lines that are not blank
        if not line.isspace():
            all_data.append(json.loads(line))
            
print(all_data[0])

#%%
import numpy as np

geotweets = list(filter(lambda x: x["loc"], all_data))
sample = np.random.choice(len(geotweets), 1000, replace=False)

sampletweets = [geotweets[i] for i in sample]

#%%    
def get_class(tweet):
    while True:
        print("\n\n\n")
        print(tweet["text"])
        print("1: Pro-Hillary; 2: Pro-Trump; 3: Other")
        answer = input("> ")
        if answer == "1":
            return "Pro-Hillary"
        elif answer == "2":
            return "Pro-Trump"
        elif answer == "3":
            return "Other"
            
for tweet in sampletweets:
    tweet["class"] = get_class(tweet)
    
#%%
import json

classtweets = json.dumps(sampletweets)

#%%
with open("classtweets.txt", "w") as outfile:
    outfile.write(classtweets)

#%%
#Now we have a list containing all of the tweets; let's do some analysis!
#What are the most common hashtags?
#First, let's implement this ourselves:
list_of_hashtags = []
for tweet in all_data:
    list_of_hashtags.extend(tweet["hashtags"])
    
#%%    
#Here we will make a list of tuples, with the first item being the hashtag, and the second item being the number of times that hashtag is in the list
counts = [(hashtag,list_of_hashtags.count(hashtag)) for hashtag in set(list_of_hashtags)]

#%%

#Uh oh!  That was wayyyyy too slow.  Luckily, Python has many libraries with efficient implementations for common use cases
#The Counter function does exactly what we need:
from collections import Counter
counts = Counter(list_of_hashtags)
counts.most_common(15)

#%%
#Here we can see a minor issue:  It's treating #debate and #Debate as different hashtags
#Let's redo the analysis with all the hashtags converted to lower-case
list_of_hashtags = [x.lower() for x in list_of_hashtags]
counts = Counter(list_of_hashtags)
counts.most_common(15)

#%%
#Let's start analyzing the tweets themselves.  The tweets have a bunch of unnecessary junk in them,
#so let's write a function which will clean up a tweet
#This function will need to use regular expressions to get rid of unnecessary characters
#as well as the Natural Language Tool-Kit (NLTK) to get rid of stop words
#Use nltk.download() to open the download manager, go to Corpora -> stopwords and download
import nltk
nltk.download()

#%%
import re
from nltk.corpus import stopwords
import html

def clean_tweet(tweet, trash):  
    #Turn things like &gt; to >
    tweet = html.unescape(tweet)
    #Turn the tweet into a list of lower case individual words
    tweet = tweet.lower().split()
    #Get rid of the words which are hyperlinks, and replace everything that isn't a letter, # or @ with a blank
    tweet = [re.sub(r"[^A-z|0-9|#|@]+","", word) for word in tweet if not word.startswith("http")]
    #Remove all the trash words
    tweet = [word for word in tweet if word not in trash and len(word) > 2]
    #Put all the words back together with a blank in between them
    return " ".join(tweet)

#%%
#Make a list of words to remove  
stop = set(stopwords.words("english"))

print("Before: {}\n\n".format(all_data[12]["text"]))
print("After: {}".format(clean_tweet(all_data[12]["text"], stop)))

#%%
#Now we'll convert all the texts
import json
import pandas as pd

with open("classtweets.txt") as infile:
    classtweets = infile.read()
    
classtweets = json.loads(classtweets)
for tweet in classtweets:
    tweet["text_clean"] = clean_tweet(tweet["text"], stop)

classtweets = pd.DataFrame(classtweets)
traintweets = classtweets.sample(frac = .8, random_state = 88)
testtweets = classtweets.drop(traintweets.index)
    
#%%
#Now we can use scikit-learn's CountVectorizer to create models!
from sklearn.feature_extraction.text import CountVectorizer

#Here we create an instance of a CountVectorizer called "vectorizer"
vectorizer = CountVectorizer(analyzer = "word", max_features = 5000)

#Now we will create a Bag of Words!
#The 5,000 most common words are given their own column, and each row represents a tweet
#Whatever words were present in the tweet will be represented by a "1"
train = vectorizer.fit_transform(traintweets["text_clean"])

#If you want to see the words which correspond to the columns, use get_feature_names()
vectorizer.get_feature_names()

#%%
#Let's train a naive Bayes model
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
import numpy as np

#Here we instantiate a MultinomialNB object, and call its .fit() method, which creates a classifier
classifier = MultinomialNB().fit(train, traintweets["class"])

#Now we have to transform our test data using our vectorizer, but be careful not to re-fit
#i.e. we will only do .transform() and not .fit_transform()
test = vectorizer.transform(testtweets["text_clean"])

#Now to predict the class labels
predictions = classifier.predict(test)

print("Accuracy = {}".format(np.mean(predictions == testtweets["class"])))

print(metrics.confusion_matrix(testtweets["class"], predictions))

print(metrics.classification_report(testtweets["class"], predictions))
    
#%%
#Here's a support vector machine model...
from sklearn.linear_model import SGDClassifier
SVMclassifier = SGDClassifier(loss='hinge', penalty='l2', alpha=1e-3, n_iter=5, random_state=42)
SVMclassifier.fit(train, traintweets["class"])
SVMpredictions = SVMclassifier.predict(test)

print("Accuracy = {}".format(np.mean(SVMpredictions == testtweets["class"])))

print(metrics.confusion_matrix(testtweets["class"], SVMpredictions))

print(metrics.classification_report(testtweets["class"], SVMpredictions))



#%%
#Let's plot where the tweets are coming from:
import pandas as pd
geotweets = list(filter(lambda x: x["loc"], all_data))

def trans_tweet(tweet):
    result = {}
    result["long"] = tweet["loc"]["coordinates"][0] if tweet["loc"].get("bounding_box") is None else tweet["loc"]["bounding_box"]["coordinates"][0][0][0]
    result["lat"] = tweet["loc"]["coordinates"][1] if tweet["loc"].get("bounding_box") is None else tweet["loc"]["bounding_box"]["coordinates"][0][0][1]
    result["text"] = clean_tweet(tweet["text"], stop)
    result["time"] = tweet["time"]
    result["class"] = tweet.get("class")
    return result
    
mydf = pd.DataFrame(list(map(trans_tweet, geotweets)))

mydf["time"] = pd.to_datetime(mydf["time"])

predictions = classifier.predict(vectorizer.transform(mydf["text"]))

mydf["class"] = predictions

demtweets = mydf[mydf["class"] == "Pro-Hillary"]
reptweets = mydf[mydf["class"] == "Pro-Trump"]

demtweets = demtweets.groupby(["lat","long"]).count().reset_index()
reptweets = reptweets.groupby(["lat","long"]).count().reset_index()

from math import sqrt
demtweets["scale"] = list(map(sqrt,demtweets["class"]*4))
reptweets["scale"] = list(map(sqrt,reptweets["class"]*4))


#%%

import plotly
import plotly.plotly as py


plotly.tools.set_credentials_file(username='xyz', api_key='abc')

data = [ dict(
        type = 'scattergeo',
        name = "Pro-Hillary / Anti-Trump",
        locationmode = 'USA-states',
        lon = demtweets['long'],
        lat = demtweets['lat'],
        mode = 'markers',
        marker = dict( 
            size = demtweets["scale"], 
            sizemin = 3,
            opacity = 0.4,
            symbol = 'circle',
            color = "rgb(50, 50, 255)",
        )),
        dict(
        type = 'scattergeo',
        name = "Pro-Trump / Anti-Hillary",
        locationmode = 'USA-states',
        lon = reptweets['long'],
        lat = reptweets['lat'],
        mode = 'markers',
        marker = dict( 
            size = reptweets["scale"], 
            sizemin = 3,
            opacity = 0.4,
            symbol = 'circle',
            color = "rgb(255, 50, 50)",
        ))]

layout = dict(
        title = 'Tweets during the second Presidential debate',
        geo = dict(
            scope='usa',
            projection=dict( type='albers usa' ),
            showland = True,
            landcolor = "rgb(250, 250, 250)",
            subunitcolor = "rgb(217, 217, 217)",
            countrycolor = "rgb(217, 217, 217)",
            countrywidth = 0.5,
            subunitwidth = 0.5        
        ),
    )


fig = dict( data=data, layout=layout )

#This plots into your plotly account
plot_url = py.plot(fig, filename='tweets')


""" If you'd rather create a picture:
py.image.save_as(fig, filename='a-simple-plot.png')

from PIL import Image
img = Image.open("a-simple-plot.png")
img.show()
"""