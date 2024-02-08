import kivy
kivy.require("2.2.1")
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

class MyTextInputApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')  # Create a vertical box layout

        text_input = TextInput()  # Create a text input widget
        output_label = Label()    # Create a label widget

        layout.add_widget(text_input)  # Add text input widget to the layout
        layout.add_widget(output_label)  # Add label widget to the layout

        # Bind the text property of the text input to the text property of the label
        text_input.bind(text=output_label.setter('text'))

        return layout  # Return the layout as the root widget of the app


if __name__ == "__main__":
    MyTextInputApp().run()