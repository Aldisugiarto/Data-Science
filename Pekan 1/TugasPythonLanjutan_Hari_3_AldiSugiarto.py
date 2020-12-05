# Author    :Aldi Sugiarto
# Tanggal   : 22 Juli 2020
# Versi     : 1.0

#---------------------------------------------------Tugas Python Scraping No.1---------------------------------------------------#
#Import library untuk request open url dan beautifulsoup
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd


# ---------------------------------------------------Membuat fungsi---------------------------------------------------#
def getHTML_wiki(addr):
    alamat = addr
    html = urlopen(alamat)
    data = BeautifulSoup(html, 'html.parser')
    return data

#Akses html menggunakan beautifulsoup
addr_1 = "https://en.wikipedia.org/wiki/List_of_brightest_stars"
tag_1 = "table"
class_1 ="wikitable"
data = getHTML_wiki(addr_1)
table = data.findAll(tag_1, {"class": class_1})[0]
rows = table.findAll("tr")

# Parsing data ke sebuah list
val = []
for row in rows:
    for tag in row.findAll('span'):
            tag.decompose()
    List_1 = [cell.get_text().strip() for cell in row(['td','th'])]
    val.append(List_1)

#Memasukan data ke dalam tabel berupa dataframe
df = pd.DataFrame(val[1:],columns=val[0])
print(df)

#---------------------------------------------------Tugas Python Scraping No.2---------------------------------------------------#
#Mengakses url yang akan diambil datanya
data_film = getHTML_wiki("https://en.wikipedia.org/wiki/List_of_action_films_of_the_2020s")
table_2020 = data_film.findAll("table",{"class":"wikitable"})[0]
rows_2020 = table_2020.findAll("tr")
table_2021 = data_film.findAll("table",{"class":"wikitable"})[1]
rows_2021 =table_2021.findAll("tr")

# Memasukan data HTML ke dalam list
List_2020 = []
List_2021 = []
for row in rows_2020:
    raw_list_2020 = [cell.get_text().strip() for cell in row.findAll(['td','th'])]
    List_2020.append(raw_list_2020)
for row in rows_2021:
    raw_list_2021 = [cell.get_text().strip() for cell in row.findAll(['td','th'])]
    List_2021.append(raw_list_2021)

#Hapus elemen dan print hasilnya
del(List_2020[1])                               #Hapus list elemen ke-1
print(len(List_2020))                           #Print panjang list 2020
del(List_2021[0:2])                             #Hapus list elemen ke-0 s/d 1
print(len(List_2021))                           #Print panjang list 2021
List_film = List_2020 + List_2021               #Menggabungkan list 2020 dan 2021
print('Daftar film(2020 - 2021): ',List_film)   #Print list gabungan tersebut