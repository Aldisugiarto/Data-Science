# Author    : Aldi Sugiarto
# Tanggal   : 23 Juli 2020
# Versi     : 1.0

#---------------------------------------------------Tugas Python Scraping ---------------------------------------------------#
#Import library untuk request open url dan beautifulsoup
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import csv

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
#Simpan data dalam file csv
csv_pok = open("data_pokemon.csv","w+",newline='')
writer = csv.writer(csv_pok,delimiter=',')
for inp in List:
    writer.writerow(inp)
print(List)