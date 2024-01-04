import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

class PropertyBindingApp(App):
    def build(self):
        # Create a BoxLayout
        layout = BoxLayout(orientation='vertical')

        # Create a Label widget
        label = Label(text='Type Something:')

        # Create a TextInput widget
        text_input = TextInput()

        # Bind text_input's text property to label's text property
        text_input.bind(text=label.setter('text'))

        # Add widgets to the layout
        layout.add_widget(label)
        layout.add_widget(text_input)

        return layout

if __name__ == '__main__':
    PropertyBindingApp().run()
