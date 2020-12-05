import tweepy as tw
import re
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

consumer_key = *Your consumer key*
consumer_secret = *Your consumer secret*
access_token = *Your token*
access_token_secret = *Your token secret*

auth = tw.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api = tw.API(auth,wait_on_rate_limit=True)

search_words = "jouska"
date_since = "2020-07-25"


def Search(words,date,count):
    new_search = words + " -filter:retweets"
    tweets = tw.Cursor(api.search,
            q=new_search,
            lang="id",
            since=date).items(count)
    items = []
    for tweet in tweets:
        item = []
        item.append(tweet.id)
        item.append(tweet.user.screen_name)
        item.append(tweet.user.location)
        item.append (' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet.text).split()))
        items.append(item)
    return items

n_tweet = 50
items_jouska = Search(search_words,date_since,n_tweet)
print(items_jouska)
# hasil_jouska = pd.DataFrame(data=items_jouska, columns=['User','Lokasi','Tweet'])
# print(hasil_jouska)
# j_data = hasil_jouska.to_json(orient='split')
# print(j_data)
