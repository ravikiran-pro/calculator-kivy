import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout 	#importing grid layout
class Application(App):
	def build(self):
		l1=Label(text="hi",width=100)
		l2=Label(text="bye",width=100)
		l3=Label(text="welcome",width=100)
		l4=Label(text="get away",width=100)
		layout=GridLayout(cols=2)
		layout.add_widget(l1)
		layout.add_widget(l2)
		layout.add_widget(l3)
		layout.add_widget(l4)
		return layout

application=Application()
application.run()