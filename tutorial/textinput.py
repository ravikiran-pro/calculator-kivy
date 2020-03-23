import kivy
from kivy.app import App
from kivy.uix.textinput import TextInput

class Application(App):	
	def build(self):
		return TextInput(text="hello",font_size=50,multiline=False,height=5)

win=Application()
win.run()