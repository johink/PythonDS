#This code borrowed from Adil Moujahid (http://adilmoujahid.com/posts/2014/07/twitter-analytics/)

#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "access token goes here"
access_token_secret = "access token secret goes here"
consumer_key = "consumer key goes here"
consumer_secret = "consumer secret goes here"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)
        if status == 420:
            return False


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #Edit the value of track to change what you're looking for in the tweets
    stream.filter(track=['trump'])
