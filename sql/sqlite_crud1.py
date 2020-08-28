import sqlite3
conn = sqlite3.connect('test.sqlite') #建立資料庫連線

# 建立資料表
sqlstr = '''CREATE TABLE 'contact'
("id" INTEGER PRIMARY KEY NOT NULL,
"name" TEXT NOT NULL,
"tel" TEXT NOT NULL)
'''

conn.execute(sqlstr)
conn.commit() #update
conn.close() #close connect