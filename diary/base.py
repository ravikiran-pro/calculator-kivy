import kivy
from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.config import Config 
from sqlite import Connection
from datetime import date as today
from kivy.uix.scrollview import ScrollView
from kivy.app import runTouchApp

Config.set('graphics', 'resizable', True) 
screenwidth=0
screenheight=0
rotate=False
choice=1
def WXY(size):
	return (screenwidth/100)*(size/3.2)
def HXY(size):
	return (screenheight/100)*(size/4.8)

class Viewer():
	def __init__(self,master):
		self.master=master
		Window.clearcolor=(0,1,0,5)
		self.addb=Button(text="ADD",pos=(WXY(2),HXY(450)),width=WXY(60),height=HXY(30),size_hint=(None,None),font_size=HXY(16))
		self.addb.bind(on_press=self.adder)
		self.master.add_widget(self.addb)
		self.layout = GridLayout(cols=1, spacing=HXY(10), size_hint_y=None)
		self.layout.bind(minimum_height=self.layout.setter('height'))
		self.connection=Connection()
		self.values=self.connection.getvaluesasc("date,content","diarydata")
		self.lists=[]
		index=0
		for date,content in self.values:
			label=Label(text=str(date))
			self.lists.append(Button(text=content+"\n"+str(date), size_hint_y=None, height=HXY(250),font_size=HXY(18),halign="left", valign="middle"))
			self.lists[index].bind(size=self.lists[index].setter('text_size'))
			self.lists[index].bind(on_press=self.popuptriger)
			self.layout.add_widget(label)
			self.layout.add_widget(self.lists[index])
			index+=1
		self.connection.conn.close();
		self.root = ScrollView(size=(WXY(310),HXY(440)),pos=(WXY(5),HXY(10)),size_hint=(None,None))
		self.root.add_widget(self.layout)
		self.master.add_widget(self.root)

	def on_rotate(self):
		self.addb.pos=(WXY(2),HXY(450))
		self.addb.width=WXY(60)
		self.addb.height=HXY(30)
		self.addb.font_size=HXY(16)
		self.root.size=(WXY(310),HXY(440))
		self.root.pos=(WXY(5),HXY(0))
		self.layout.spacing=HXY(4)
		index=0
	def popuptriger(self,event):
		editButton = Button(text = "Edit")
		deleteButton = Button(text = "Delete")
		cancelButton = Button(text = "Cancel")
		layout = BoxLayout()
		self.identity=event.text
		self.userpriority=Popup(title="Do you wish to continue",content=layout,width=Window.width,height=HXY(100),size_hint=(None,None))
		layout.add_widget(deleteButton)
		layout.add_widget(editButton)
		layout.add_widget(cancelButton)

		editButton.bind(on_press=self.editviewer)
		deleteButton.bind(on_press=self.deletelists)
		cancelButton.bind(on_press=self.userpriority.dismiss)
		
		self.userpriority.open()
	def deletelists(self,event):
		self.connection=Connection()
		query="delete from diarydata where date='{}'".format(self.identity[-10:])
		self.connection.delete(query)
		self.connection.conn.commit()
		self.userpriority.dismiss()
		self.master.remove_widget(self.root)
		self.master.remove_widget(self.addb)
		self.viewer=Viewer(self.master)
	def editviewer(self,event):
		self.connection=Connection()
		query="delete from diarydata where date='{}'".format(self.identity[-10:])
		self.connection.delete(query)
		self.connection.conn.commit()
		self.userpriority.dismiss()
		self.master.remove_widget(self.root)
		self.master.remove_widget(self.addb)
		self.viewer=Notepad(self.master,self.identity[:-10],self.identity[-10:])
	def adder(self,event):
		self.master.remove_widget(self.addb)
		self.master.remove_widget(self.root)
		self.master.remove_widget(self.root)
		self.master.remove_widget(self.addb)
		self.notepad=Notepad(self.master,"Empty your heart",today.today())
		global choice 
		choice=3

