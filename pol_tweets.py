import json, pandas as pd

num_done = 0

with open("tweets.txt", "w") as outfile:
    for i in range(5):
        filename = r"D:\twitdata" + str(i) + ".txt"
        print("File {} is starting.".format(i))
        with open(filename) as infile:
            for line in infile:
                if not line.isspace():
                    tweet = json.loads(line)
                    try:
                        mydict = {}
                        mydict["time"] = tweet["created_at"]
                        mydict["text"] = tweet["text"]
                        mydict["hashtags"] = [x["text"] for x in tweet["entities"]["hashtags"]]
                        mydict["loc"] = tweet["geo"] if tweet["geo"] is not None else tweet["user"]["location"]
                        outfile.write(json.dumps(mydict) + "\n")
                        num_done += 1
                    except:
                        pass
                    if num_done % 10000 == 0:
                        print("Tweets processed: {}".format(num_done))
        print("File {} is done.".format(i))
        
        #%%