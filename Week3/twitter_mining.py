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
