from customtkinter import *
from PIL import Image
from datetime import datetime
from ..Utilities.Hovertooltip import Hovertooltip
from ..Utilities.CalendarToplevelWindow import CalendarToplevelWindow
from ..Utilities.FloatSpinbox import FloatSpinbox
from ..Utilities.Generator import UserIDGenerator
from ..Base import WaterDatabase as WD
from ..Utilities.JsonMethods import *

class RegisterPage(CTkFrame):
    def __init__(self, master, app):
        super().__init__(master)
        self.logger = app.logger
        self.app = app
        self.configure(fg_color='transparent')
        self.grid_configure(sticky='nsew')

        self.register_data = {
            "userid":'',
            "name":'',
            "username":'',
            "password":"",
            "confirm_password": "",
            "dob":"",
            "gender":"",
            "email":"",
            "activity_level":"",
            "weight": "",
            "height" : "",
            "register_time":"",
            'level' :'',
            'experiencepoints' :'',
            'lastlogin' :'',
            'verificationcode' :'',
            'verificationtime': '',
            'verifiedcode' :'',
            'recoveryemail' :'',
            'recoverycode':''
        }
        fields = [
            ("Name",1),
            ("Username", 3),
            ("Password", 5),
            ("Confirm Password", 7),
            ("DOB",9),
            ("Gender", 11),
            ("Email", 13),
            ("Activity Level", 15),
            ("Weight (in Kg)", 17),
            ("Height (in cms)", 19),
            ("Register",21)
        ]
        # Scroll Bar
        self.scroll_frame = CTkScrollableFrame(self, fg_color=('#FFFFFF','#333333'))#, label_text= 'Aqua Sign Up'
        self.center_frame = CTkFrame(self.scroll_frame, fg_color=('#FFFFFF','#333333'))
        self.center_frame.grid(row=0, column=0, padx=20, pady=30)
        def back(event):
            app.show_page("LoginPage")
        
        self.center_frame.columnconfigure((0,1,2), weight=1)
        self.scroll_frame.rowconfigure(0, weight=1)
        self.scroll_frame.columnconfigure(0, weight=1)
        back_image = CTkImage(dark_image=Image.open(app.arrow_left_light),light_image=Image.open(app.arrow_left_dark), size=(40,40))
        self.backtosingup_label = CTkLabel(master=self.center_frame, text= '', text_color=('#333333', '#FFFFFF'), fg_color=('#FFFFFF','#333333'), width=50, height=50,font=('x',25), image=back_image,cursor='hand2')
        self.backtosingup_label.grid(row=0, column=0, padx=10,pady=10,sticky='w')
        self.backtosingup_label.bind("<Button-1>", command=back)

        self.aqua_frame = CTkFrame(self.center_frame, height=40, width=70, fg_color=('#FFFFFF','#333333'))
        self.aqua_frame.grid(row=0, column=0, padx=70, pady=5, sticky='w')  
        self.register_label_1 = CTkLabel(
            master=self.aqua_frame,
            text='Aqua ',
            text_color=('white','white'),
            fg_color=('#1877f2', '#1E90FF'),
            font=('x', 40),
            anchor='center',
            corner_radius=10
        )
        self.register_label_1.grid(row=1, column=0, padx=10, pady=10, sticky='w',ipadx=5,ipady=5)  
        self.register_label_2 = CTkLabel(
            master=self.aqua_frame,
            text='Sign Up',
            text_color=('black','#1E90FF'),
            fg_color=('#FFFFFF','#333333'),
            font=('x', 40),
            anchor='center'
        )
        self.register_label_2.grid(row=1, column=1, padx=0, pady=20, sticky='w')  

        self.name_label = CTkLabel(master=self.center_frame, text=fields[0][0], font=('x', 25), anchor='center',text_color=('#333333', '#FFFFFF'))
        self.name_label.grid(row=fields[0][1], column=0, padx=50, pady=(10,0), sticky='w')
        
        self.name_entry = CTkEntry(master=self.center_frame,width=400, height=40, font=("Bold",23), text_color=('#333333', '#FFFFFF'), placeholder_text=f'{fields[0][0]}',placeholder_text_color=("#999999", "#CCCCCC"), fg_color=("#F2F2F2",'#555555'), corner_radius=3, border_color=('#CCCCCC','#999999'), border_width=1)
        self.name_entry.grid(row=fields[0][1]+1, column=0, padx=50, pady=10, sticky='w')
        Hovertooltip(self.name_entry, "Enter your name in 3-50 characters")
        
        self.username_label = CTkLabel(master=self.center_frame, text=fields[1][0], font=('x', 25), anchor='center',text_color=('#333333', '#FFFFFF'))
        self.username_label.grid(row=fields[1][1], column=0, padx=50, pady=(10,0), sticky='w')

        self.username_entry = CTkEntry(master=self.center_frame,width=400, height=40, font=("Bold",23), text_color=('#333333', '#FFFFFF'), placeholder_text=f'{fields[1][0]}',placeholder_text_color=("#999999", "#CCCCCC"), fg_color=("#F2F2F2",'#555555'), corner_radius=3, border_color=('#CCCCCC','#999999'), border_width=1)
        self.username_entry.grid(row=fields[1][1]+1, column=0, padx=50, pady=10, sticky='w')
        Hovertooltip(self.username_entry, "Enter your username in 5-15 characters")
        
        self.username_progressbar = CTkProgressBar(self.center_frame,width=398,height=7,border_width=0, corner_radius=3, fg_color=("#F2F2F2",'#555555'), progress_color='white', border_color='#F6F4F9')
        self.username_progressbar.grid(row=fields[1][1]+1, column=0, padx=51, pady=(32,0), sticky='w')
        self.username_progressbar.set(0)
        def progress_username(event):
            value = len(self.username_entry.get())
            if value == 1:
                self.username_progressbar.set(0)
                self.username_progressbar.configure(progress_color='red')
            elif value >= 15 or value < 5:
                self.username_progressbar.set(value / 15) 
                self.username_progressbar.configure(progress_color='red')
            elif value >= 8 and value < 10 :
                self.username_progressbar.set(value / 15)
                self.username_progressbar.configure(progress_color='#55FF00')
                
            elif value > 10 and value < 15 :
                self.username_progressbar.set(value / 15)
                self.username_progressbar.configure(progress_color='#FF8E35')

        self.username_entry.bind('<KeyRelease>', command=progress_username)
        self.username_entry.bind('<Control-v>', command=progress_username)
        
        def pass_check(event):
            password = self.password_entry.get()
            confirm_password = self.conform_password_entry.get()
            if len(password) > 0:
                if password != confirm_password:
                    if len(password) <= len(confirm_password):
                        self.conform_password_entry.configure(border_color='#FF664B')
                    
                else:
                    self.conform_password_entry.configure(border_color=('#CCCCCC','#999999'))
        def validate_space(char):
            if char == " ":
                return False
            return True

        self.password_label = CTkLabel(master=self.center_frame, text=fields[2][0], font=('x', 25), anchor='center',text_color=('#333333', '#FFFFFF'))
        self.password_label.grid(row=fields[2][1], column=0, padx=50, pady=(10,0), sticky='w')

        self.password_entry = CTkEntry(master=self.center_frame, width=400, height=40, font=("Bold",23), text_color=('#333333', '#FFFFFF'), placeholder_text=f'{fields[2][0]}',placeholder_text_color=("#999999", "#CCCCCC"), fg_color=("#F2F2F2",'#555555'), corner_radius=3, border_color=('#CCCCCC','#999999'), border_width=1, show='*')
        self.password_entry.grid(row=fields[2][1]+1, column=0, padx=50, pady=10, sticky='w')
        Hovertooltip(self.password_entry, "Enter your password in 8-25 characters")
        
        self.password_level_label = CTkLabel(master=self.center_frame, text="", font=('x', 20), anchor='center',text_color=('#333333', '#FFFFFF'))
        self.password_level_label.grid(row=fields[2][1], column=0, padx=170, pady=(10,0), sticky='w')

        self.password_progressbar = CTkProgressBar(self.center_frame,width=396,height=7,border_width=0, corner_radius=3, fg_color=("#F2F2F2",'#555555'), progress_color='white', border_color='#F6F4F9')
        self.password_progressbar.grid(row=fields[2][1]+1, column=0, padx=51, pady=(32,0), sticky='w')
        self.password_progressbar.set(0)
        
        def progress_password(event):
            pass_check(event)
            check_sym = ['#', '$', '@', '!', '^', '&', '*']
            value = len(self.password_entry.get())
            password = self.password_entry.get()

            if value == 1:
                self.password_progressbar.set(0)
                self.password_progressbar.configure(progress_color='red')
                self.password_level_label.configure(text='')
            elif value >= 30 or value < 8:
                self.password_progressbar.set(value / 30) 
                self.password_progressbar.configure(progress_color='red')
                self.password_level_label.configure(text='')
            elif value >= 8 and value < 10:
                self.password_progressbar.set(value / 30)
                self.password_progressbar.configure(progress_color='#55FF00')
                self.password_level_label.configure(text='(Easy)')

            elif value > 10 and value < 15:
                if any(char in check_sym for char in password):
                    self.password_progressbar.set(value / 30)
                    self.password_progressbar.configure(progress_color='#DAFF35')
                    self.password_level_label.configure(text='(Good)')
                else:
                    self.password_progressbar.set(value / 30)
                    self.password_progressbar.configure(progress_color='#55FF00')
                    self.password_level_label.configure(text='(Easy)')

            elif value >= 15 and value < 20:
                if any(char in check_sym for char in password):
                    self.password_progressbar.set(value / 30)
                    self.password_progressbar.configure(progress_color='#FFBC35')
                    self.password_level_label.configure(text='(Hard)')
                else:
                    self.password_progressbar.set(value / 30)
                    self.password_progressbar.configure(progress_color='#55FF00')
                    self.password_level_label.configure(text='(Easy)')

            elif value >= 20 and value < 30:
                if any(char in check_sym for char in password):
                    self.password_progressbar.set(value / 30)
                    self.password_progressbar.configure(progress_color='#FF8E35')
                    self.password_level_label.configure(text='(Impossible)')
                else:
                    self.password_progressbar.set(value / 30)
                    self.password_progressbar.configure(progress_color='#55FF00')
                    self.password_level_label.configure(text='(Easy)')
            elif value > 30:
                self.password_progressbar.set(value / 30)
                self.password_progressbar.configure(progress_color='red')
                self.password_level_label.configure(text='')

        self.password_entry.bind('<KeyRelease>', command=progress_password)
        self.password_entry.bind('<Control-v>', command=progress_password)
        self.conform_password_label = CTkLabel(master=self.center_frame, text=fields[3][0], font=('x', 25), anchor='center',text_color=('#333333', '#FFFFFF'))
        self.conform_password_label.grid(row=fields[3][1], column=0, padx=50, pady=(10,0), sticky='w')

        self.conform_password_entry = CTkEntry(master=self.center_frame, width=400, height=40, font=("Bold",23), text_color=('#333333', '#FFFFFF'), placeholder_text=f'{fields[3][0]}',placeholder_text_color=("#999999", "#CCCCCC"), fg_color=("#F2F2F2",'#555555'), corner_radius=3, border_color=('#CCCCCC','#999999'), border_width=1, show='*')
        self.conform_password_entry.grid(row=fields[3][1]+1, column=0, padx=50, pady=10, sticky='w')
        self.conform_password_entry.bind("<KeyRelease>", command=pass_check)
        
        self.image_eye_on = CTkImage(dark_image=Image.open(app.eye_on_light),light_image=Image.open(app.eye_on_dark), size=(20,20))
        self.image_eye_off = CTkImage(dark_image=Image.open(app.eye_off_light),light_image=Image.open(app.eye_off_dark), size=(20,20))
        self.eye_pwd_label = CTkLabel(master=self.center_frame, text="", image=self.image_eye_off, cursor='hand2', fg_color=("#F2F2F2",'#555555'))
        self.eye_pwd_label.grid(row=fields[2][1]+1, column=0, padx=60, pady=(6,10), sticky='e')
        self.eye_cnpwd_label = CTkLabel(master=self.center_frame, text="", image=self.image_eye_off, cursor='hand2', fg_color=("#F2F2F2",'#555555'))
        self.eye_cnpwd_label.grid(row=fields[3][1]+1, column=0, padx=60, pady=10, sticky='e')
        
        validation_cmd = self.center_frame.register(validate_space)
        self.username_entry.configure(validate="key", validatecommand=(validation_cmd, '%S'))
        self.password_entry.configure(validate="key", validatecommand=(validation_cmd, '%S'))
        self.conform_password_entry.configure(validate="key", validatecommand=(validation_cmd, '%S'))

        def reveal_password(event):
            self.eye_pwd_label.configure(image=self.image_eye_on)
            self.password_entry.configure(show="")

        def hide_password(event):
            self.eye_pwd_label.configure(image=self.image_eye_off)
            self.password_entry.configure(show="*")

        def reveal_conform_password(event):
            self.eye_cnpwd_label.configure(image=self.image_eye_on)
            self.conform_password_entry.configure(show="")

        def hide_conform_password(event):
            self.eye_cnpwd_label.configure(image=self.image_eye_off)
            self.conform_password_entry.configure(show="*")

        self.password_entry.bind('<KeyRelease>', validate_space)
        self.conform_password_entry.bind('<KeyRelease>', validate_space)

        self.eye_pwd_label.bind("<ButtonPress>", reveal_password)
        self.eye_pwd_label.bind("<ButtonRelease>", hide_password)

        self.eye_cnpwd_label.bind("<ButtonPress>", reveal_conform_password)
        self.eye_cnpwd_label.bind("<ButtonRelease>", hide_conform_password)

        self.dob_label = CTkLabel(master=self.center_frame, text=fields[4][0], font=('x', 25), anchor='center',text_color=('#333333', '#FFFFFF'))
        self.dob_label.grid(row=fields[4][1], column=0, padx=50, pady=(10,0), sticky='w')

        self.dob_entry = CTkEntry(master=self.center_frame, width=370, height=40, font=("Bold",23), text_color=('#333333', '#FFFFFF'), fg_color=("#F2F2F2",'#555555'), corner_radius=3, border_color=('#CCCCCC','#999999'), border_width=1,state='readonly')
        self.dob_entry.grid(row=fields[4][1]+1, column=0, padx=(50,0), pady=10, sticky='w')

        self.dob_entry_label = CTkLabel(master=self.center_frame,width=368, height=38, text=' Select DOB', font=('x', 25), anchor='w', text_color=("#999999", "#CCCCCC"), fg_color=("#F2F2F2",'#555555'))
        self.dob_entry_label.grid(row=fields[4][1]+1, column=0, padx=(51,0), pady=9, sticky='w')
        
        cal_imag = CTkImage(dark_image=Image.open(app.calendar_dark_image),light_image=Image.open(app.calendar_light_image), size=(25,25))
        self.calendar_toplevel_window = None

        def select_dob():
            if self.calendar_toplevel_window is None or not self.calendar_toplevel_window.winfo_exists():
                self.calendar_toplevel_window = CalendarToplevelWindow(self) 
                self.calendar_toplevel_window.grab_set()  
            else:
                self.calendar_toplevel_window.grab_set()

        self.dob_select = CTkButton(master=self.center_frame, text='',image=cal_imag, command= select_dob, hover_color=('#125aa8','#0f5daf'), fg_color='#1877f2', text_color=('#333333', '#FFFFFF'), height=40, width=40, corner_radius=3, border_width=1, border_color=('#CCCCCC','#999999'))
        self.dob_select.grid(row=fields[4][1]+1, column=0, padx=(350,0), pady=10)

        self.gender_label = CTkLabel(master=self.center_frame, text=fields[5][0], font=('x', 25), anchor='center',text_color=('#333333', '#FFFFFF'))
        self.gender_label.grid(row=fields[5][1], column=0, padx=50, pady=(10,0), sticky='w')
    
        def checkbox_event_male():
            if check_male.get() == '1':
                self.gender_checkbox_female.deselect()
            self.register_data['gender'] = 'Male'
        def checkbox_event_female():
            if check_female.get() == '1':
                self.gender_checkbox_male.deselect()
            self.register_data['gender'] = 'Female'

        check_male = StringVar(value="off")
        check_female = StringVar(value="off")
        self.gender_checkbox_male = CTkCheckBox(self.center_frame, text="Male", command=checkbox_event_male,
                                            variable=check_male, font=('x', 25), text_color=('#333333', '#FFFFFF'), hover_color=('#125aa8','#0f5daf'), fg_color='#1877f2', corner_radius=3, border_color=('#CCCCCC','#999999'), border_width=2)
        self.gender_checkbox_male.grid(row=fields[5][1]+1, column=0, padx=50, pady=10, sticky='w')
        self.gender_checkbox_female = CTkCheckBox(self.center_frame, text="Female", command=checkbox_event_female,
                                            variable=check_female, font=('x', 25), text_color=('#333333', '#FFFFFF'), hover_color=('#125aa8','#0f5daf'), fg_color='#1877f2', corner_radius=3, border_color=('#CCCCCC','#999999'), border_width=2)
        self.gender_checkbox_female.grid(row=fields[5][1]+1, column=0, padx=(160,30), pady=10, sticky='w')

        self.email_label = CTkLabel(master=self.center_frame, text=fields[6][0], font=('x', 25), anchor='center',text_color=('#333333', '#FFFFFF'))
        self.email_label.grid(row=fields[6][1], column=0, padx=50, pady=(10,0), sticky='w')

        self.email_entry = CTkEntry(master=self.center_frame, width=400, height=40, font=("Bold",23), text_color=('#333333', '#FFFFFF'), placeholder_text=f'{fields[6][0]}',placeholder_text_color=("#999999", "#CCCCCC"), fg_color=("#F2F2F2",'#555555'), corner_radius=3, border_color=('#CCCCCC','#999999'), border_width=1)
        self.email_entry.grid(row=fields[6][1]+1, column=0, padx=50, pady=10, sticky='w')
        
        self.activity_level_label = CTkLabel(master=self.center_frame, text=fields[7][0], font=('x', 25), anchor='center',text_color=('#333333', '#FFFFFF'))
        self.activity_level_label.grid(row=fields[7][1], column=0, padx=50, pady=(10,0), sticky='w')
        
        self.activity_level_label_bord = CTkEntry(master=self.center_frame, width=402, height=42, font=("Bold",23), text_color=('#333333', '#FFFFFF'), fg_color=("#F2F2F2",'#555555'), corner_radius=3, border_color=('#CCCCCC','#999999'), border_width=1,state='readonly')
        self.activity_level_label_bord.grid(row=fields[7][1]+1, column=0, padx=50, pady=10, sticky='w')
        
        self.activity_level_menu = CTkOptionMenu(self.center_frame, dynamic_resizing=True,
                                                        values=["Low Level", "Medium Level", "High Level"], text_color=('#333333', '#FFFFFF'), corner_radius=0, width=398, height=40,button_color=('#F2F2F2','gray'),button_hover_color=('#D6D6D6','#B5B5B5'), dropdown_fg_color='#737373',dropdown_hover_color='#D6D6D6',font=('x', 22), fg_color=("#F2F2F2",'#555555'), dropdown_font=('x', 20),dropdown_text_color=('#333333', '#FFFFFF'))
        self.activity_level_menu.set("--Select--")
        self.activity_level_menu.grid(row=fields[7][1]+1, column=0, padx=52, pady=10, sticky='w')

        self.weight_label = CTkLabel(master=self.center_frame, text=fields[8][0], font=('x', 25), anchor='center',text_color=('#333333', '#FFFFFF'))
        self.weight_label.grid(row=fields[8][1], column=0, padx=50, pady=(10,0), sticky='w')
        self.weight_entry = FloatSpinbox(master=self.center_frame, width=400, height=40, font=("Bold",23), text_color=('#333333', '#FFFFFF'), fg_color=("#F2F2F2",'#555555'), corner_radius=3, border_color=('#CCCCCC','#999999'), border_width=1, button_bg_color='white', button_fg_color=("#F2F2F2",'#555555'),button_hover_color='gray', set_min_limit=20, set_max_limit=250,set_default_value = 20)
        self.weight_entry.grid(row=fields[8][1]+1, column=0, padx=50, pady=10, sticky='w')
        Hovertooltip(self.weight_entry, "Enter your weight in killograms(kg)")
        self.height_label = CTkLabel(master=self.center_frame, text=fields[9][0], font=('x', 25), anchor='center',text_color=('#333333', '#FFFFFF'))
        self.height_label.grid(row=fields[9][1], column=0, padx=50, pady=(10,0), sticky='w')

        self.height_entry = FloatSpinbox(master=self.center_frame, width=400, height=40, font=("Bold",23), text_color=('#333333', '#FFFFFF'), fg_color=("#F2F2F2",'#555555'), corner_radius=3, border_color=('#CCCCCC','#999999'), border_width=1, button_bg_color='white', button_fg_color=("#F2F2F2",'#555555'),button_hover_color='gray',set_min_limit=90, set_max_limit=213, set_default_value = 90)
        self.height_entry.grid(row=fields[9][1]+1, column=0, padx=50, pady=10, sticky='w')
        Hovertooltip(self.height_entry, "Enter your height in centimeters(cm)")
        self.register_button = CTkButton(
            master=self.center_frame,
            text=f'{fields[10][0]}',
            font=('x', 25),
            text_color='white',
            fg_color='#1877f2',
            command=self.register_user,
            height=50,
            width=250
        )
        self.register_button.grid(row=fields[10][1], column=0, padx=(130,0), pady=20, sticky='w')
        self.scroll_frame.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
    def register_user(self):
        try:
            self.register_button.configure(state='disabled')
            self.register_data['name'] = self.name_entry.get()
            self.register_data['username'] = self.username_entry.get()
            self.register_data['password'] = self.password_entry.get()
            self.register_data['confirm_password'] = self.conform_password_entry.get()
            self.register_data['email'] = self.email_entry.get()
            self.register_data['activity_level'] = self.activity_level_menu.get()
            self.register_data['weight'] = self.weight_entry.get()
            self.register_data['height'] = self.height_entry.get()
            error_messages = []
            if not self.register_data['name']:
                error_messages.append("Please enter your name")

            elif len(self.register_data['name']) < 3 or len(self.register_data['name']) > 50:
                error_messages.append("Name must be between 3 and 50 characters")

            if len(self.register_data['username']) < 5 or len(self.register_data['username']) > 15:
                error_messages.append("Username must be between 5 and 15 characters")

            if len(self.register_data['password']) < 8 or len(self.register_data['password']) > 25:
                error_messages.append("Password must be between 8 and 25 characters")

            if not self.register_data['email']:
                error_messages.append("Please enter yout Email")
            
            if not self.register_data['dob']:
                error_messages.append("Please enter yout DOB")

            if not self.register_data['activity_level'] or (self.register_data['activity_level']).strip() == '--Select--':
                error_messages.append("Please select your activity level")

            if not self.register_data['gender']:
                error_messages.append("Please enter yout Gender")
            
            if self.register_data['password'] != self.register_data['confirm_password']:
                error_messages.append("Passwords do not match with conform password")
            try:
                weight = float(self.register_data['weight'])
                if weight < 20 or weight > 250:
                    error_messages.append("Weight must be between 20 and 250")
            except ValueError:
                error_messages.append("Invalid weight")

            try:
                height = float(self.register_data['height'])
                if height < 90 or height > 213:
                    error_messages.append("Height must be between 90cm and 213cm")
            except ValueError:
                error_messages.append("Invalid height")

            def error_back():
                self.register_button.configure(state='normal')
                self.whiteframe.grid_forget()
            if error_messages:    
                if len(error_messages) > 4:
                    error_messages.clear()
                    error_messages.append("Enter the necessary details")
                self.whiteframe = CTkFrame(master=self, 
                        width=450,
                        height=250,
                        fg_color=('#FFFFFF','#333333'),
                        border_color=('#333333','#CCCCCC'),
                        border_width=1
                        )
                meh_image = CTkImage(dark_image=Image.open(self.app.meh_image_path), size=(40,40))
                self.error_e = CTkLabel(self.whiteframe, text='\n'.join(error_messages), font=('x', 25), text_color=('#333333', '#FFFFFF'))
                self.error_e.grid(row=0, column=0, padx=20, pady=20)
                self.error_e_image = CTkLabel(master=self.whiteframe, text="", image=meh_image)
                self.error_e_image.grid(row=1, column=0, padx=20, pady=(15,20))
                self.whiteframe.grid(row=0, column=0, padx=20, pady=30)    
                self.whiteframe.after(2000, error_back) 
                # messagebox.showerror("Error", "\n".join(error_messages))
            else:
                self.register_data['register_time'] = datetime.now()
                del self.register_data['confirm_password']
                try :
                    db = WD.Database()
                    code = UserIDGenerator()
                    db.create_tables()
                    userid = code.generate_user_id()
                    # load_mode()
                    self.register_data['userid'] = userid
                    # db.get_all_values('userdata')
                    done = db.set_values(tablename='userdata', data=self.register_data)
                    db.close_connection()
                except Exception as e:
                    self.logger.error(f"Error in register page: registerdata: {e}")
                if done == True:
                # Register Success image
                    thumb_up_image = CTkImage(dark_image=Image.open(self.app.success_register_image_path), size=(40,40))
                    # Register Success frame
                    self.whiteframe = CTkFrame(master=self, 
                        width=450,
                        height=250,
                        fg_color=('#FFFFFF','#333333'),
                        border_color=('#333333','#CCCCCC'),
                        border_width=1
                    )    
                    self.login_s = CTkLabel(self.whiteframe, text='Registered Successfully', font=('x', 25), text_color=('#333333', '#FFFFFF'))
                    self.login_s.grid(row=0, column=0, padx=20, pady=30)
                    self.login_s_image = CTkLabel(master=self.whiteframe, text="", image=thumb_up_image)
                    self.login_s_image.grid(row=1, column=1, padx=20, pady=20)
                    self.progressbar_login_s =  CTkProgressBar(master=self.whiteframe, width=398, height=20, border_width=0, corner_radius=10, fg_color=("#EEEEEE",'#333333'), progress_color=('#2196F3','#4CAF50'), border_color=("#F2F2F2",'#555555'), determinate_speed=1.90)
                    self.progressbar_login_s.set(0)
                    self.progressbar_login_s.start()
                    self.progressbar_login_s.grid(row=1, column=0, padx=20, pady=30)
                    self.whiteframe.grid(row=0, column=0, padx=20, pady=30)
                    def change_reg_s():
                        self.login_s.configure(text="Getting things ready for you")
                    self.whiteframe.after(1500, change_reg_s)
                    def switch_to_homepage():
                        self.app.show_page("HomePage", userdata=self.register_data)
                    self.whiteframe.after(3500, switch_to_homepage)
                elif done == False: 
                    self.whiteframe = CTkFrame(master=self, 
                        width=450,
                        height=250,
                        fg_color=('#FFFFFF','#333333'),
                        border_color=('#333333','#CCCCCC'),
                        border_width=1)
                    thumb_down_image = CTkImage(dark_image=Image.open(self.app.fail_register_image_path), size=(40,40))
                    self.login_f = CTkLabel(self.whiteframe, text='Username already taken', font=('x', 25), text_color=('#333333', '#FFFFFF'))
                    self.login_f.grid(row=0, column=0, padx=20, pady=20)
                    self.login_f_image = CTkLabel(master=self.whiteframe, text="", image=thumb_down_image)
                    self.login_f_image.grid(row=1, column=0, padx=20, pady=(15,20))
                    self.whiteframe.grid(row=0, column=0, padx=20, pady=30)    
                    self.whiteframe.after(2000, error_back)  
                else:
                    self.logger.error("Error register_user - error_messages - else block: {e}",)      
        except Exception as e:
            self.logger.error(f'Error register_user: {e}')
