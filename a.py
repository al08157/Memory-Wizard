from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.label import Label
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.popup import Popup

class Task:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class TaskList:
    def __init__(self):
        self.tasks = []

class HomeScreen(Screen):
    pass

class AddTaskScreen(Screen):
    name_input = ObjectProperty()
    description_input = ObjectProperty()

    def add_task(self):
        name = self.name_input.text
        description = self.description_input.text

        if not name or not description:
            invalid_form_popup = Popup(title='Invalid Form', 
                                       content=Label(text='Please fill out both fields.'), 
                                       size_hint=(0.8, 0.3))
            invalid_form_popup.open()
            return

        task = Task(name=name, description=description)
        app = App.get_running_app()
        app.task_list.tasks.append(task)

        self.name_input.text = ''
        self.description_input.text = ''

class TaskListScreen(Screen):
    task_list_view = ObjectProperty()

    def on_pre_enter(self, *args):
        app = App.get_running_app()
        task_list = app.task_list
        self.task_list_view.clear_widgets()

        if not task_list.tasks:
            empty_list_label = Label(text='No tasks yet.')
            self.task_list_view.add_widget(empty_list_label)
        else:
            for task in task_list.tasks:
                task_label = Label(text=f'{task.name}: {task.description}')
                self.task_list_view.add_widget(task_label)

class TaskListApp(App):
    task_list = TaskList()

    def build(self):
        Builder.load_file('tasklist.kv')
        screen_manager = ScreenManager()
        screen_manager.add_widget(HomeScreen(name='home'))
        screen_manager.add_widget(AddTaskScreen(name='add_task'))
        screen_manager.add_widget(TaskListScreen(name='task_list'))
        return screen_manager

if __name__ == '__main__':
    TaskListApp().run()
