import kivy
from kivy.app import App
from kivy.uix.label import Label

class TouchEventsApp(App):
    def build(self):
        # Create a Label widget
        label = Label(text='Touch Me!',
                      font_size='50sp',
                      color=(0, 0, 1, 1))  # Blue color initially

        # Bind touch events to methods
        label.bind(on_touch_down=self.on_touch_down,
                   on_touch_up=self.on_touch_up)

        return label

    def on_touch_down(self, instance, touch):
        # Change label color when touched
        instance.color = (1, 0, 0, 1)  # Red color

    def on_touch_up(self, instance, touch):
        # Change label color back when touch released
        instance.color = (0, 0, 1, 1)  # Blue color

if __name__ == '__main__':
    TouchEventsApp().run()
