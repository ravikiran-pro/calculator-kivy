import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
class Application(App):
	def build(self):
		self.swap=Button(text="change page",on_press=self.change)
		self.master = BoxLayout(orientation="vertical")
		self.master.add_widget(self.swap)
		return self.master
	def change(self,event):
		self.master.remove_widget(self.swap)

application=Application()
application.run()