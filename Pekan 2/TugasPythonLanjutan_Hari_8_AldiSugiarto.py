import tweepy as tw
import re
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

consumer_key = "2jmajJHnOxcx4K8saR3b8sibA"
consumer_secret = "eWRBrcS41ZhOngnJUYtsMCwQi3hUUIY2Q8cgrBZw5Z490V5Nw0"
access_token = "2677235168-CKKsBzsI9tJw5R3qp00ztAsEAzEzUJWS7xAee1W"
access_token_secret = "EoopoBbTOiWY9TldEDLEdPWG2UZKP37jJjDxY5ziIOxLo"

auth = tw.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api = tw.API(auth,wait_on_rate_limit=True)

search_words_1 = "jouska"
search_words_2 = "anies baswedan"
search_words_3 = "terawan agus putranto"
date_since_1 = "2020-07-27"
date_since_2 = "2020-07-27"
date_since_3 = "2020-07-27"

def Search(words,date,count):
    new_search = words + " -filter:retweets"
    tweets = tw.Cursor(api.search,
            q=new_search,
            lang="id",
            since=date).items(count)
    items = []
    for tweet in tweets:
        item = []
        item.append (' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet.text).split()))
        items.append(item)
    return items
def std_senti(items_):
    pos_list = open("./kata_positif.txt", "r")
    pos_kata = pos_list.readlines()
    neg_list = open("./kata_negatif.txt", "r")
    neg_kata = neg_list.readlines()
    S = []
    for item in items_:
        count_p = 0
        count_n = 0
        for kata_pos in pos_kata:
            if kata_pos.strip() in item[0]:
                count_p += 1
        for kata_neg in neg_kata:
            if kata_neg.strip() in item[0]:
                count_n += 1
        S.append(count_p - count_n)
    return S
def PlotData(hasil1,hasil2 = {'value':[1,2,3,4,5,6]},hasil3={'value':[1,2,3,4,5,6]}):
    fig ,ax = plt.subplots(nrows=1,ncols=3,figsize=(15,7))
    labels1, counts1 = np.unique(hasil1["value"], return_counts=True)
    ax[0].bar(labels1, counts1, align='center')
    plt.gca().set_xticks(labels1)

    labels2, counts2 = np.unique(hasil2["value"], return_counts=True)
    ax[1].bar(labels2, counts2, align='center')
    plt.gca().set_xticks(labels2)

    labels3, counts3 = np.unique(hasil3["value"], return_counts=True)
    ax[2].bar(labels3, counts3, align='center')
    plt.gca().set_xticks(labels3)
    return plt.show()

n_tweet = 1000
items_jouska = Search(search_words_1,date_since_1,n_tweet)
hasil_jouska = pd.DataFrame(data=items_jouska, columns=['tweet'])
val_s = std_senti(items_jouska)
# print(val_s)
hasil_jouska["value"] = val_s
print("---------------------------------------Penipuan Jouska---------------------------------------")
print(hasil_jouska)
print("Nilai rata-rata: " + str(np.mean(hasil_jouska["value"])))
print("Nilai median: " + str(np.median(hasil_jouska["value"])))
print("Standar deviasi: " + str(np.std(hasil_jouska["value"])))

items_gub = Search(search_words_2,date_since_2,n_tweet)
hasil_gub = pd.DataFrame(data=items_gub, columns=['tweet'])
val_gub = std_senti(items_gub)
# print(val_s)
hasil_gub["value"] = val_gub
print("---------------------------------------Anies Baswedan---------------------------------------")
print(hasil_gub)
print("Nilai rata-rata: " + str(np.mean(hasil_gub["value"])))
print("Nilai median: " + str(np.median(hasil_gub["value"])))
print("Standar deviasi: " + str(np.std(hasil_gub["value"])))

items_kes = Search(search_words_3,date_since_3,n_tweet)
hasil_kes = pd.DataFrame(data=items_kes, columns=['tweet'])
val_kes = std_senti(items_kes)
# print(val_s)
hasil_kes["value"] = val_kes
print("---------------------------------------Terawan Agus Putranto---------------------------------------")
print(hasil_kes)
print("Nilai rata-rata: " + str(np.mean(hasil_kes["value"])))
print("Nilai median: " + str(np.median(hasil_kes["value"])))
print("Standar deviasi: " + str(np.std(hasil_kes["value"])))

PlotData(hasil1=hasil_jouska,hasil2=hasil_gub,hasil3=hasil_kes)

print("---------------------------------------Kesimpulan---------------------------------------")
print("1. Analisis data ini berguna untuk mengetahui sentimen topiK yang diinginkan")
print("2. Kata kunci yang tepat akan berpengaruh terhadap hasil")