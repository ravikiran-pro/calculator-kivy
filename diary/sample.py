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

screenwidth=0
screenheight=0
rotate=False
choice=1
class Application(App):
	def build(self):
		Window.clearcolor=(1,1,1,0)
		Window.size=(320,480)
		self.connection=Connection()
		self.img = Image(source ='net.jpeg')
		self.img.allow_stretch = True
		self.img.opacity = 1
		self.password=TextInput(text="Ravikiran@ms1",multiline=False,height=10,size_hint=(None,None))
		self.loginbutton=Button(text="Unlock")
		self.loginbutton.bind(on_press=self.login)
		self.registerbutton=Button(text="Register")
		self.registerbutton.bind(on_press=self.register)
		#creating layout based on conditions
		cols=self.connection.size("pwmanager")
		self.master=BoxLayout(orientation="vertical")
		self.master.add_widget(self.img)
		self.master.add_widget(self.password)
		if cols is not 1:
			self.master.add_widget(self.registerbutton)
		else:
			self.master.add_widget(self.loginbutton)  
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
		else:
			self.password.text="Retry"

	def register(self,event):
		if(self.password.text is not ""):
			values="('{}')".format(str(self.password.text))
			columnname="('{}')".format("password")	
			self.connection.insertintotable("pwmanager",columnname,values)
			self.master.remove_widget(self.registerbutton)	
			self.master.add_widget(self.loginbutton)
			self.password.text=""
app=Application()
app.run()