import csv
with open('test.csv','w',encoding='utf-8-sig') as csvfile:
    fieldnames = ['name','high','weight']
    writer = csv.DictWriter(csvfile, fieldnames = fieldnames)

    writer.writeheader()

    writer.writerow({'name':'chiu','high':168,'weight':65})
    writer.writerow({'name':'David','high':170,'weight':68})