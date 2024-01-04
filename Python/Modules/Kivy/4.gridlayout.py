import kivy
kivy.require("2.2.1")
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

class GridLayoutApp(App):
    def build(self):
        layout = GridLayout(
            cols=3, 
            row_force_default=True,
            row_default_height=100,
            col_force_default=True,
            col_default_width=200,
            spacing=(50, 50))

        for i in range(1, 7):
            button = Button(text=f'Button {i}')
            layout.add_widget(button)
        return layout

if __name__ == '__main__':
    GridLayoutApp().run()
