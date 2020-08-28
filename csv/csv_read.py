# import csv 
# with open ('test.csv', newline='',encoding='utf-8-sig') as csvfile:
#     rows = csv.reader(csvfile)
#     for row in rows:
#         print(row)


import csv 
with open ('test.csv', newline='',encoding='utf-8-sig') as csvfile:
    rows = csv.DictReader(csvfile)
    for row in rows:
        print(row['name'],row['high'],row['weight'])