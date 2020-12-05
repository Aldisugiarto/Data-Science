# Author    :Aldi Sugiarto
# Tanggal   : 21 Juli 2020
# Versi     : 1.0

#---------------------------------------------------Tugas Python---------------------------------------------------#
#Import library untuk request open url dan beautifulsoup
from urllib.request import urlopen
from bs4 import BeautifulSoup

#Akses html menggunakan beautifulsoup
alamat = "https://blog.sanbercode.com/"
html = urlopen(alamat)
data = BeautifulSoup(html, 'html.parser')

#Mencari tag dan class
items_judul = data.findAll("a", {"class": "text-dark"})[1:4]
items_penulis = data.findAll("a", {"class": "text-muted text-capitalize"})[1:4]

#Masukan teks pada list menggunakan list comprehension
list_judul = [i.get_text().strip() for i in items_judul]
list_penulis = [i.get_text().strip() for i in items_penulis]

#Print List judul dan penulis
print('Judul:',list_judul)
print('Penulis:',list_penulis)