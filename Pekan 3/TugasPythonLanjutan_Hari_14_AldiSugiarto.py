# Author    : Aldi Sugiarto
# Tanggal   : 05 Agustus 2020
# Versi     : 1.0

#---------------------------------------------------Tugas Python Scraping and saving to Ms.Excel---------------------------------------------------#
#Import library untuk request open url dan beautifulsoup, serta openpyxl
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from openpyxl import Workbook
import sqlite3

#Akses alamat yang memiliki keamanan khusus
print('-'*30,'Request data dari web','-'*30)
alamat = "https://pokemondb.net/pokedex/all"
safeAdd = Request(alamat, headers={'User-Agent': 'Mozilla/5.0'})
html = urlopen(safeAdd)
data = BeautifulSoup(html, 'html.parser')

#Mendapatkan data table dari data html
print('-'*30,'Parsing data dari HTML','-'*30)
table = data.findAll("table",{"class":"data-table block-wide"})[0]
rows = table.findAll("tr")
# print(rows)
#Memasukan data e sebuah list
print('-'*30,'Memasukan data ke sebuah List','-'*30)
List = []
for row in rows:
    raw = [cell.get_text().strip() for cell in row.findAll(['td','th'])]
    del(raw[0])
    del (raw[1:3])
    print(raw)
    List.append(raw)
    if raw[0] == 'Venomoth':
        break;
print(len(List))

#Membuat koneksi dengan database
print('-'*30,'Membuat koneksi database','-'*30)
conn = sqlite3.connect('TugasPythonLanjutan_Hari_14_AldiSugiarto.db')

#Membuat table pada database
print('-'*30,'Membuat tabel pada database','-'*30)
create_pokemon_table = '''CREATE TABLE IF NOT EXISTS pokemon (
                                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                                 nama TEXT NOT NULL,
                                 hp integer NOT NULL,
                                 attack integer NOT NULL,
                                 defense integer NOT NULL,
                                 sp_attack integer NOT NULL,
                                 sp_defense integer NOT NULL,
                                 speed integer NOT NULL);'''
cursor = conn.cursor()
cursor.execute(create_pokemon_table)

#Menyisipkan data pokemon ke tabel pokemon
print('-'*30,'Menyisipkan data ke sebuah table','-'*30)
insert_query = '''INSERT INTO pokemon 
                ('nama','hp','attack','defense','sp_attack','sp_defense','speed')
                VALUES(?,?,?,?,?,?,?)'''
cursor.executemany(insert_query,List[1:])
conn.commit()
print('*'*30,'Data berhasil disisipkan','*'*30)

#Menutup koneksi database
print('-'*30,'Menutup koneksi database','-'*30)
cursor.close()
conn.close()