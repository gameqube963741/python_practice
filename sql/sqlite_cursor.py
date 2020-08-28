import sqlite3
conn = sqlite3.connect('test.sqlite') #建立資料連線
cursor = conn.cursor() #建立 cursor 物件

# 建立資料表
sqlstr = '''CREATE TABLE IF NOT EXISTS table01
("id " INTEGER PRIMARY KEY NOT NULL,
"name" TEXT NOT NULL,
"tel" TEXT NOT NULL)
'''
cursor.execute(sqlstr)

sqlstr = 'insert into table01 values(1, "David", "0977177998")'
cursor.execute(sqlstr)
conn.commit() #update
conn.close() #close connect