class Application(App):
	def build(self):
		Window.clearcolor=(1,1,1,0)
		#Window.size=(320,480)
		self.connection=Connection()
		self.img = Image(source ='net.jpeg',size_hint=(None,None))
		self.img.allow_stretch = True
		self.img.opacity = 1
		self.password=TextInput(text="password",multiline=False,size_hint=(None,None))
		self.loginbutton=Button(text="Unlock",size_hint=(None,None))
		self.loginbutton.bind(on_press=self.login)
		self.registerbutton=Button(text="Register",size_hint=(None,None))
		self.registerbutton.bind(on_press=self.register)
		#creating layout based on conditions
		cols=self.connection.size("pwmanager")
		self.master=FloatLayout()
		if cols is not 1:
			self.master.add_widget(self.registerbutton)
		else:
			self.master.add_widget(self.loginbutton)  
		self.master.add_widget(self.img)
		self.master.add_widget(self.password)
		self.master.bind(size=self.on_rotate)
		return self.master

	def login(self,event):
		passwordtext=self.connection.getvalues("*","pwmanager")
		userentry=""
		for i in passwordtext.fetchone():
			userentry=i
		if(userentry==self.password.text):
			self.master.remove_widget(self.loginbutton)
			self.master.remove_widget(self.img)
			self.master.remove_widget(self.password)
			self.connection.conn.close()
			self.viewer=Viewer(self.master)
		else:
			self.password.text="Retry"
		global choice
		choice=2
	def register(self,event):
		if(self.password.text is not ""):
			values="('{}')".format(str(self.password.text))
			columnname="('{}')".format("password")	
			self.connection.insertintotable("pwmanager",columnname,values)
			self.master.remove_widget(self.registerbutton)	
			self.master.add_widget(self.loginbutton)
			self.password.text=""
	def on_rotate(self,event,event1):
		global screenheight
		global screenwidth
		global choice
		screenheight=Window.height
		screenwidth=Window.width
		if(choice==1):
			self.img.pos=(WXY(60),HXY(263))
			self.img.width=WXY(207)
			self.img.height=HXY(164)

			self.password.pos=(WXY(53),HXY(180))
			self.password.width=WXY(208)
			self.password.height=HXY(37)
			self.password.font_size=HXY(18)

			self.loginbutton.pos=(WXY(82),HXY(117))
			self.loginbutton.width=WXY(146)
			self.loginbutton.height=HXY(40)
			self.loginbutton.font_size=HXY(18)
		
			self.registerbutton.pos=(WXY(82),HXY(117))
			self.registerbutton.width=WXY(146)
			self.registerbutton.height=HXY(40)			
		elif (choice==2):
			self.viewer.on_rotate()
		elif (choice==3):
			self.viewer.notepad.on_rotate()

class Notepad():
	def __init__(self,master,content,date):
		self.master=master
		self.datesetter=TextInput(text=str(date),pos=(WXY(5),HXY(440)),width=WXY(146),height=HXY(40),font_size=HXY(25),halign="left",size_hint=(None,None),multiline=False)
		self.submit=Button(text="submit",pos=(WXY(174),HXY(440)),width=WXY(141),height=HXY(40),size_hint=(None,None),font_size=HXY(25))
		self.submit.bind(on_press=self.popuptriger)
		self.content=TextInput(text=content,pos=(WXY(5),HXY(5)),width=WXY(310),height=HXY(430),font_size=(HXY(18)),size_hint=(None,None))
		self.master.add_widget(self.datesetter)
		self.master.add_widget(self.submit)
		self.master.add_widget(self.content)
		Window.clearcolor=(0,1,0,5)

	def on_rotate(self):
		global screenheight
		global screenwidth
		screenheight=Window.height
		screenwidth=Window.width

		self.datesetter.pos=(WXY(5),HXY(440))
		self.datesetter.width=WXY(146)
		self.datesetter.height=HXY(40)
		self.datesetter.font_size=HXY(25)

		self.submit.pos=(WXY(174),HXY(440))		
		self.submit.width=WXY(141)
		self.submit.height=HXY(40)
		self.submit.font_size=HXY(25)
        
		self.content.pos=(WXY(5),HXY(5))		
		self.content.width=WXY(310)
		self.content.height=HXY(430)
		self.content.font_size=HXY(18)
	def popuptriger(self,event):
		closeButton = Button(text = "Close")
		cancelButton = Button(text = "cancel")
		saveButton = Button(text = "Save")

		layout = BoxLayout()
		self.userpriority=Popup(title="Do you wish to continue",content=layout,width=Window.width,height=HXY(100),size_hint=(None,None))
		layout.add_widget(cancelButton)
		layout.add_widget(saveButton)
		layout.add_widget(closeButton)

		saveButton.bind(on_press=self.saveswapper)
		closeButton.bind(on_press=self.nonsaveswapper)
		cancelButton.bind(on_press=self.userpriority.dismiss)
		
		self.userpriority.open()
	def saveswapper(self,event):
		self.connection=Connection()
		values="('{}','{}')".format(str(self.datesetter.text),str(self.content.text))
		columnname="('{}','{}')".format("date","content")
		query="delete from diarydata where date='{}'".format(self.datesetter.text)
		self.connection.delete(query)
		self.connection.insertintotable("diarydata",columnname,values)
		self.connection.conn.close()
		self.removelayout()
	def nonsaveswapper(self,event):
		self.removelayout()
	def removelayout(self):
		res=0;
		for i in self.datesetter.text:
			if(i>='0' and i<'9'):	
				res=(res*10)+int(i)
		self.userpriority.dismiss()
		self.master.remove_widget(self.datesetter)
		self.master.remove_widget(self.content)
		self.master.remove_widget(self.submit)
		global choice
		choice=2
		self.viewer=Viewer(self.master)

app=Application()
app.run()
