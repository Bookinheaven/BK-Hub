from customtkinter import *
from typing import Union, Tuple, Optional, Any
from tkcalendar import Calendar
from datetime import date as d, datetime

class DateBox(CTkFrame):
    def configure_info(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
            print(key, value)

    def __init__(self, 
                 master: Any, 
                 width: int = 140, 
                 height: int = 28, 
                 corner_radius: Optional[Union[int, str]] = 0, 
                 border_width: Optional[Union[int, str]] = 0, 
                 border_spacing: Optional[Union[int, str]] = 0, 
                 text_color: str = 'black',
                 date: str = 'Date Selector',
                 date_in_pattern: str = '%m/%d/%y',
                 date_out_pattern: str = '%d/%m/%Y',
                 font: Union[str, Tuple[str, int]] = ('Arial', 9),
                 bg_color: Union[str, Tuple[str, str]] = "transparent", 
                 fg_color: Union[str, Tuple[str, str]] = "blue", 
                 hover_color: Union[str, Tuple[str, str]] = None,
                 ipadx: Union[int, Tuple[int, int]] = 2,
                 ipady: Union[int, Tuple[int, int]] = 2,
                 border_color: Union[str, Tuple[str, str], None] = None, 
                 background_corner_colors: Optional[Tuple[Union[str, Tuple[str, str]]]] = None,
                 text_color_disabled: str | Tuple[str, str] | None = None,
                 round_width_to_even_numbers: bool = True,
                 round_height_to_even_numbers: bool = True,
                 textvariable: Variable | None = None,
                 image: CTkImage | Any | None = None,
                 state: str = "normal",
                 hover: bool = True,
                 compound: str = "left",
                 anchor: str = "center",
                 **kwargs: Any):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, **kwargs)

        # Store attributes
        self.date = date
        self.olddate = date
        self.text_color = text_color
        self.font = font
        self.bg_color = bg_color
        self.fg_color = fg_color
        self.select = False
        self.date_out_pattern = date_out_pattern
        self.date_in_pattern = date_in_pattern

        # Configure widgets
        self.box = CTkButton(
            master=master, 
            text=str(self.date), 
            fg_color=self.fg_color, 
            hover_color=hover_color, 
            command=self.pressedbutton,
            font=self.font,
            border_width=border_width,  
            border_color=border_color,
            border_spacing=border_spacing,
            corner_radius=corner_radius,
            width=width,
            height=height,
            text_color=text_color,
            text_color_disabled= text_color_disabled,
            round_width_to_even_numbers=round_width_to_even_numbers,
            round_height_to_even_numbers=round_height_to_even_numbers,
            textvariable=textvariable,
            image=image,
            state = state,
            hover = hover,
            compound= compound,
            anchor=anchor,
        )
        self.box.grid(row=0, column=0, ipadx=ipadx, ipady=ipady)
        self.date_label = self.box 

    def pressedbutton(self):
        if not self.select:
            self.select = True
            self.box.configure(state="disabled")
        else:
            self.select = False

    def on_date_select(self, event, command_fun):
        if self.select:
            self.date = event.widget.get_date()
            if not self.date == 'Date Selector':
                self.date = datetime.strptime(self.date, self.date_in_pattern)
            self.box.configure(text=str(self.date.strftime(self.date_out_pattern)))
            self.select = False
            self.box.configure(state="normal")
            if command_fun:
                command_fun(self.date)
    def config_button(self, *args, **kwargs):
        return self.box.configure(*args, **kwargs)
    
    def get_date(self):
        return self.date
    def get_button(self):
        return self.box
    def forget_grid(self):
        self.box.grid_forget()
    def reset_text(self):  
        self.box.configure(text=self.olddate)

# if __name__ == '__main__':
#     Window = CTk()
#     frame1 = CTkFrame(Window)
#     frame1.grid(row=0, column=0, sticky='nsew', padx=20,pady=20)
#     date_box1 = DateBox(master=frame1, fg_color='green', pop_hovercolor='red', border_color='green', border_width=3, date_out_pattern='%d-%m-%Y')
    
#     cal = Calendar(
#             frame1,
#             selectmode='day',
#             locale='en_US',
#             disabledforeground='red',   
#             cursor="hand2",
#             pattern='mm/dd/yyyy',
#             mindate=d(1920, 12, 1),
#             maxdate=d.today(),
#             background=ThemeManager.theme["CTkFrame"]["fg_color"][1],
#             selectbackground=ThemeManager.theme["CTkButton"]["fg_color"][1]
#         )
#     cal.selection_set(d(2005, 3, 1))
#     cal.grid(row=1,column=0,padx=10, pady=10)
    
#     # Bind the calendar's event to the DateBox's method
#     cal.bind("<<CalendarSelected>>", date_box1.on_date_select)
    
#     Window.mainloop()


