import sqlite3

class connection():
	def __init__(self):
		self.conn=sqlite3.connect('diaryuserdata.db')
		self.mycursor=self.conn.cursor()
	def createtable(self,tbname,*data):
		query="create table "+tbname+"( "
		for i in data:
			query+=i
		query+=")"
		self.mycursor.execute(query)
		self.conn.commit()
	def insertintotable(self,tbname,values,*columnname):
		query="insert into "+tbname+"("
		for i in columnname:
			query+=i
		query+=")"
		query+="values("+values+")"
		self.mycursor.execute(query)
		self.conn.commit()
	def getvalues(self,selector,tbname):
		query="select "+selector+" from "+tbname
		return self.mycursor.execute(query)
	def size(self,tbname):
		datas=self.getvalues("*",tbname)
		return len(datas.fetchall())
con=connection()
con.createtable("pwmanager","name varchar(100),","age int")
con.insertintotable("pwmanager","'ravi','23'","name,","age")
con.insertintotable("pwmanager","'kiran','29'","name,","age")
con.insertintotable("pwmanager","'preethi','22'","name,","age")
size=con.size("pwmanager")
print(size)
values=con.getvalues("*","pwmanager")
for i in values:
	print(i)


