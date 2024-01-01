import kivy
kivy.require("2.2.1")
from kivy.app import App
from kivy.uix.label import Label

class MyApp (App):
    def build(self):
        # markup text with different colour
        l2 = Label(
            text = "[color=#ff3333][b]'Label'[/b] is Added [/color]\n[color=#3333ff]Screen !!:):):):)[/color]",
			font_size ='20sp', 
            markup = True)
        return l2
        lb = Label(
            text="This is Lable and its multi\nLine",
            font_size="20sp",
            color = "red"
        )
        return lb
    
    
label = MyApp()
label.run()

"""
[b][/b] -> Activate bold text
[i][/i] -> Activate italic text
[u][/u] -> Underlined text
[s][/s] -> Strikethrough text
[font=][/font] -> Change the font
[size=][/size]] -> Change the font size
[color=#][/color] -> Change the text color
[ref=][/ref] -> Add an interactive zone. The reference + bounding box inside the reference will be available in Label.refs
[anchor=] -> Put an anchor in the text. You can get the position of your anchor within the text with Label.anchors
[sub][/sub] -> Display the text at a subscript position relative to the text before it.
[sup][/sup] -> Display the text at a superscript position relative to the text before it.
"""
