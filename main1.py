from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty


class Task(Screen):
    task_input = ObjectProperty(None)

    def add_task(self):
        task_text = self.task_input.text
        if task_text:
            self.manager.get_screen('tasks').add_task(task_text)
            self.task_input.text = ''


class Tasks(Screen):
    task_list = ObjectProperty(None)

    def add_task(self, task_text):
        task_item = TaskItem(text=task_text)
        self.task_list.add_widget(task_item)


class TaskItem(Screen):
    text = ObjectProperty(None)


class MainScreen(Screen):
    pass


class Manager(ScreenManager):
    pass


class ToDoListApp(App):
    def build(self):
        pass

ToDoListApp().run()
