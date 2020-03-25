import kivy
from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.config import Config 
from sqlite import Connection
from datetime import date as today
Config.set('graphics', 'resizable', True) 
screenwidth=0
screenheight=0
rotate=False
choice=1
def WXY(size):
	return (screenwidth/100)*(size/3.2)
def HXY(size):
	return (screenheight/100)*(size/4.8)

class Notepad():
	def __init__(self,master):
		self.master=master
		self.datesetter=TextInput(text=str(today.today()),pos=(WXY(5),HXY(440)),width=WXY(146),height=HXY(40),font_size=HXY(25),size_hint=(None,None))
		self.submit=Button(text="submit",pos=(WXY(174),HXY(440)),width=WXY(141),height=HXY(40),size_hint=(None,None),font_size=HXY(25))
		self.content=TextInput(text=str(today.today()),pos=(WXY(5),HXY(5)),width=WXY(310),height=HXY(430),size_hint=(None,None))
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

class Application(App):
	def build(self):
		Window.clearcolor=(1,1,1,0)
		Window.size=(320,480)
		self.connection=Connection()
		self.img = Image(source ='net.jpeg',size_hint=(None,None))
		self.img.allow_stretch = True
		self.img.opacity = 1
		self.password=TextInput(text="Ravikiran@ms1",multiline=False,size_hint=(None,None))
		self.loginbutton=Button(text="Unlock",size_hint=(None,None))
		self.loginbutton.bind(on_press=self.login)
		self.registerbutton=Button(text="Register",size_hint=(None,None))
		self.registerbutton.bind(on_press=self.register)
		#creating layout based on conditions
		cols=self.connection.size("pwmanager")
		self.move=FloatLayout()
		if cols is not 1:
			self.move.add_widget(self.registerbutton)
		else:
			self.move.add_widget(self.loginbutton)  
		self.move.add_widget(self.img)
		self.move.add_widget(self.password)
		self.move.bind(size=self.on_rotate)
		return self.move

	def login(self,event):
		passwordtext=self.connection.getvalues("*","pwmanager")
		userentry=""
		for i in passwordtext.fetchone():
			userentry=i
		if(userentry==self.password.text):
			self.move.remove_widget(self.loginbutton)
			self.move.remove_widget(self.img)
			self.move.remove_widget(self.password)
			self.connection.conn.close()
			self.notepad=Notepad(self.move)
		else:
			self.password.text="Retry"
		global choice
		choice=2
	def register(self,event):
		if(self.password.text is not ""):
			self.connection.insertintotable("pwmanager","'"+self.password.text+"'","password")
			self.move.remove_widget(self.registerbutton)	
			self.move.add_widget(self.loginbutton)
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
			self.notepad.on_rotate()
app=Application()
app.run()