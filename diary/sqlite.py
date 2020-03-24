import sqlite3
class Connection():
	def __init__(self):
		self.conn=sqlite3.connect('diaryuserdata')
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

'''
con=Connection()
con.createtable("pwmanage","name varchar(100),","age int")
con.insertintotable("pwmanage","'ravi','23'","name,","age")
con.insertintotable("pwmanage","'kiran','29'","name,","age")
con.insertintotable("pwmanage","'preethi','22'","name,","age")
size=con.size("pwmanage")
print(size)
values=con.getvalues("*","pwmanage")
for i in values:
	print(i)
'''