import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

class Application(App):
	def build(seld):
		welcome=Label(text="[u][i][color=ff3333] hi this is john [/color][/i][/u]",font_size=50,markup=True)
		entry=TextInput(text="write something",multiline=False)


		welcome1=Label(text="[u][i][color=ff3333] hi this is john [/color][/i][/u]",font_size=50,markup=True)
		entry1=TextInput(text="write something",multiline=False)
		'''
			Cannot place both items hence individual places should happen 
			Hence, boxlayout is used 
		'''
		w=BoxLayout(orientation="vertical")
		'''BoxLayout( orientation=vertical | horizontal)'''
		w.add_widget(welcome)
		w.add_widget(entry)
		w.add_widget(welcome1)
		w.add_widget(entry1)
						
		return w
		
application =Application()
application.run()