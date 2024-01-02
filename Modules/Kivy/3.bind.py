import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

class KeyboardEventsApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.label = Label(text='Press a key!')
        Window.bind(on_key_down=self.on_key_down)
        layout.add_widget(self.label)
        return layout
    def on_key_down(self, instance, keyboard, keycode, text, modifiers):
         self.label.text = f'Key pressed: {text}'
         #print(instance, keyboard, keycode, text, modifiers)

if __name__ == '__main__':
    KeyboardEventsApp().run()
