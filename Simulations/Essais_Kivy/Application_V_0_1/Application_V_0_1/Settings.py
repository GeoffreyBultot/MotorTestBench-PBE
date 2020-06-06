
from kivy.app import App
from kivy.config import Config

from kivy.uix.screenmanager import Screen, ScreenManager, FadeTransition
from kivy.uix.filechooser import FileChooser
class SettingsScreen(Screen):
    i = 0
    j = 0
    def __init__(self, app, **kwargs):
        super(SettingsScreen, self).__init__(**kwargs)

        #layout = FloatLayout()
        #self.add_widget(layout)

        self.app = app
        print(app.root.ids)
    def update(self, dt):
        pass