# Author    : Aldi Sugiarto
# Tanggal   : 08 Agustus 2020
# Versi     : 1.0
# Email     : aldisugiarto5@gmail.com

#---------------------------------------------------Tugas Python Ms.Excel to JSON---------------------------------------------------#
#Import library
from openpyxl import load_workbook
import json

#Membuat class
class convert_excel_to():
    def open_excel(self,fileName):
        data = load_workbook(filename=fileName)
        sheet = data.active
        return sheet
    def convert_dict(self,sheet):
        pokemon_data = []
        for row_index in range(len(sheet['A'])):
            if sheet[row_index + 1][0].value == "Name":
                continue
            pokemon = {}
            pokemon['nama'] = sheet[row_index + 1][0].value
            pokemon['type'] = sheet[row_index + 1][1].value
            pokemon['total'] = sheet[row_index + 1][2].value
            pokemon['hp'] = sheet[row_index + 1][3].value
            pokemon['attack'] = sheet[row_index + 1][4].value
            pokemon['defense'] = sheet[row_index + 1][5].value
            pokemon['SpAttack'] = sheet[row_index + 1][6].value
            pokemon['SpDefense'] = sheet[row_index + 1][7].value
            pokemon['speed'] = sheet[row_index + 1][8].value

            pokemon_data.append(pokemon)
        return pokemon_data
    def generate_file_json(self,data,file):
        with open(file, 'w') as outfile:
            json.dump(data, outfile)
#Membuat default log
def log(string):
    print('#','-'*20,string,'-'*20,'#')
#Proses membuka file Ms.Excel dan generate file JSON
log('Inisialisasi class')
convert = convert_excel_to()
log('Mengambil data sheet dari file .xlsx')
data_excel = convert.open_excel('pokemon_db.xlsx')
log('Convert data sheet ke dictionary')
data = convert.convert_dict(data_excel)
log('Generate file JSON')
convert.generate_file_json(data,'aldi.json')