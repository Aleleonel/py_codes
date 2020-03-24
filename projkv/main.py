from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class Gerar(BoxLayout):
    pass


class Privilegio(App):
    def build(self):
        return Gerar()


Privilegio().run()