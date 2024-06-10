from datetime import datetime, timedelta, date
from customtkinter import *
from tkcalendar import Calendar
from ..Utilities.DatabaseMethods import *
from ..Utilities.DateBox import DateBox
from PIL import Image
from ..Utilities.GraphManger import bar_graph

# Dark theme & Light theme
BackgroundFgColor = ('#ffffff', '#111b21')
FrameFgColor = ('#f0f2f5','#202c33')
SubFramsFgColor = ('#dfe5e7','#2a3942')
TextColor = ('#333333', '#FFFFFF')
FontName = 'Ariral'
def update_bar_graph(self):
    # Clear the current plot
    if self.graph_bar != None:
        self.ax.clear()
    finval = {}
    if len(self.final_data_grpah) > 0:
        for x in self.final_data_grpah:
            for key, value in x.items():
                finval[key] = value
    else:
        finval = {'No Data': {'currentpoints': 0, 'dailypoints': 0, 'drank': 0, 'drink': 0}}
    Labels = ['Current Points', 'Daily Points', 'Drank', 'Drink']
    self.graph_bar, self.ax = bar_graph(self=self.graph_frame, labels=Labels, rawdata=finval)
    self.graph_bar_tk = self.graph_bar.get_tk_widget()
    self.graph_bar_tk.grid_propagate(False)
    self.graph_bar_tk.grid_rowconfigure(0, weight=1) 
    self.graph_bar_tk.grid_columnconfigure(0, weight=1)
    self.graph_bar_tk.config(height=400, width=400)
    self.graph_bar_tk.config(bg='#202c33')
    
    self.graph_bar_tk.grid(row=1, column=0, padx=5, pady=5, sticky='n')

    

