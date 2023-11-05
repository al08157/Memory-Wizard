from kivy.app import App
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

Window.clearcolor = (1,0.8,0.8,1)

class MyApp(App):
    def build(self):
        layout = GridLayout(rows = 2, row_force_default = True, row_default_height = 60, col_force_default = True, col_default_width = 80)
        self.text_input = TextInput(text = '', multiline = False)
        btn1 = Button(text = 'Click Me_1', font_size = '9sp', size_hint = (0.3,0.3), on_press = self.btn_click1)
        btn2 = Button(text = 'Click Me_2', font_size = '9sp', size_hint = (0.3,0.3), on_press = self.btn_click2)
        btn3 = Button(text = 'Click Me_3', font_size = '9sp', size_hint = (0.3,0.3), on_press = self.btn_click3)
        btn4 = Button(text = 'Click Me_4', font_size = '9sp', size_hint = (0.3,0.3), on_press = self.btn_click4)
        layout.add_widget(self.text_input)
        layout.add_widget(btn1)
        layout.add_widget(btn2)
        layout.add_widget(btn3)
        layout.add_widget(btn4)

        return layout
    
    


    def btn_click1(self,btn1):
        print('Hi')
    def btn_click2(self,btn2):
        name = self.text_input.text
        print(f'{name}')
    def btn_click3(self,btn3):
        print('how ')
    def btn_click4(self,btn4):
        print('are you?')

MyApp().run() 