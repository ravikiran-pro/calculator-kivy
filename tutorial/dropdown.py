import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
class Application(App):
	def build(self):
		l1=Label(text="start",size=(25,25),size_hint=(None,None))
		"""
		l2=Label(text="start",width=1,size_hint=(0.1,1),size=(10,10))
		l3=Label(text="start",width=1,size_hint=(0.1,1),size=(10,10))
		l4=Label(text="start",width=1,size_hint=(0.1,1),size=(10,10))
		"""
		sidepanel=BoxLayout(orientation='vertical')
		sidepanel.add_widget(l1)
		"""
		sidepanel.add_widget(l2)
		sidepanel.add_widget(l3)
		sidepanel.add_widget(l4)
		"""
		button=Button(text="click me",size_hint=(0.9,1))
		frame=BoxLayout(spacing=10)
		frame.add_widget(sidepanel)
		frame.add_widget(button)
		return frame

application=Application()
application.run()