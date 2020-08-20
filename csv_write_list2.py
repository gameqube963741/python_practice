import csv

csv_table = [
    ['name','high','weight'],
    ['chiu',168,65],
    ['david',170,68]
]

with open('n_H_W.csv','w',encoding='utf-8-sig') as file:
    writer = csv.writer(file)
    writer.writerows(csv_table)