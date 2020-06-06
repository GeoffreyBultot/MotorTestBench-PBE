'''
TabbedPanel
============

Test of the widget TabbedPanel.
'''

import kivy
kivy.require('1.0.6') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.lang import Builder
from kivy.properties import StringProperty
import random


from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.slider import Slider
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle


class TestBenchWindow(TabbedPanel):
    
    MotorVoltage = StringProperty()

    def __init__(self, **kwargs):
        super(TestBenchWindow, self).__init__(**kwargs)
        self.MotorVoltage = str(random.randint(1, 100))
    def change_text(self):
        self.MotorVoltage = str(random.randint(1, 100))


class TestBenchApp(App):
    def build(self):
        return TestBenchWindow()

if __name__ == '__main__':
    TestBenchApp().run()