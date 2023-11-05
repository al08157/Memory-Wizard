from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager, SlideTransition
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.core.window import Window
from buildingmapview import BuildingMapView
from kivy.uix.button import Button
from kivy_garden.mapview import MapView, MapMarker
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.relativelayout import RelativeLayout
import set




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
        if (self.ids.checkname.text) == (self.ids.confcheckname.text) and (self.ids.checkpassword.text) == (self.ids.confcheckpassword.text):
            self.check[(self.ids.checkname.text)] = (self.ids.checkpassword.text)
            self.ids.checkname.text = ''
            self.ids.checkpassword.text = ''
            self.ids.confcheckname.text = ''
            self.ids.confcheckpassword.text = ''
            print(self.check)
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
    coordinate_set = set.coordinate_set
    
   

    def __init__(self, **kwargs):
        super(TaskScreen, self).__init__(**kwargs)
        self.mapview = BuildingMapView()
        self.add_widget(self.mapview)

    def on_enter(self):
        try:
            self.mapview.start_getting_markets_in_fov()
        except:
            pass 

        
    
 
    def add_task(self):
        task = self.ids.tasks.text.strip()
        app = App.get_running_app()
        self.selected_locations = app.selected_locations
    
        new_task = {'text': task, 'locations': self.selected_locations}
        # Create a circular queue structure to hold no more than 5 tasks at a duration.
        if task:
            if len(self.tasks) < 5:
                self.tasks.append(new_task)
            else:
                self.tasks.pop(0)
                self.tasks.append(new_task)
            self.ids.tasks.text = ''
            app.selected_locations = []
            print(self.tasks)
            msg_box = Popup(title='Confirm', content=Label(text='Task has been added'), size_hint=(None, None), size=(300, 150))
            msg_box.open()
            self.update_task_list()

    def update_task_list(self):
        

        task_list_screen = self.manager.get_screen('List')
        # task_list_screen.clear_widgets()
        task_button_height = 50

        # Set the initial position of the first task button
        task_button_y = 0.7
        # print(task_button_y)

        for i in range(len(self.tasks)):

            task_button = Button(text=self.tasks[i]['text'], size_hint=(0.8, None), height=task_button_height,
                                pos_hint={'center_x': 0.5, 'y': task_button_y})
            lon = self.tasks[i]['locations'][0]['lon']
            lat = self.tasks[i]['locations'][0]['lat']
            self.coordinate_set.add((lon,lat))
            task_button.bind(on_press=lambda instance, lon=lon, lat=lat: self.on_task_button_pressed(lon, lat))
            task_list_screen.add_widget(task_button)

            # Increase the y position for the next task button
            task_button_y -= 0.06
        print(self.coordinate_set)
        
    def on_task_button_pressed(self, lon, lat):
        app = App.get_running_app()
        map_screen = self.manager.get_screen('Map')
        map_screen.set_location(lat, lon)
        self.manager.current = 'Map'
    

    
    




 

    



class MapTask(Screen):
    
    def __init__(self, **kwargs):
        super(MapTask, self).__init__(**kwargs)
        self.mapview = MapView(zoom=18)
        self.add_widget(self.mapview)

    def set_location(self, lat, lon):
        self.mapview.center_on(lat, lon)
        marker = MapMarker(lat=lat, lon=lon)
        self.mapview.add_marker(marker)


class TaskList(Screen):
    def exit_app(self):
        App.get_running_app().stop()
    
    def change_screen(self, screen_name):
        screen_manager = self.manager
        screen_manager.transition = SlideTransition(direction='right')
        screen_manager.current = screen_name
    
    def __init__(self, **kwargs):
        super(TaskList, self).__init__(**kwargs)

        # create a relative layout for your layout
        self.layout = RelativeLayout()

        # create a label for your task list
        self.task_list_label = Label(text='Task List', size_hint=(1, 0.1), pos_hint={'top': 1})
        self.layout.add_widget(self.task_list_label)

        # create a scroll view for your task list
        self.task_list_scroll_view = ScrollView(size_hint=(1, 0.8), pos_hint={'top': 0.9})
        self.task_list_layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
        self.task_list_layout.bind(minimum_height=self.task_list_layout.setter('height'))
        self.task_list_scroll_view.add_widget(self.task_list_layout)
        self.layout.add_widget(self.task_list_scroll_view)

        # create back and exit buttons
        self.back_button = Button(text='Back', size_hint=(0.4, 0.07), pos_hint={'center_x': 0.25, 'y': 0})
        self.back_button.bind(on_press=lambda x: self.change_screen('First'))
        self.layout.add_widget(self.back_button)

        self.exit_button = Button(text='Exit', size_hint=(0.4, 0.07), pos_hint={'center_x': 0.75, 'y': 0})
        self.exit_button.bind(on_press=lambda x: self.exit_app())
        self.layout.add_widget(self.exit_button)

        # set the relative layout as the root widget for the screen
        self.add_widget(self.layout)





class Manager(ScreenManager):
    pass

    
class FinalApp(App):
    
    tasks = []
    
    def build(self):
        self.selected_locations = []

FinalApp().run()