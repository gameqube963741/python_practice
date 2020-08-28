import csv
with open('test.csv','w',encoding = 'utf-8-sig') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['姓名','身高','體重'])
    writer.writerow(['chiu','170','58'])
    writer.writerow(['kit','183','78'])