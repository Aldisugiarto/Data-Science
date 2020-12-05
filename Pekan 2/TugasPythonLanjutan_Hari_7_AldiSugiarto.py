import tweepy as tw

consumer_key = "2jmajJHnOxcx4K8saR3b8sibA"
consumer_secret = "eWRBrcS41ZhOngnJUYtsMCwQi3hUUIY2Q8cgrBZw5Z490V5Nw0"
access_token = "2677235168-CKKsBzsI9tJw5R3qp00ztAsEAzEzUJWS7xAee1W"
access_token_secret = "EoopoBbTOiWY9TldEDLEdPWG2UZKP37jJjDxY5ziIOxLo"

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
