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
from kivy.graphics import Color, Rectangle, Canvas

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from Gauge import Gauge
from dictionary import *

class ManualScreen(Screen):
    
    def __init__(self, app,**kwargs):
        super(ManualScreen, self).__init__(**kwargs)
        layout = FloatLayout()#FloatLayout(orientation='vertical', padding=20, spacing=5)
        self.add_widget(layout)
        self.app = app

        with self.canvas.before:
            Color(0.9, 0.9, 0.9, 1) 
            self.rect = Rectangle(size=(75,50), pos=(800-75,0),rgb=(1,1,1),source='Datas/irisib.png')
        
        box_Gauges = GridLayout(rows=3,cols=2,col_default_width=150, col_force_default=True,row_default_height=150, row_force_default=True, pos = (10,-20))
        gaugesize = 150
        fontSize = 20
        self.gaugeU_Motor = Gauge(value=0, size_gauge=gaugesize, size_text=fontSize,text_desc="U Motor",size_desc=15)
        self.gaugeI_Motor = Gauge(value=0, size_gauge=gaugesize, size_text=fontSize,text_desc="I Motor",size_desc=15)
        self.gaugeU_Brake = Gauge(value=0, size_gauge=gaugesize, size_text=fontSize,text_desc="U Brake",size_desc=15)
        self.gaugeI_brake = Gauge(value=0, size_gauge=gaugesize, size_text=fontSize,text_desc="I Brake",size_desc=15)
        self.gauge_Speed  = Gauge(value=0, size_gauge=gaugesize, size_text=fontSize,text_desc="Speed",size_desc=15)
        self.gauge_Couple = Gauge(value=0, size_gauge=gaugesize, size_text=fontSize,text_desc="Couple",size_desc=15)
        
        box_Gauges.add_widget(self.gaugeU_Motor)
        box_Gauges.add_widget(self.gaugeI_Motor)
        box_Gauges.add_widget(self.gaugeU_Brake)
        box_Gauges.add_widget(self.gaugeI_brake)
        box_Gauges.add_widget(self.gauge_Speed)
        box_Gauges.add_widget(self.gauge_Couple)
        
        settings_layout = GridLayout(rows=3,cols=2,
                                     col_default_width=150, col_force_default=True,
                                     row_default_height=30, row_force_default=True, 
                                     pos = (400,-20),spacing = [5,10])

        self.btnSetSpeed =Button(text="Set Speed", on_release = self.btnSetting_Release)#"TC_Set_Speed")
        self.btnSetSpeed.id = "TC_Set_Speed"
        self.btnSetUmotor=Button(text="Set Umotor", on_release = self.btnSetting_Release)
        self.btnSetUmotor.id = "TC_Set_Umotor"
        self.btnSetCouple=Button(text="Set Couple", on_release = self.btnSetting_Release)
        self.btnSetCouple.id = "TC_Set_Couple"
        self.txtbxSetSpeed  = TextInput(text='0', input_filter='float')
        self.txtbxSetUmotor = TextInput(text='0', input_filter='float')
        self.txtbxSetCouple = TextInput(text='0', input_filter='float')
        
        
        settings_layout.add_widget(self.txtbxSetSpeed)
        settings_layout.add_widget(self.btnSetSpeed)
        settings_layout.add_widget(self.txtbxSetUmotor)
        settings_layout.add_widget(self.btnSetUmotor)
        settings_layout.add_widget(self.txtbxSetCouple)
        settings_layout.add_widget(self.btnSetCouple)

        

        layout.add_widget(settings_layout)
        layout.add_widget(box_Gauges)

    def btnSetting_Release(self, instance):
        print(TC_dict[instance.id])



    

    def update(self, dt):
        i = self.app.labtooTestBench.TMTC_COM.testNumber
        if(i<100):
            self.gaugeU_Motor.value = (i/1.5)
            self.gaugeU_Brake.value = (i/2)
            self.gauge_Speed.value = i
            self.gaugeI_Motor.value = (100-i)/2
            self.gaugeI_brake.value = (100-1.5*i)
            self.gauge_Couple.value = (75-i)
        else:
            self.i=0
            