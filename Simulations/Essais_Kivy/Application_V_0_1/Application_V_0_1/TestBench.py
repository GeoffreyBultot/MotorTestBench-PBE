#:kivy 1.0.6

__all__ = ('TestBench',)
__title__ = 'Application_V_0_1'
__version__ = '0.1'
__author__ = 'Bultot Geoffrey'
import kivy
kivy.require('1.0.6') # replace with your current kivy version !
from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen, ScreenManager, FadeTransition
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.gesture import GestureDatabase
from kivy.uix.boxlayout import BoxLayout
from kivy.gesture import Gesture 
from kivy.uix.widget import Widget
import Gauge
from Automatic import AutomaticScreen
from Manuel import ManualScreen
from Settings import SettingsScreen
import random
from threading import Thread, RLock
from kivy.base import runTouchApp
from kivy.factory import Factory as F
from kivy.core.window import Window
from kivy.base import runTouchApp
from kivy.lang import Builder
from dictionary import *
from LabtoolLayer import *
from kivy.config import Config
Config.set('graphics', 'resizable', False)
Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '480')
class ScreenManager(ScreenManager):
    pass

class TestBenchWindow(BoxLayout):
    pass

class HomeScreen(Screen):
    def __init__(self, app, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)
        self.app = app
    def update(self, dt):
        pass

class TestBenchApp(App):
    tm = 1000
    labtooTestBench = LabtoolLayer()
    title = 'TestBench ISIB'
    def build(self):
        
        
        Config.write()
        self.root = Builder.load_file('TestBench.kv')
        sm = self.root.ids.sm
        sm.add_widget(HomeScreen(self,name='HomeScreen'))
        sm.add_widget(AutomaticScreen(self,name='AutomaticScreen'))
        sm.add_widget(ManualScreen(self,name='ManualScreen'))
        sm.add_widget(SettingsScreen(self,name='SettingsScreen'))
        Clock.schedule_interval(sm.current_screen.update, 1.0/60.0)
        pass#return TestBenchWindow()

    def changeScreen(self,idx_Screen):
        sm = self.root.ids.sm
        Clock.unschedule(sm.current_screen.update)
        sm.current = Screens_dict[idx_Screen]

        Clock.schedule_interval(sm.current_screen.update, 1.0/60.0)

    def quit(self):
        self.labtooTestBench.TMTC_COM.ReadBus_Threat_ON = False
        self.labtooTestBench.TMTC_COM.ReadThread.join()
        self.get_running_app().stop()
        pass
#create Screen Manager
#sm = ScreenManager(transition=FadeTransition())
#sm.add_widget(AutomaticScreen(name='AutomaticScreen'))
#sm.add_widget(ManualScreen(name='ManualScreen'))
#sm.current = 'AutomaticScreen'

if __name__ == '__main__':
    TestBenchApp().run()
