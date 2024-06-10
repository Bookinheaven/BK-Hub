from customtkinter import *
from typing import Union, Callable
class FloatSpinbox(CTkFrame):
    def __init__(self, *args,
                 width: int = 100,
                 height: int = 32,
                 step_size: Union[int, float] = 1,
                 command: Callable = None,
                 font: Union[str, str, int] =  ('Arial', 'normal', 9),
                 text_color : str = 'black',
                 fg_color : str = 'white',
                 bg_color : str = 'black',
                 button_fg_color : str = 'blue',
                 button_bg_color : str = 'blue',
                 button_hover_color: str = 'gray',
                 corner_radius: int = 3, 
                 border_color: str = 'black', 
                 border_width: int  = 1,
                 set_min_limit : Union[int,float] = 0,
                 set_max_limit : Union[int,float] = 1000,
                 set_default_value: Union[int, float] = 0,
                 **kwargs):
        super().__init__(*args, width=width, height=height, **kwargs)

        # Define the varibale for def access range
        self.step_size = step_size
        self.command = command
        self.set_min_limit = set_min_limit
        self.set_max_limit = set_max_limit
        self.set_default_value = float(set_default_value)

        self.configure(fg_color=fg_color)

        self.grid_columnconfigure((0, 2), weight=0)
        self.grid_columnconfigure(1, weight=1)

        self.subtract_button = CTkButton(self, text="-", width=height-6, height=height-6,command=self.subtract_button_callback, font=font, text_color=text_color, bg_color=button_bg_color, fg_color=button_fg_color, hover_color=button_hover_color,corner_radius=corner_radius, border_color=border_color,border_width=border_width)
        self.subtract_button.grid(row=0, column=0, padx=(3, 0), pady=3)

        self.entry = CTkEntry(self, width=width-(2*height), height=height-6,font=font, text_color=text_color, fg_color=fg_color, bg_color=bg_color,border_color=border_color, border_width= border_width,corner_radius=corner_radius)
        self.entry.grid(row=0, column=1, columnspan=1, padx=3, pady=3, sticky="ew")

        def button_pressed_in(event):
            self.interv = 100
            self.after_id = self.after(800, increase_value)
        def button_pressed_sub(event):
            self.interv = 100
            self.after_id = self.after(800, decrease_value)

        def button_released(event):
            if self.after_id:
                self.after_cancel(self.after_id)

        self.add_button = CTkButton(self, text="+", width=height-6, height=height-6,
                                                  command=self.add_button_callback,font=font, text_color=text_color,bg_color=button_bg_color, fg_color=button_fg_color,hover_color=button_hover_color,corner_radius=corner_radius, border_color=border_color,border_width=border_width)
        self.add_button.grid(row=0, column=2, padx=(0, 3), pady=3)
        self.add_button.bind("<ButtonPress-1>", button_pressed_in)
        self.add_button.bind("<ButtonRelease-1>", button_released)
        self.subtract_button.bind("<ButtonPress-1>", button_pressed_sub)
        self.subtract_button.bind("<ButtonRelease-1>", button_released)

        def increase_value():
            current_value = float(self.entry.get())
            if current_value < self.set_max_limit:
                self.add_button_callback()
            self.after_id = self.after(self.interv, increase_value)
            
        def decrease_value():
            current_value = float(self.entry.get())
            if current_value > self.set_min_limit:
                self.subtract_button_callback()
            self.after_id = self.after(self.interv, decrease_value)

        if self.set_default_value:
            self.entry.insert(0, f"{self.set_default_value}")
        else:
            self.entry.insert(0, "0.0")
    
    def add_button_callback(self):
        if self.command is not None:
            self.command()
        try:
            value = float(self.entry.get()) + self.step_size
            if value <= self.set_max_limit:
                self.entry.delete(0, "end")
                self.entry.insert(0, value)
        except ValueError:
            return

    def subtract_button_callback(self):
        if self.command is not None:
            self.command()
        try:
            value = float(self.entry.get()) - self.step_size
            if value >= self.set_min_limit:
                self.entry.delete(0, "end")
                self.entry.insert(0, value)
        except ValueError:
            return

    def get(self) -> Union[float, None]:
        try:
            return float(self.entry.get())
        except ValueError:
            return None

    def set(self, value: float):
        if value >= self.set_min_limit and value <= self.set_max_limit:
            self.entry.delete(0, "end")
            self.entry.insert(0, str(float(value)))
