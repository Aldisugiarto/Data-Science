# import tweepy as tw
#
# consumer_key = "2jmajJHnOxcx4K8saR3b8sibA"
# consumer_secret = "eWRBrcS41ZhOngnJUYtsMCwQi3hUUIY2Q8cgrBZw5Z490V5Nw0"
# access_token = "2677235168-CKKsBzsI9tJw5R3qp00ztAsEAzEzUJWS7xAee1W"
# access_token_secret = "EoopoBbTOiWY9TldEDLEdPWG2UZKP37jJjDxY5ziIOxLo"
#
# auth = tw.OAuthHandler(consumer_key,consumer_secret)
# auth.set_access_token(access_token,access_token_secret)
# api = tw.API(auth)
#
# nama = "kompascom"
# jumlahTweet = 10
#
# tweets = api.user_timeline(id=nama,count=jumlahTweet)
#
# for tweet in tweets:
#     print(tweet.user.screen_name)
#     print(tweet.text)
import tweepy as tw
import re
import pandas as pd

consumer_key = "2jmajJHnOxcx4K8saR3b8sibA"
consumer_secret = "eWRBrcS41ZhOngnJUYtsMCwQi3hUUIY2Q8cgrBZw5Z490V5Nw0"
access_token = "2677235168-CKKsBzsI9tJw5R3qp00ztAsEAzEzUJWS7xAee1W"
access_token_secret = "EoopoBbTOiWY9TldEDLEdPWG2UZKP37jJjDxY5ziIOxLo"

auth = tw.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api = tw.API(auth,wait_on_rate_limit=True)

search_words = "jouska"
date_since = "2020-07-25"


def preprocessing(words,date,count):
    new_search = words + " -filter:retweets"
    tweets = tw.Cursor(api.search,
            q=new_search,
            lang="id",
            since=date).items(count)
    items = []
    stopword = ['yang', 'akan', 'di', 'dan', ]
    new_tweets = []
    for tweet in tweets:
        new_word = ''
        for word in tweet.text.lower().split():
            if (word not in stopword):
                new_word = new_word + ' ' + word
        new_tweets.append(new_word)
    for tweet in new_tweets:
        item = []
        item.append (' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split()))
        items.append(item)
    return items

n_tweet = 10
items_jouska = preprocessing(search_words,date_since,n_tweet)
hasil_jouska = pd.DataFrame(data=items_jouska, columns=['tweet'])
print(hasil_jouska)