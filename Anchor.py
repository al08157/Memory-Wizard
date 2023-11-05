from kivy.app import App 
from kivy.uix.button import Button 
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window 


Window.clearcolor = (0.8,0.8,1,1)


class MyLayoutApp(App):
    def build(self):
        layout = FloatLayout()
        btn1 = Button(text = 'Click_1', pos_hint = {'center_x':0.08, 'center_y': 0.08}, size_hint =(None, None), width = 100, height = 50 )
        btn2 = Button(text = 'Click_2', pos_hint = {'center_x':0.08, 'center_y': 0.92}, size_hint =(None, None), width = 100, height = 50 )
        btn3 = Button(text = 'Click_3', pos_hint = {'center_x':0.92, 'center_y': 0.08}, size_hint =(None, None), width = 100, height = 50 )
        btn4 = Button(text = 'Click_4', pos_hint = {'center_x':0.92, 'center_y': 0.92}, size_hint =(None, None), width = 100, height = 50 )
        btn5 = Button(text = 'Click_5', pos_hint = {'center_x':0.5, 'center_y': 0.5}, size_hint =(None, None), width = 100, height = 50 )
        layout.add_widget(btn1)
        layout.add_widget(btn2)
        layout.add_widget(btn3)
        layout.add_widget(btn4)
        layout.add_widget(btn5)

        return layout
    
    
MyLayoutApp().run()