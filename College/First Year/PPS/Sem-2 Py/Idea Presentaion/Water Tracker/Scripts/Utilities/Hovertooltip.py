from customtkinter import CTkToplevel
from tkinter import Label

class Hovertooltip:
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tooltip = None
        self.widget.bind("<Enter>", self.display_tooltip)
        self.widget.bind("<Leave>", self.hide_tooltip)

    def display_tooltip(self, event):
        if self.tooltip is None or not self.tooltip.winfo_exists():
            x, y, _, _ = self.widget.bbox("insert")
            x += self.widget.winfo_rootx() + 5
            y += self.widget.winfo_rooty() + 35
            self.tooltip = CTkToplevel()
            self.tooltip.wm_overrideredirect(True)
            self.tooltip.wm_geometry(f"+{x}+{y}")
            label = Label(self.tooltip, text=self.text, background="white", relief='solid', borderwidth=1)
            label.grid(ipadx=5, ipady=2, sticky='nsew')
        else:
            self.tooltip.deiconify()

    def hide_tooltip(self, event=None):
        if self.tooltip is not None and self.tooltip.winfo_exists():
            self.tooltip.withdraw()
