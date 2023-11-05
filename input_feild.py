from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput 
from kivy.uix.button import Button 
from kivy.core.window import Window 


Window.clearcolor = (0.8,0.8,1,1)

class MyApp(App):
    check = {'asad':'Khanpathan09'}
    def build(self):
        layout = GridLayout(cols = 1,row_force_default = True, row_default_height = 50, padding = 150, spacing = 40)
        self.username  = TextInput(text = 'Enter your name ')
        self.password  = TextInput(text = 'Enter your password ')
        self.Login = Button(text = 'Log In ',on_press = lambda obj: self.submitbtn(obj, self.check))

        layout.add_widget(self.username)
        layout.add_widget(self.password)
        layout.add_widget(self.Login)
        return layout
    def submitbtn(self,obj,check):
        if (self.username.text).lower() in check and self.password.text == check[(self.username.text).lower()]:
            print('your name and password match the data, Welcome! ')
        else:
            if (self.username.text).lower() not in check:
                print('Invalid name')
            elif self.password.text != check[(self.username.text).lower()]:
                print('Invalid password!')

MyApp().run()