class HistoryPage(CTkFrame):
    def __init__(self, master, app):
        super().__init__(master)
        self.logger = app.logger
        # Data from the login or registerpage.
        self.userdata = app.userdata
        
        # To make sure there are no changes in the data.
        self.userdata = database_extractor(app, userdata=True, username=self.userdata['username'].strip())
        
        # Extracting Userstats From Raw - Organized.
        self.userstats = database_extractor(app, userstats=True, userid=self.userdata['userid'].strip())
    
        # History page main scrollable frame
        self.top_level_scroll_bar =  CTkScrollableFrame(master=self,corner_radius=10,fg_color=BackgroundFgColor)

        # Configure settings for self
        self.grid_configure(sticky='nsew')
        
        # Configure app's color scheme
        app.configure(fg_color=('#d8e2eb', '#202c33'))
        
        # Section: 1 Frame - for title
        self.top_frame = CTkFrame(master=self.top_level_scroll_bar,corner_radius=10,fg_color=FrameFgColor)
        self.title_label = CTkLabel(master=self.top_frame, text="Water Intake History", font=('Arial',44), fg_color='transparent', text_color=TextColor)
        self.title_label.grid(row=0, column=0, padx=20, pady=20)
        
        self.start_date = None
        self.end_date = None
        self.final_data_grpah = None
        self.graph_bar = None
        self.graph_frame = None
        # Option Menu Function
        def option_selector(event=None):
            # History data
            history: dict = self.userstats['waterintakehistory']
            
            self.value = {}
            # Option Selection: 
            self.selected_option = self.mode_selector.get()
           
            # Date Selection str format
            selected_date_str = self.cal.get_date()
            
            # Date Selection datetime.date format
            self.selected_date = datetime.strptime(selected_date_str, '%m/%d/%Y').date()
            
            # Todays Date str format
            today_date_str = date.today().strftime('%m/%d/%Y')
            
            # Date Selection datetime.date format
            self.today_date = datetime.strptime(today_date_str, '%m/%d/%Y').date()
            
            # Custom selector
            def custom(start: datetime, end: datetime):
                # Convert start and end to datetime.date if they are datetime.datetime
                if isinstance(start, datetime):
                    start = start.date()
                if isinstance(end, datetime):
                    end = end.date()
                values = []
                self.final_data_grpah = []
                if start and end:
                    for key, value in history.items():
                        key_date = datetime.strptime(key, '%m/%d/%Y').date()
                        if start <= key_date <= end:
                            print(key, value)
                            values.append({
                                "day": key,
                                "data": value
                            })
                            self.final_data_grpah.append({
                                key: value
                            })
                return values

            # This function is to get a signal from the date box module when an event occures 
            def date_data(date, fromd : str = ''):
                if fromd == 'start':
                    self.start_date = date
                if fromd == 'end':
                    self.end_date = date
                # Swapping 
                if self.start_date and self.end_date:
                    if self.start_date.date() > self.end_date.date():
                        self.start_date, self.end_date = self.end_date, self.start_date
                        self.start_date_button.config_button(text=str(self.end_date.strftime('%d/%m/%Y')))
                        self.end_date_button.config_button(text=str(self.start_date.strftime('%d/%m/%Y')))
                    self.values = custom(start=self.start_date, end=self.end_date)

            self.start_date_button.on_date_select(event=event, command_fun=lambda ddate: date_data(date=ddate, fromd='start'))
            self.end_date_button.on_date_select(event=event, command_fun=lambda ddate: date_data(date=ddate, fromd='end'))

            # For single dates

            def for_single_dates():
                valuex = [] # Default / Pre-Defined
                self.final_data_grpah = []
                for key, value in history.items():
                    if key == selected_date_str:  
                        valuex.append({
                            "day": key,
                            "data": value}) # Adding to the list
                        self.final_data_grpah.append({
                                key: value
                            })
                return valuex
            
            # For X days
            def ForXDays(days: int = 6):
                valuex = [] # Default / Pre-Defined
                self.final_data_grpah = []
                ago_date = self.selected_date - timedelta(days=days)
                self.start_date_label_fake.configure(text=str(self.selected_date.strftime('%d/%m/%Y')))
                self.end_date_label_fake.configure(text=str(ago_date.strftime('%d/%m/%Y'))) 
                
                for key, value in history.items(): # Key and value pair
                    # Key datetime.date format
                    key_date = datetime.strptime(key, '%m/%d/%Y').date()
                    if ago_date <= key_date <= self.selected_date: # Checking whether date is in btw or not
                        valuex.append({
                            "day": key,
                            "data": value}) # Adding to the list
                        self.final_data_grpah.append({
                                key: value
                            })
                # print(valuex)
                valuex = valuex if valuex else {} # Storing it in instance for future access
                # print(valuex)
                return valuex
            
            # if self.mid2_calendar_frame.grid_info():
            #     self.mid2_calendar_frame.grid_forget()

            # Options
            if self.selected_option == 'Single':
                # print('single day')
                self.values = for_single_dates() 
                if self.mid_calendar_frame.grid_info():
                    self.start_date_button.reset_text()
                    self.end_date_button.reset_text()
                    self.mid_calendar_frame.grid_remove()
      
            elif self.selected_option == '7 days ago':
                # print('7 days')
                self.values = ForXDays(days=6) # Including that day so days = 6
                self.ago_date = self.today_date - timedelta(days=6)  # Update ago_date here
                # print(self.today_date.strftime('%d/%m/%Y'))
                # self.end_date_label_fake.update()
                if not self.mid2_calendar_frame.grid_info():
                    self.mid2_calendar_frame.grid(row=0, column=3, padx= 10, pady=10,sticky='e')
                if self.mid_calendar_frame.grid_info():
                    self.start_date_button.reset_text()
                    self.end_date_button.reset_text()
                    self.mid_calendar_frame.grid_remove()
          
            elif self.selected_option == '30 days ago':
                # print('30 days')
                self.values = ForXDays(days=29) # Including that day so days = 29
            
                if not self.mid2_calendar_frame.grid_info():
                    self.mid2_calendar_frame.grid(row=0, column=2, padx= 10, pady=10,sticky='e')
                if self.mid_calendar_frame.grid_info():
                    self.start_date_button.reset_text()
                    self.end_date_button.reset_text()
                    self.mid_calendar_frame.grid_remove()
              
            elif self.selected_option == 'From the start':
                self.values = custom(start=self.userdata['register_time'], end=self.selected_date)
                self.start_date_label_fake.configure(text=str(self.userdata['register_time'].strftime('%d/%m/%Y')))
                self.end_date_label_fake.configure(text=str(self.selected_date.strftime('%d/%m/%Y')))
                if not self.mid2_calendar_frame.grid_info():
                    self.mid2_calendar_frame.grid(row=0, column=2, padx= 10, pady=10,sticky='e')
                if self.mid_calendar_frame.grid_info():
                    self.start_date_button.reset_text()
                    self.end_date_button.reset_text()
                    self.mid_calendar_frame.grid_remove()

            elif self.selected_option == 'Custom':
                if not self.mid_calendar_frame.grid_info():
                    self.mid_calendar_frame.grid(row=0, column=2, padx= 10, pady=10,sticky='e')
                if self.mid2_calendar_frame.grid_info():
                    self.mid2_calendar_frame.grid_forget()
            # Updates the widgets
            update_widgets(self=self, page='history')
            if self.graph_frame != None:
                update_bar_graph(self)

        # Section 2 : Frame - for calendar    
        self.first_main_calendar_frame = CTkFrame(master=self.top_level_scroll_bar,corner_radius=10,fg_color=FrameFgColor)
        
        self.second_main_calendar_frame = CTkFrame(master=self.top_level_scroll_bar,corner_radius=10,fg_color=FrameFgColor)
        mode = get_appearance_mode()

        dark_options = {
            'background': '#111B21',
            'foreground': '#FFFFFF',
            'disabledbackground': '#2A3942',
            'disabledforeground': '#CCCCCC',
            'bordercolor': '#808080',
            'headersbackground': '#202C33',
            'headersforeground': '#FFFFFF',
            'selectbackground': '#225588',
            'selectforeground': '#FFFFFF',
            'disabledselectbackground': '#3E3E3E',
            'disabledselectforeground': '#808080',
            'normalbackground': '#2A3942',
            'normalforeground': '#FFFFFF',
            'weekendbackground': '#2A3942',
            'othermonthforeground': '#999999',
            'othermonthbackground': '#1E1E1E',
            'othermonthweforeground': '#999999',
            'othermonthwebackground': '#1E1E1E',
            'disableddaybackground': '#3E3E3E',
            'disableddayforeground': '#808080',
        }

        light_options = {
            'background': '#F0F0F0',
            'foreground': '#333333',
            'disabledbackground': '#D0D0D0',
            'disabledforeground': '#777777',
            'bordercolor': '#BBBBBB',
            'headersbackground': '#CCCCCC',
            'headersforeground': '#333333',
            'selectbackground': '#1E90FF',
            'selectforeground': '#FFFFFF',
            'disabledselectbackground': '#CCCCCC',
            'disabledselectforeground': '#777777',
            'normalbackground': '#F0F0F0',
            'normalforeground': '#333333',
            'weekendbackground': '#F0F0F0',
            'othermonthforeground': '#666666',
            'othermonthbackground': '#F0F0F0',
            'othermonthweforeground': '#666666',
            'othermonthwebackground': '#F0F0F0',
            'disableddaybackground': '#D0D0D0',
            'disableddayforeground': '#777777',
        }

        options = dark_options if mode == 'Dark' else light_options

        # Calendar widget
        self.cal = Calendar(
            master=self.second_main_calendar_frame,
            selectmode='day',
            locale='en_US',
            cursor="hand2",
            font=('Arial', 20),
            date_pattern='mm/dd/yyyy',
            **options
        )
        
        # Binding for function
        self.cal.bind("<<CalendarSelected>>", option_selector)
        
        # Modes Label and frame with option menu
        self.top_calendar_frame = CTkFrame(master=self.first_main_calendar_frame,corner_radius=10,fg_color=('#FFFFFF','#333333'))
        self.modes_label = CTkLabel(master=self.top_calendar_frame, text="Modes", font=('Arial',24), fg_color='transparent', text_color=TextColor)
        self.mode_selector = CTkOptionMenu(master=self.top_calendar_frame, font=('Arial', 22), dynamic_resizing=False,values=["Single", "7 days ago", "30 days ago", "From the start", "Custom"], text_color=TextColor, corner_radius=0,button_color=('#F2F2F2','gray'),button_hover_color=('#D6D6D6','#B5B5B5'), dropdown_fg_color='#737373',dropdown_hover_color='#D6D6D6', fg_color=("#F2F2F2",'#555555'), dropdown_font=('x', 20),dropdown_text_color=('#333333', '#FFFFFF'), command=option_selector, width=170)
        self.mode_selector.set("Single")

        # Start and End date 
        cal_imag = CTkImage(dark_image=Image.open(app.calendar_light_image),light_image=Image.open(app.calendar_dark_image), size=(40,40))
        self.mid_calendar_frame = CTkFrame(master=self.first_main_calendar_frame,corner_radius=10, fg_color=FrameFgColor)
        self.cal_img_label = CTkLabel(master=self.mid_calendar_frame, text="",fg_color='transparent', image=cal_imag)
        self.start_date_label = CTkLabel(master=self.mid_calendar_frame, text="Start :", font=('Arial',24), fg_color='transparent', text_color=TextColor)
        
        self.mid2_calendar_frame = CTkFrame(master=self.first_main_calendar_frame,corner_radius=10, fg_color=FrameFgColor)
        self.start2_date_label = CTkLabel(master=self.mid2_calendar_frame, text="Start :", font=('Arial',24), fg_color='transparent', text_color=TextColor)
        self.end2_date_label = CTkLabel(master=self.mid2_calendar_frame, text="End :", font=('Arial',24), fg_color='transparent', text_color=TextColor)
        self.cal2_img_label = CTkLabel(master=self.mid2_calendar_frame, text="",fg_color='transparent', image=cal_imag)
        self.start_date_label_fake = CTkLabel(master=self.mid2_calendar_frame, text=" ", font=('Arial',24), fg_color='transparent', text_color=TextColor)
        self.end_date_label_fake = CTkLabel(master=self.mid2_calendar_frame, text=" ", font=('Arial',24), fg_color='transparent', text_color=TextColor)
        self.start_date_label_fake.grid(row=0, column=2, padx= 5, pady=5,sticky='w')
        self.end_date_label_fake.grid(row=0, column=4, padx= 5, pady=5,sticky='w')
        self.cal2_img_label.grid(row=0, column=0, padx= 10, pady=10,sticky='nw')
                
        
        self.start_date_button_frame = CTkFrame(master=self.mid_calendar_frame,corner_radius=10, fg_color=FrameFgColor)
        self.start_date_button = DateBox(master=self.start_date_button_frame, date_in_pattern='%m/%d/%Y', font=('Arial', 22), fg_color='#446688', text_color=TextColor,ipadx=5,ipady=5, border_color='#88AABB', width=50, height=30, corner_radius=10, hover_color='#88AABB')
        self.start_date_button_frame.grid(row=0, column=2, padx= 5, pady=5,sticky='w')
        
        self.end_date_label = CTkLabel(master=self.mid_calendar_frame, text="End :", font=('Arial',24), fg_color='transparent', text_color=TextColor)
        self.end_date_button_frame = CTkFrame(master=self.mid_calendar_frame,corner_radius=10, fg_color=FrameFgColor)
        self.end_date_button = DateBox(master=self.end_date_button_frame,  date_in_pattern='%m/%d/%Y', font=('Arial', 22), fg_color='#446688', text_color=TextColor,ipadx=5,ipady=5, border_color='#88AABB', width=50, height=30, corner_radius=10, hover_color='#88AABB')
        self.end_date_button_frame.grid(row=0, column=4, padx= 5, pady=5,sticky='w')

        # Grid for Start and End date labels
        self.cal_img_label.grid(row=0, column=0, padx= 10, pady=10,sticky='nw')
        self.start_date_label.grid(row=0, column=1, padx= 10, pady=10,sticky='w')
        self.start2_date_label.grid(row=0, column=1, padx= 10, pady=10,sticky='w')
        self.end2_date_label.grid(row=0, column=3, padx= 10, pady=10,sticky='w')
        self.end_date_label.grid(row=0, column=3, padx= 10, pady=10,sticky='w')

        
        # Grid for option menu
        self.modes_label.grid(row=0, column=0, padx= 10, pady=10,sticky='w')
        
        # Grid for option menu
        self.mode_selector.grid(row=0, column=1, padx= 10, pady=10,sticky='nw')
        
        # Grid for calendar 
        self.cal.grid(row=1, column=0, padx= 10, pady=10,sticky='nsew')
        
        # Section 3 : Near Mid layer - for boxes 
        self.down_widgets_frame = CTkFrame(master=self.top_level_scroll_bar,corner_radius=10,fg_color=FrameFgColor)
    
        # BOX 1 frame and labels : Amount of water need to drink daily
        self.drink_frame = CTkFrame(master=self.down_widgets_frame,corner_radius=10,fg_color=SubFramsFgColor)
        self.drink_frame.grid(row=1, column=0, sticky='nsew', padx=20, pady=20)
        self.drink_frame.rowconfigure([0,1], weight=1)
        self.drink_frame.columnconfigure(0, weight=1)
        self.drink_label = CTkLabel(master=self.drink_frame, text="Drink", text_color=TextColor,bg_color="transparent", font=("Ariral", 20))
        self.drink_label.grid(row=0, column=0,padx=20, pady=(5, 1))
        self.drink_amount_label = CTkLabel(master=self.drink_frame, text='', text_color=TextColor,bg_color="transparent",font=("Ariral", 20))
        self.drink_amount_label.grid(row=1, column=0,padx=20, pady=(1, 5))

        # BOX 2 frame and labels : Amount of water drank
        self.drank_frame = CTkFrame(master=self.down_widgets_frame,corner_radius=10,fg_color=SubFramsFgColor)
        self.drank_frame.grid(row=1, column=1, sticky='nsew', padx=20, pady=20)
        self.drank_frame.rowconfigure([0,1], weight=1)
        self.drank_frame.columnconfigure(1, weight=1)
        self.drank_label = CTkLabel(master=self.drank_frame, text="Drank", text_color=TextColor,bg_color="transparent", font=("Ariral", 20))
        self.drank_label.grid(row=0, column=1,padx=20, pady=(5, 1))
        self.drank_amount_label = CTkLabel(master=self.drank_frame, text='', text_color=TextColor,bg_color="transparent",font=("Ariral", 20))
        self.drank_amount_label.grid(row=1, column=1,padx=20, pady=(1, 5))

        # BOX 3 frame and labels : Points gained
        self.points_gained_frame = CTkFrame(master=self.down_widgets_frame,corner_radius=10,fg_color=SubFramsFgColor)
        self.points_gained_frame.grid(row=1, column=2, sticky='nsew', padx=20, pady=20)
        self.points_gained_frame.rowconfigure([0,1], weight=1)
        self.points_gained_frame.columnconfigure(2, weight=1)
        self.points_gained_label = CTkLabel(master=self.points_gained_frame, text="Points Gained", text_color=TextColor,bg_color="transparent", font=("Ariral", 20))
        self.points_gained_label.grid(row=0, column=2,padx=20, pady=(5, 1))
        self.points_gained_amount_label = CTkLabel(master=self.points_gained_frame, text='', text_color=TextColor,bg_color="transparent",font=("Ariral", 20))
        self.points_gained_amount_label.grid(row=1, column=2,padx=20, pady=(1, 5))
       
        # BOX 4 frame and labels: for points lost 
        self.points_lost_frame = CTkFrame(master=self.down_widgets_frame,corner_radius=10,fg_color=SubFramsFgColor)
        self.points_lost_frame.grid(row=1, column=3, sticky='nsew', padx=20, pady=20)
        self.points_lost_frame.rowconfigure([0,1], weight=1)
        self.points_lost_frame.columnconfigure(2, weight=1)
        self.points_lost_label = CTkLabel(master=self.points_lost_frame, text="Points Lost", text_color=TextColor,bg_color="transparent", font=("Ariral", 20))
        self.points_lost_label.grid(row=0, column=2,padx=20, pady=(5, 1))
        self.points_lost_amount_label = CTkLabel(master=self.points_lost_frame, text='', text_color=TextColor,bg_color="transparent",font=("Ariral", 20))
        self.points_lost_amount_label.grid(row=1, column=2,padx=20, pady=(1, 5))
       
        # Mid Frame grid
        self.down_widgets_frame.rowconfigure([0,1], weight=1)
        self.down_widgets_frame.columnconfigure([0,1,2,3], weight=1)
        self.down_widgets_frame.grid(row=3, column=0, padx=10, pady=10, sticky='nsew')
        
        # Top Frame grid
        self.top_frame.columnconfigure(0,weight=1)
        self.top_frame.rowconfigure(0,weight=1)
        self.top_frame.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')
        
        # Sets the defualt data as today's data
        option_selector(event=None)
        
        # For Grpahs
        
        self.graph_frame = CTkFrame(master=self.top_level_scroll_bar,corner_radius=10,fg_color=SubFramsFgColor)
        self.points_gained_label = CTkLabel(master=self.graph_frame, text="Graph", text_color=TextColor,bg_color="transparent", font=("Ariral", 20))
        self.points_gained_label.grid(row=0, column=0,padx=10, pady=10, sticky='n')
        update_bar_graph(self)
        
        self.graph_frame.columnconfigure(0,weight=1)
        self.graph_frame.rowconfigure(0,weight=1)
        self.graph_frame.grid(row=4, column=0, padx= 10, pady=10, sticky='nsew')
        
        # Calander frame grid
        self.first_main_calendar_frame.columnconfigure(0,weight=1)
        self.first_main_calendar_frame.rowconfigure(0,weight=1)
        self.first_main_calendar_frame.grid(row=1, column=0, padx= 10, pady=10, sticky='nsew')
        
        self.second_main_calendar_frame.columnconfigure(0,weight=1)
        self.second_main_calendar_frame.rowconfigure(0,weight=1)
        self.second_main_calendar_frame.grid(row=2, column=0, padx= 10, pady=10, sticky='nsew')
        
        self.top_calendar_frame.rowconfigure(0,weight=1)
        self.top_calendar_frame.columnconfigure(0,weight=1)
        self.top_calendar_frame.grid(row=0, column=0, padx= 10, pady=10, sticky='nw')
        
        # Main scrollable frame grid
        self.top_level_scroll_bar.grid_columnconfigure(0,weight=1)
        self.top_level_scroll_bar.grid(row=0, column=0, sticky='nsew', padx=2, pady=2)
