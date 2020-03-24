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
   
Config.set('graphics', 'resizable', True) 
class Application(App):
	def build(self):
		Window.clearcolor=(1,1,1,0)
		self.img = Image(source ='logo.png')
		self.img.allow_stretch = True
		self.img.opacity = 1
		self.move=FloatLayout()
		self.label=Label(text="""[color=ff3333]Enter password[/color]""",pos=(Window.width/2-40,160),width=40,height=10,size_hint=(None,None),markup=True)
		self.password=TextInput(multiline=False,pos=(Window.width/2-70,120),width=100,height=30,size_hint=(None,None),font_size="16sp")
		self.button=Button(text="login",pos=(Window.width/2-40,100),width=40,height=10,size_hint=(None,None))
		self.button.bind(on_press=self.login)
		self.move.add_widget(self.label)
		self.move.add_widget(self.img)
		self.move.add_widget(self.password)
		self.move.add_widget(self.button) 
		return self.move
	def login(self,event):
		self.move.remove_widget(self.button)
		self.move.remove_widget(self.label)
		self.move.remove_widget(self.img)
		self.move.remove_widget(self.password)
app=Application()
app.run()
