from customtkinter import *
from .window import center_screen
from tkcalendar import Calendar
from datetime import date, datetime

class CalendarToplevelWindow(CTkToplevel):
    def __init__(self, master):
        super().__init__(master)
        center_screen(self, height=200, width=300)
        self.resizable(False, False)
        self.title('Calendar')
        def on_date_select(date):
            selected_date = self.cal.get_date()
            selected_date_format = datetime.strptime(selected_date, "%m/%d/%y")
            selected_date_format= selected_date_format.strftime("%d/%m/%Y")
            # print(selected_date)
            master.dob_entry_label.configure(text=f' {selected_date_format}', text_color=('#333333', '#FFFFFF'))
            master.register_data['dob'] = selected_date
            self.destroy()
            
        calendar_frame = CTkFrame(self, height=600, width=300)
        calendar_frame.pack(fill="both", expand=True, padx=10, pady=10)
        self.cal = Calendar(
            calendar_frame,
            selectmode='day',
            locale='en_US',
            disabledforeground='red',   
            cursor="hand2",
            pattern='mm/dd/yyyy',
            mindate=date(1920, 12, 1),
            maxdate=date.today(),
            background=ThemeManager.theme["CTkFrame"]["fg_color"][1],
            selectbackground=ThemeManager.theme["CTkButton"]["fg_color"][1]
        )
        self.cal.selection_set(date(2005, 3, 1))
        self.cal.bind("<<CalendarSelected>>", on_date_select)
        self.cal.pack(fill="both", expand=False)
