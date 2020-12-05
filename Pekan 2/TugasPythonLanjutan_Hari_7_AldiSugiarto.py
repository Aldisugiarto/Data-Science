import tweepy as tw

consumer_key = *Your consumer key*
consumer_secret = *Your consumer secret*
access_token = *Your token*
access_token_secret = *your token secret*

auth = tw.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api = tw.API(auth)

nama = "jokowi"
jumlahTweet = 200

tweets = api.user_timeline(id=nama,count=jumlahTweet)
i=0
keyword = ['covid-19','pandemi','covid','kesehatan',]
covid = []
for tweet in tweets:
    for cov in keyword:
        word = tweet.text.lower()
        if(cov in word):
            i += 1
            covid.append(word)
            # print(word)
list_cov =set(covid)
print('banyaknya tweet pak jokowi yang diambil: ',jumlahTweet)
print('banyaknya pak jokowi membicarakan Covid dalam tweetnya: ',len(list_cov))
