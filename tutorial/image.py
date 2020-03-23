import kivy
from kivy.app import App
from kivy.uix.image import Image

class Application(App):
	def build(self):
		return Image(source="loadimage.jpeg",allow_stretch=True)

application=Application()
application.run()
