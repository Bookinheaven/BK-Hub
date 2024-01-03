import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Line

class CanvasDrawing(Widget):
    def on_touch_down(self, touch):
        with self.canvas:
            touch.ud['line'] = Line(points=(touch.x, touch.y))

    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]

class CanvasDrawingApp(App):
    def build(self):
        return CanvasDrawing()

if __name__ == '__main__':
    CanvasDrawingApp().run()
