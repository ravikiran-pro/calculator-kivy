
# Program to explain how to creat drop-down in kivy  
     
# import kivy module     
import kivy   
       
# base Class of your App inherits from the App class.     
# app:always refers to the instance of your application    
from kivy.app import App  
kivy.require('1.9.0')  
from kivy.uix.dropdown import DropDown 
from kivy.uix.button import Button 
from kivy.base import runTouchApp  

class Application(App):
	def build(self):
		self.dropdown = DropDown() 
		for index in range(10):
			btn = Button(text ='Value % d' % index, size_hint_y = None, height = 40,on_press=self.reply) 
			self.dropdown.add_widget(btn) 
		mainbutton = Button(text ='Hello', size_hint =(None, None), pos =(0, 500)) 
		mainbutton.bind(on_release = self.dropdown.open) 
		self.dropdown.bind(on_select = lambda instance, x: setattr(mainbutton, 'text', x)) 
		runTouchApp(mainbutton) 
		return self.dropdown
	def reply(self,event):
		self.dropdown.select(event.text)

application=Application()
application.run()
