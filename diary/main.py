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
   
# 0 being off 1 being on as in true / false 
# you can use 0 or 1 && True or False 
Config.set('graphics', 'resizable', True) 
class Application(App):
	def build(self):
		Window.clearcolor=(1,1,1,0)
		img = Image(source ='logo.png')
		img.allow_stretch = True
		img.opacity = 1
		move=FloatLayout()
		label=Label(text="""[color=ff3333]Enter password[/color]""",pos=(Window.width/2-40,160),width=40,height=10,size_hint=(None,None),markup=True)
		password=TextInput(multiline=False,pos=(Window.width/2-70,120),width=100,height=30,size_hint=(None,None),font_size="16sp")
		button=Button(text="login",pos=(Window.width/2-40,100),width=40,height=10,size_hint=(None,None))
		move.add_widget(label)
		move.add_widget(img)
		move.add_widget(password)
		move.add_widget(button) 
		return move

app=Application()
app.run()
