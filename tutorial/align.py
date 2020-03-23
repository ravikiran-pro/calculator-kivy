import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
#kivy import window for size
from kivy.core.window import Window
'''
Window.width -->getting window width
Window.height -->getting window height

size_hint=(None,None)	allows to change position
pos=(0,0)				sets position of the widget
size=(0,0)				sets size of the widget
'''
class Application(App):
	def build(self):
		#Window.size=(300,300)		#setting size of window
		return Label(text="welcome",pos=(0,Window.height-100),size_hint=(None,None),color=[105, 106, 188, 1])

application=Application()
application.run()