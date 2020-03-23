import kivy
kivy.require('1.10.1')
from kivy.app import App
from kivy.uix.label import Label	#inporting label

class application(App):
	def build(self):
		return Label(text="""[color=ff3333] hi mom ,[/color]"""
							+"""[color=ff3333][b]'Label'[/b] is Added [/color]\n
							welcome to home back after years"""
							,font_size='45sp',markup=True)

		'''
		Label properties
				>>	font_size = 'X sp'
				>> 	markup=True 			#to visible color of fonts
				dom type
				--------
				 [color=f33333] [/color]
				  [b][/b] -> Activate bold text
				  [i][/i] -> Activate italic text
				  [u][/u] -> Underlined text
				  [s][/s] -> Strikethrough text
		'''

hello=application()
hello.run()
