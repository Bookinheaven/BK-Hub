import kivy
from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout

class ImageDisplayApp(App):
    def build(self):
        # Create a BoxLayout
        layout = BoxLayout(orientation='vertical')

        # Create an Image widget
        image = Image(source='/home/burn/Documents/GitHub/FIle--_-/My_Work/Python/Mini-Projects/logo_1071x1080.png')  # Replace 'example.png' with your image filename

        # Add the image widget to the layout
        layout.add_widget(image)

        return layout

if __name__ == '__main__':
    ImageDisplayApp().run()
