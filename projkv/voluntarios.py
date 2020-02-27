import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label


class FirstLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(FirstLayout, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.add_widget(Button(text='FirstButton'))
        self.add_widget(Label(text='FirsLabel'))


class Test(App):
    def build(self):

        return FirstLayout()


Test().run()
