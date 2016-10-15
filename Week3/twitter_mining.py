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
import pandas as pd
pd.to_datetime(all_data[0]["created_at"])

summary = []
for tweet in all_data:
    mydict = {}
    mydict["time"] = pd.to_datetime(tweet["created_at"])
    mydict["text"] = tweet["text"]
    mydict["hashtags"] = [x["text"] for x in tweet["entities"]["hashtags"]]
    mydict["loc"] = tweet["geo"] if tweet["geo"] is not None else tweet["user"]["location"]
    summary.append(mydict)

mydf = pd.DataFrame(summary)

#%%
import json
#Let's dig into a more meaty dataset:  All tweets containing "#debate" during the second presidential debate
all_data = []
#Read in the file
with open("c:/users/john/desktop/python course/tweets.txt") as file:
    for line in file:
        #Only read in the lines that are not blank
        if not line.isspace():
            all_data.append(json.loads(line))
            
print(all_data[0])

#%%
#Now we have a list containing all of the tweets; let's do some analysis!
#What are the most common hashtags?
#First, let's implement this ourselves:
list_of_hashtags = []
for tweet in all_data:
    list_of_hashtags.extend(tweet["hashtags"])
    
#%%    
#Here we will make a list of tuples, with the first item being the hashtag, and the second item being the number of times that hashtag is in the list
counts = [(hashtag,list_of_hashtags.count(hashtag)) for hashtag in set(list_of_hashtags) ]

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
    #Turn the tweet into a list of lower case individual words
    tweet = html.unescape(tweet)
    tweet = tweet.lower().split()
    #Get rid of the words which are hyperlinks, and replace everything that isn't a letter, # or @ with a blank
    tweet = [re.sub(r"[^A-z|0-9|#|@|:|/]+","", word) for word in tweet if not word.startswith("http")]
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
processed_tweets = []
for tweet in all_data:
    processed_tweets.append(clean_tweet(tweet["text"], stop))
    
#%%
#Now we can use scikit-learn's CountVectorizer to create models!
from sklearn.feature_extraction.text import CountVectorizer

#Here we create an instance of a CountVectorizer called "vectorizer"
vectorizer = CountVectorizer(analyzer = "word", max_features = 5000)

#Now we will create a Bag of Words!
#The 5,000 most common words are given their own column, and each row represents a tweet
#Whatever words were present in the tweet will be represented by a "1"
train = vectorizer.fit_transform(processed_tweets)

#Here we are converting the fit_transform output to a numpy array
#numpy arrays are very efficient
train = train.toarray()

#If you want to see the words which correspond to the columns, use get_feature_names()
vectorizer.get_feature_names()

tweet = all_data[12]["text"]