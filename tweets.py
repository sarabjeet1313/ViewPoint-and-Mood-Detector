from pymongo import MongoClient
import re
import os

def clean(uncleanText):
    cleanTweet = re.sub(r'http\S+', '', uncleanText)
    cleanTweet = ''.join([char if ord(char) < 128 else '' for char in cleanTweet])
    cleanTweet = re.sub('[_()\"*#/@<>{}`+=~|]', "", str(cleanTweet))
    cleanTweet = ' '.join([word for word in uncleanText.split(" ") if word != "&amp"])
    cleanTweet = ' '.join([word for word in uncleanText.split(" ") if word != "RT"])
    cleanTweet = re.sub(r'([^\s\w]|_)+', '', cleanTweet)
    cleanTweet = cleanTweet.replace("\n" , " ")
    cleanTweet = cleanTweet.lower()

    # print("Data cleaned for the given line")
    return cleanTweet

# ------------------------------  Extracting tweets from Mongo --------------------------------- #

client = MongoClient()
db = client.Assignment3Database
search = db.twitterSearchCollection
stream = db.twitterStreamCollection


if not os.path.exists("tweets"):
    os.mkdir("tweets")

counter = 1
for tweet in search.find():

    f = open("tweets/file_" + str(counter) + ".txt", 'a')
    text = clean(tweet["text"])
    f.write(text)
    counter += 1
    f.close()

for tweet in stream.find():

    f = open("tweets/file_" + str(counter) + ".txt", 'a')
    text = clean(tweet["text"])
    f.write(text)
    counter += 1
    f.close()

# ------------------------------------------------------------------------------------------------ #