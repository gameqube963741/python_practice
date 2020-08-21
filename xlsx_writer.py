import openpyxl

workbook = openpyxl.Workbook()
sheet = workbook.worksheets[0]
sheet['A1'] = 'Hello'
sheet['B1'] = 'world'

listtile = ['name','phonenum']
sheet.append(listtile)
listdata = ['David','0977177998']
sheet.append(listdata)

workbook.save('test.xlsx')