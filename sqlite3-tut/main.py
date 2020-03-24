import sqlite3
try:
	connection=sqlite3.connect("demo.db")
except:
	print("database not available")
finally:
	mycursor=connection.cursor()

#mycursor.execute("create table pwmanager(password varchar(100))")
'''
mycursor.execute("insert into pwmanager values('ravikiran')")
mycursor.execute("insert into pwmanager values('ravikiran')")
mycursor.execute("insert into pwmanager values('ravikiran')")
mycursor.execute("insert into pwmanager values('ravikiran')")
'''
cur=mycursor.execute("select * from pwmanager")
print(cur.fetchall())
#connection.commit()	#commit to enforce changes on db after insertion
connection.close()



