import kivy
from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout 	#importing float layout(non fixed layout)
from kivy.uix.scatter import Scatter
from kivy.uix.boxlayout import BoxLayout

class Application(App):
	def build(self):
		name=Label(text="[color=ff4444][b]Name :[/b][/color]",markup=True)
		t=TextInput(text="enter your name")

		boxlayout=BoxLayout(orientation="vertical")

		#position movable elements
		scatter = Scatter()
		scatter.add_widget(t)

		#position over place elements(i.e element over elements are placed)
		floatlayout=FloatLayout()
		floatlayout.add_widget(name)
		
		#position elements via grid method (vertical and horizontal methods are available)
		boxlayout.add_widget(scatter)
		boxlayout.add_widget(floatlayout)
		return boxlayout

application=Application()
application.run()