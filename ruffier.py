from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from instructions import *
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout






class HeartCheck(App):
    def build(self):
        sm = ScreenManager()
        # sm.add_widget(InstrScreen(name='instr'))
        # sm.add_widget(PulseScr1(name='pulse1'))
        # sm.add_widget(CheckSits(name='sits'))
        # sm.add_widget(PulseScr2(name='pulse2'))
        # sm.add_widget(Result(name='result'))

        return sm




app = HeartCheck()
app.run()