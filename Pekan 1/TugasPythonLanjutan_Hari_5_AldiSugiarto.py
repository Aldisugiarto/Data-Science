# Author    : Aldi Sugiarto
# Tanggal   : 24 Juli 2020
# Versi     : 1.0

#---------------------------------------------------Tugas Python Scraping---------------------------------------------------#
#Import library untuk request open url dan beautifulsoup
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import csv
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler
import numpy as np

#Akses alamat yang memiliki keamanan khusus
alamat = "https://pokemondb.net/pokedex/all"
safeAdd = Request(alamat, headers={'User-Agent': 'Mozilla/5.0'})
html = urlopen(safeAdd)
data = BeautifulSoup(html, 'html.parser')

#Mendapatkan data table dari data html
table = data.findAll("table",{"class":"data-table block-wide"})[0]
rows = table.findAll("tr")

#Memasukan data e sebuah list
List = []
for row in rows:
    raw = [cell.get_text().strip() for cell in row.findAll(['td','th'])]
    List.append(raw)

#Masukan data dalam sebuah frame
df = pd.DataFrame(List[1:985],columns=List[0])
df_pokemon = df.loc[:,'Attack':'Defense']
print(df_pokemon)

#Mengubah data dalam bentuk array
df_array = np.array(df_pokemon)
df_array = df_array.astype('int64')

#Clustering data menggunakan k means
kmeans = KMeans(n_clusters=3,random_state=100)
kmeans.fit(df_array)
print(kmeans)
df_pokemon['kluster'] = kmeans.labels_
print(df_pokemon)

#Plot hasil clustering
fig, ax = plt.subplots(figsize=(10,5))
ax.scatter(df_array[:,0],df_array[:,1],s=10,c=df_pokemon.kluster,marker='o',alpha=0.5)
plt.xlabel('Att')
plt.ylabel('Def')
plt.title('Hasil Klustering K-Means')
plt.show()

#---------------------------------------------------Kesimpulan---------------------------------------------------#
# 1. Klustering data menggunakan K mean berfungsi untuk mengetahui penyebaran dan pola suatu data.
# 2. Penyebaran data menunjukan pola yang dapat kita ambil suatu informasinya.
# 3. Klustering berfungsi untuk melabeli suatu data.