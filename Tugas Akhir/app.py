# Author    : Aldi Sugiarto
# Tanggal   : 13 Agustus 2020
# Versi     : 1.0
# Email     : aldisugiarto5@gmail.com
#---------------------------------------------------Tugas Akhir Python Lanjutan---------------------------------------------------#

#Import library yang dibutuhkan
import tweepy as tw
import re
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime
import sqlite3

#Inisialisasi variabel global
keyword = "vaksin covid"

#Otentikasi twitter api
consumer_key = *Your consumer key*
consumer_secret = *Your consumer secret*
access_token = *Your token*
access_token_secret = *your token secret*

auth = tw.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api = tw.API(auth,wait_on_rate_limit=True)

#Class twitter
class twitter():
    def Search(self,words,date):
        new_search = words + " -filter:retweets"
        tweets = tw.Cursor(api.search,
                q=new_search,
                lang="id",
                since=date,
                tweet_mode='extended').items(100)
        items = []
        for tweet in tweets:
            item = []
            item.append(tweet.created_at.strftime('%Y-%m-%d'))
            item.append(tweet.user.screen_name)
            item.append (' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet.full_text).split()).lower())
            item.append(0)
            items.append(item)
        return items

#Class database sqlite
class database():
    def open_db(self,name):
        conn = sqlite3.connect(name)
        cursor = conn.cursor()
        return cursor,conn
    def create_table_1(self):
        table = '''CREATE TABLE IF NOT EXISTS data_twitter (
                    id_tweet INTEGER PRIMARY KEY AUTOINCREMENT,
                    date TEXT,
                    user TEXT,
                    tweet TEXT,
                    state INTEGER);'''
        c,conn = self.open_db('data_tweet.db')
        c.execute(table)
        self.close_db(conn,c)
        return print("Table 1 has been created")
    def create_table_2(self):
        table = '''CREATE TABLE IF NOT EXISTS data_sentiment (
                    id_senti INTEGER PRIMARY KEY AUTOINCREMENT,
                    date TEXT,
                    user TEXT,
                    tweet TEXT,
                    sentiment TEXT);'''
        c,conn = self.open_db('data_tweet.db')
        c.execute(table)
        self.close_db(conn,c)
        return print("Table 2 has been created")
    def insert(self,q,data):
        c, conn = self.open_db('data_tweet.db')
        c.executemany(q, data)
        conn.commit()
        self.close_db(conn, c)
        return print("Data has been entered to database")
    def update(self,q):
        c, conn = self.open_db('data_tweet.db')
        c.execute(q)
        conn.commit()
        self.close_db(conn, c)
        return print("Data has been update to database")
    def show(self,q,f):
        c, conn = self.open_db('data_tweet.db')
        c.execute(q)
        if f.isnumeric():
            n = int(f)
            disp = c.fetchmany(n)
        else:
            disp = c.fetchall()
        self.close_db(conn, c)
        return print(disp)
    def select(self,q):
        c,conn = self.open_db('data_tweet.db')
        c.execute(q)
        val = c.fetchall()
        self.close_db(conn,c)
        return val
    def lihat(self,q,tanggal):
        c,conn = self.open_db('data_tweet.db')
        c.execute(q,tanggal)
        val = c.fetchall()
        self.close_db(conn,c)
        return val
    def close_db(self,conn,cur):
        cur.close()
        conn.close()
#Membuat fungsi setiap menu
#1. Update data
def UpdateData(keyword):
    t = twitter()
    since_date = (datetime.datetime.today() - datetime.timedelta(days=2)).strftime('%Y-%m-%d')
    print(since_date)
    tweet = t.Search(keyword,since_date)
    # print(tweet)
    insert = '''INSERT INTO data_twitter
            ('date','user','tweet','state')
            VALUES(?,?,?,?)'''
    db = database()
    db.insert(insert,tweet)
    disp = '''SELECT * FROM data_twitter'''
    db.show(disp,'10')
#2. Update Nilai Sentiment
def UpdateSentiment():
    pos_list = open("./kata_positif.txt", "r")
    pos_kata = pos_list.readlines()
    neg_list = open("./kata_negatif.txt", "r")
    neg_kata = neg_list.readlines()
    select = '''SELECT tweet FROM data_twitter WHERE state = 0'''
    db = database()
    tweets = db.select(select)
    S = []
    for tweet in tweets:
        count_p = 0
        count_n = 0
        for kata_pos in pos_kata:
            if kata_pos.strip() in tweet[0]:
                count_p += 1
        for kata_neg in neg_kata:
            if kata_neg.strip() in tweet[0]:
                count_n += 1
        S.append(count_p - count_n)
        # print(tweet)
    select = '''SELECT date,user,tweet FROM data_twitter WHERE state = 0'''
    data = db.select(select)
    if len(data) != 0:
        items = []
        for i in range (len(S)):
            raw = list(data[i])
            raw.append(S[i])
            items.append(raw )
        print(items)
        insert = '''INSERT INTO data_sentiment
                ('date','user','tweet','sentiment')
                VALUES(?,?,?,?)'''
        db.insert(insert,items)
        update = '''UPDATE data_twitter 
                    SET state = 1
                    WHERE state = 0'''
        db.update(update)
        disp = 'Data sentiment has been updated'
    else:
        disp = 'No data is changed'
    return print(disp)
#3. Lihat
def Lihat():
    t_awal = input('tanggal awal(format: 2020-08-01)    :')
    t_akhir = input('tanggal akhir(format: 2020-08-01)  :')
    select = '''SELECT user,date,tweet FROM data_twitter WHERE date BETWEEN ? and ?'''
    tanggal = []
    tanggal.append(t_awal)
    tanggal.append(t_akhir)
    db = database()
    disp = db.lihat(select,tanggal)
    if len(disp) != 0:
        df = pd.DataFrame(disp,columns = ['User','Tanggal tweet','Tweet'])
        print(df)
    else:
        print('Tidak ada data pada tanggal tersebut')
#4. Visualisasi
def Visualisasi():
    t_awal = input('tanggal awal(format: 2020-08-01)    :')
    t_akhir = input('tanggal akhir(format: 2020-08-01)  :')
    # t_awal = '2020-08-01'
    # t_akhir = '2020-09-01'
    select = '''SELECT sentiment FROM data_sentiment WHERE date BETWEEN ? and ?'''
    tanggal = []
    tanggal.append(t_awal)
    tanggal.append(t_akhir)
    db = database()
    data = db.lihat(select, tanggal)
    val = [int(item) for i in data for item in i]
    print('Nilai rata-rata:' + str(np.mean(val)))
    print('Nilai Median:' + str(np.median(val)))
    print('Standar deviasi:'+ str(np.std(val)))
    labels, counts = np.unique(val, return_counts=True)
    plt.bar(labels, counts, align='center')
    plt.gca().set_xticks(labels)
    return plt.show()

#Create table
db = database()
db.create_table_1()
db.create_table_2()

#Variable global
option = '0'
keluar = True
while(keluar):

    if option == '0':
        # Apps features
        print("Apa yang ingin anda lakukan?")
        print("\t1. Update Data")
        print("\t2. Update Nilai Sentiment")
        print("\t3. Lihat")
        print("\t4. Visualisasi")
        print("\t5. Keluar")

        option = input("Input Anda :\n")
    elif option == '1':
        UpdateData(keyword)
        option = '0'
    elif option == '2':
        UpdateSentiment()
        option = '0'
    elif option == '3':
        Lihat()
        option = '0'
    elif option == '4':
        Visualisasi()
        option = '0'
    elif option == '5':
        keluar = False
