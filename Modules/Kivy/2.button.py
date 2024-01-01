import kivy
kivy.require("2.2.1")
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class WidgetLayoutApp(App):
    def build(self):
        layout = BoxLayout(orientation="vertical")
        label = Label(
            text="Hello Once"
        )
        button = Button(
            text="Click Me"
        )
        layout.add_widget(label)
        layout.add_widget(button)
        return layout
    
if __name__ == "__main__":
    WidgetLayoutApp().run()
