import kivy
kivy.require("2.2.1") #kivy.__version__
from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):

    def build(self):
        return Label(text="Hello World!")


if __name__ == "__main__":
    MyApp().run()