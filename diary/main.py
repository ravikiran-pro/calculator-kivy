import kivy
from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.config import Config 
from sqlite import Connection
   
Config.set('graphics', 'resizable', True) 
class Application(App):
	def build(self):
		Window.clearcolor=(1,1,1,0)
		self.connection=Connection()
		self.img = Image(source ='logo.png')
		self.img.allow_stretch = True
		self.img.opacity = 1
		self.label=Label(text="""[color=ff3333][b]Enter password[/b][/color]""",pos=(Window.width/2-20,160),width=40,height=10,size_hint=(None,None),markup=True)
		self.password=TextInput(multiline=False,pos=(Window.width/2-70,120),width=130,height=30,size_hint=(None,None),font_size="16sp")
		self.loginbutton=Button(text="Login",pos=(Window.width/2-40,100),width=70,height=10,size_hint=(None,None))
		self.loginbutton.bind(on_press=self.login)
		self.registerbutton=Button(text="Register",pos=(Window.width/2-40,100),width=70,height=10,size_hint=(None,None))
		self.registerbutton.bind(on_press=self.register)
		#creating layout based on conditions
		self.move=FloatLayout()
		self.connection=Connection()
		cols=self.connection.size("pwmanager")
		if cols is not 1:
			self.move.add_widget(self.registerbutton)
		else:
			self.move.add_widget(self.loginbutton)  
		self.move.add_widget(self.label)
		self.move.add_widget(self.img)
		self.move.add_widget(self.password)
		return self.move

	def login(self,event):
		passwordtext=self.connection.getvalues("*","pwmanager")
		userentry=""
		for i in passwordtext.fetchone():
			userentry=i
		if(userentry==self.password.text):
			self.move.remove_widget(self.loginbutton)
			self.move.remove_widget(self.label)
			self.move.remove_widget(self.img)
			self.move.remove_widget(self.password)
			self.connection.conn.close()
		else:
			self.password.text="Retry"
	def register(self,event):
		if(self.password.text is not ""):
			self.connection.insertintotable("pwmanager","'"+self.password.text+"'","password")
			self.move.remove_widget(self.registerbutton)	
			self.move.add_widget(self.loginbutton)
			self.password.text=""

app=Application()
app.run()
