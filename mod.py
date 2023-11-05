from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy_garden.mapview import MapView
from kivy.uix.textinput import TextInput




Window.clearcolor = (0.8,0.8,1,1)
Window.size = (540,900)


    

class HomeScreen(Screen):
    check = {'asad': 'asad'}
    def submitbtn(self):
        if (self.ids.username.text).lower() in self.check and self.ids.password.text == self.check[(self.ids.username.text).lower()]:
            self.ids.username.text = ''
            self.ids.password.text = ''
            self.manager.current = 'First'
            self.manager.transition.direction ='left'
        else:
            if (self.ids.username.text).lower() not in self.check or self.ids.password.text != self.check[(self.ids.username.text).lower()]:
                msg_box = Popup(title='Error', content=Label(text='Invalid username or password'), size_hint=(None, None), size=(300, 150))
                msg_box.open()

class SignUp(Screen):
    check = HomeScreen.check
    def sign_up(self):
        if (self.ids.checkname.text).lower() == (self.ids.confcheckname.text).lower() and (self.ids.checkpassword.text).lower() == (self.ids.confcheckpassword.text).lower():
            self.check[(self.ids.checkname.text).lower()] = (self.ids.checkpassword.text).lower()
            self.ids.checkname.text = ''
            self.ids.checkpassword.text = ''
            self.ids.confcheckname.text = ''
            self.ids.confcheckpassword.text = ''
            msg_box = Popup(title='Confirmed', content=Label(text='Name and Password have been added to data'), size_hint=(None, None), size=(330, 150))
            msg_box.open()
            self.manager.current = 'Home'
            self.manager.transition.direction ='right'
        else:
            self.ids.checkname.text = ''
            self.ids.checkpassword.text = ''
            self.ids.confcheckname.text = ''
            self.ids.confcheckpassword.text = ''
            msg_box = Popup(title='Error', content=Label(text='Name and Password do not match!'), size_hint=(None, None), size=(300, 150))
            msg_box.open()
        

class TaskScreen(Screen):
    tasks = []

    def add_task(self):
        task = self.ids.tasks.text.strip()
        # Create a queue structure to hold no more than 5 tasks at a duration.
        if task:
            if len(self.tasks) < 5:
                self.tasks.append(task)
            else:
                self.tasks.pop(0)
                self.tasks.append(task)
            self.ids.tasks.text = ''
            msg_box = Popup(title='Confirm', content=Label(text='Task has been added'), size_hint=(None, None), size=(300, 150))
            msg_box.open()
            self.update_task_list()

    def update_task_list(self):
        task_list_screen = self.manager.get_screen('List')
        for i in range(len(self.tasks)):
            task_list_screen.ids['task_' + str(i+1)].text = self.tasks[i]

    def build_map(self):
        self.mapview = MapView(zoom=11, lat=37.7749, lon=-122.4194)
        self.search_field = TextInput(pos_hint={'center_x': 0.5, 'top': 0.97}, size_hint=(0.8, None),
                                         height=40, hint_text='Search location')
        self.search_field.bind(text=self.search_location)
        self.add_widget(self.search_field)
        self.add_widget(self.mapview)

    def search_location(self, value):
        if value and len(value) > 2:
            self.mapview.search_location(value)
        


class TaskList(Screen):
    pass





class Manager(ScreenManager):
    pass

    
class ModApp(App):
    def build(self):
        pass

ModApp().run()