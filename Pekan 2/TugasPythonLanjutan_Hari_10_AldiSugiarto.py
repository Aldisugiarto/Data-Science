# Author    : Aldi Sugiarto
# Tanggal   : 01 Agustus 2020
# Versi     : 1.0

#---------------------------------------------------Tugas Python Scraping and saving to Ms.Excel---------------------------------------------------#
#Import library untuk request open url dan beautifulsoup, serta openpyxl
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from openpyxl import Workbook

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
# print(List)

#Menyimpan data ke Ms. Excel
wb = Workbook()
ws = wb.active
ws.title = 'Data Pokemon'

for item in List[:17]:
    ws.append(item)
wb.save('TugasPythonLanjutan_Hari_10_AldiSugiarto.xlsx')
print('-'*40,'Data Berhasil Disimpan','-'*40)