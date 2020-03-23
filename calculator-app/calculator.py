import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
class Application(App):
    def build(self):
        master = BoxLayout(orientation="vertical")
        
        self.display=Label(text="",font_size="32sp")
        subslide0 = BoxLayout(orientation="horizontal") 
        subslide0.add_widget(self.createbutton('^'))
        subslide0.add_widget(self.createbutton('%'))
        subslide0.add_widget(self.createbutton('c'))
        subslide0.add_widget(self.createbutton('<-'))


        subslide1 = BoxLayout(orientation="horizontal") 
        subslide1.add_widget(self.createbutton('1'))
        subslide1.add_widget(self.createbutton('2'))
        subslide1.add_widget(self.createbutton('3'))
        subslide1.add_widget(self.createbutton('+'))

        subslide2 = BoxLayout(orientation="horizontal")
        subslide2.add_widget(self.createbutton('4'))
        subslide2.add_widget(self.createbutton('5'))
        subslide2.add_widget(self.createbutton('6'))
        subslide2.add_widget(self.createbutton('-'))
        
        subslide3 = BoxLayout(orientation="horizontal")
        subslide3.add_widget(self.createbutton('7'))
        subslide3.add_widget(self.createbutton('8'))
        subslide3.add_widget(self.createbutton('9'))
        subslide3.add_widget(self.createbutton('*'))
        

        subslide4 = BoxLayout(orientation="horizontal")
        subslide4.add_widget(self.createbutton('0'))
        subslide4.add_widget(self.createbutton('.'))
        subslide4.add_widget(self.createbutton('='))
        subslide4.add_widget(self.createbutton('/'))

        master.add_widget(self.display)
        master.add_widget(subslide0)
        master.add_widget(subslide1)
        master.add_widget(subslide2)
        master.add_widget(subslide3)
        master.add_widget(subslide4)
        
        return master

    def createbutton(self,var):
        self.btn=Button(text='[b]'+var+'[/b]',font_size=32,markup=True)
        self.btn.bind(on_press = self.callback)
        return self.btn
        
    def callback(self,callback):
        if callback.text[3:4] is  '=' : 
            if '^' not in self.display.text:
                self.display.text=str(eval(self.display.text))
            else:
                index=0
                for i in self.display.text:
                    if i is '^':
                        break
                    index+=1
                self.display.text=str(eval(self.display.text[index+1:])**eval(self.display.text[:index]))

        elif callback.text[3:4] is 'c':
            self.display.text=" "
        elif callback.text[3:4] is '<':
            self.display.text=self.display.text[:len(self.display.text)-1]
        else:
            getter=self.display.text
            setter=getter+callback.text[3:4]        
            self.display.text=setter


application=Application()
application.run()
