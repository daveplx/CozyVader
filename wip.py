import kivy

kivy.require('1.10.0')

from kivy.core.window import Window
Window.fullscreen = 'auto'
#Window.borderless = True
#Window.clearcolor = (1, 1, 1, 0)

from kivy.app import App

from kivy.graphics import Rectangle

from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

class wipApp(App):

    def build(self):
        self.rootLayout = FloatLayout(size=Window.size)

        self.buttonGrid = GridLayout(cols=5, rows=2, size_hint=(.95, .2), pos_hint={'x': .025, 'y': .7}, padding=10, spacing=5)
        self.buttonGrid.add_widget(Button(text='d4'))
        self.buttonGrid.add_widget(Button(text='d6'))
        self.buttonGrid.add_widget(Button(text='d8'))
        self.buttonGrid.add_widget(Button(text='d10'))
        self.buttonGrid.add_widget(Button(text='d12'))
        self.buttonGrid.add_widget(Button(text='d20'))
        self.buttonGrid.add_widget(Button(text='d100'))
        self.buttonGrid.add_widget(Button(text='dN'))
        self.buttonGrid.add_widget(Button(text='Mod:'))
        self.buttonGrid.add_widget(Button(text='+4'))
        self.rootLayout.add_widget(self.buttonGrid)

        self.rollTray = BoxLayout(size_hint=(.95, .2), pos_hint={'x': .025, 'y': .5}, padding=10, spacing=5)
        self.rollTray.add_widget(Button(size_hint=(.9, 1), text='omg so many dice.'))
        self.rollTray.add_widget(Button(size_hint=(.1, 1), text='>'))
        self.rootLayout.add_widget(self.rollTray)

        self.buttonBox = BoxLayout(size_hint=(.95, .1), pos_hint={'x': .025, 'y': .4}, padding=10, spacing=5)
        self.buttonBox.add_widget(Button(text='clear'))
        self.buttonBox.add_widget(Button(text='save'))
        self.buttonBox.add_widget(Button(text='roll'))
        self.rootLayout.add_widget(self.buttonBox)

        self.resultGrid = GridLayout(cols=1, rows=2, size_hint=(.95, .3), pos_hint={'x': .025, 'y': .1}, padding=10, spacing=5)
        self.resultGrid.add_widget(Button(size_hint=(1, .7), pos_hint={'x': 0, 'y': .3}, text='I am dice.'))
        self.resultGrid.add_widget(Button(size_hint=(1, .3), pos_hint={'x': 0, 'y': 0}, text='Total:'))
        self.rootLayout.add_widget(self.resultGrid)

        with self.rootLayout.canvas.before:
            self.rect = Rectangle(pos=self.rootLayout.pos, size=self.rootLayout.size, source=("C:\\Users\\dri.TACTON\\Downloads\\papyrus.jpg"))

        return self.rootLayout

if __name__ == '__main__':
    wipApp().run()