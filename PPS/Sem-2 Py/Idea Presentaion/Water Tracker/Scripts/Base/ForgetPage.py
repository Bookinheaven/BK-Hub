from typing import Any
from customtkinter import *
from ..Utilities.Generator import EmailSender
from ..Utilities.DatabaseMethods import *
from datetime import datetime

from PIL import Image

Font = 'Arial'
class ForgetPage(CTkFrame):    
    def __init__(self, master: Any, app: Any):
        super().__init__(master) 
        self.configure(fg_color=('#333333','#1E1E1E'))
        self.grid_configure(sticky='nsew')
        # Basic Configure in master(waterintake base) and self
        # master.configure(fg_color=('#ffffff','#111b21'),border_width=0,corner_radius=10)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.center_frame = CTkFrame(self, fg_color=('#FFFFFF','#333333'), width=600, height=600)
        self.username = None
        self.code = None
        self.userdata = None
        self.username_entry_inner = None
        def error_back():
            self.whiteframe.grid_forget()
            self.button.configure(state='normal')
        def check_time(self):
            current_time = datetime.now()
            # Calculate the difference in time
            if self.userdata["verificationtime"]:
                time_difference = current_time - self.userdata["verificationtime"]

                # Check if the time difference is less than 10 minutes
                if time_difference.total_seconds() < 600:  # 10 minutes = 600 seconds
                    self.userdata["verifiedcode"] = True
                    print("Success")
                else:
                    self.userdata["verifiedcode"] = False
                    print("timed out")

                # Print the updated userdata
                update_userdata(self=app, userdata=self.userdata)
                
                if self.userdata["verifiedcode"] == True:
                    password_page()
                    pass
                # app.show_page('LoginPage')
            else:
                print('nOne Found')

        def back(event):
            app.show_page("LoginPage")
        
        # self.center_frame.columnconfigure((0,1,2), weight=1)

        back_image = CTkImage(dark_image=Image.open(app.arrow_left_light),light_image=Image.open(app.arrow_left_dark), size=(40,40))
        self.backtosingup_label = CTkLabel(master=self.center_frame, text= '', text_color=('#333333', '#FFFFFF'), fg_color=('#FFFFFF','#333333'), width=50, height=50,font=('x',25), image=back_image,cursor='hand2')
        self.backtosingup_label.grid(row=0, column=0, padx=10,pady=10,sticky='w')
        self.backtosingup_label.bind("<Button-1>", command=back)
        

        self.login_label = CTkLabel(self.center_frame, text="Forget Password",font=(Font,29), text_color=('#333333', '#FFFFFF'))
        self.login_label.grid(row=0, column=0, padx=20, pady=(10,0))
        def check_code(self):
            if self.username_entry:
                self.username = self.username_entry.get() 
            current_code = self.code_entry.get()
            if self.code:
                print(self.code)
            elif self.userdata:
                self.code = self.userdata['verificationcode']
            else:
                self.userdata = database_extractor(app, userdata=True, username=self.username.strip())
                self.code = self.userdata['verificationcode']
            if current_code == self.code:
                check_time(self)
            else: 
                print('Invalid Code')

        def code_subpage(self):
            if self.username_label.grid_info() and self.gmail_entry.grid_info():
                for item in self.changer:
                    item.grid_remove()
                self.got_code.configure(text='forgot code?')
                if not self.username:
                    self.username_label.grid(row=2, column=0, padx=50, pady=(10,0), sticky='w')
                    self.username_entry.grid(row=3, column=0, padx=50, pady=10, sticky='w')

                    self.username_entry.configure(validate="key", validatecommand=(validation_cmd, '%S'))
                    self.username_entry.focus() 
                self.code_label = CTkLabel(master=self.center_frame, text='Code', font=(Font, 25), anchor='center',text_color=('#333333', '#FFFFFF'))
                self.code_label.grid(row=4, column=0, padx=50, pady=(10,0), sticky='w')
                self.code_entry = CTkEntry(master=self.center_frame,width=400, height=40, font=(Font,23), text_color=('#333333', '#FFFFFF'), placeholder_text='Code',placeholder_text_color=("#999999", "#CCCCCC"), fg_color=("#F2F2F2",'#555555'), corner_radius=3, border_color=('#CCCCCC','#999999'), border_width=1)
                self.code_entry.grid(row=5, column=0, padx=50, pady=10, sticky='w')
                def button_click():
                    check_code(self)
                self.button.configure(command=button_click, state='normal')
            else:
                for item in self.changer:
                    item.grid()
                self.code_label.grid_remove()
                self.code_entry.grid_remove()
                self.got_code.configure(text='got code?')
                self.button.configure(command=send_mail, state='normal')

        # Check for username :
        check = False
        def validate_space(char):
            if char == " ":
                return False
            return True
        validation_cmd = self.center_frame.register(validate_space)
        # Username
        if not check:
            def send_mail(event=None):
                self.button.configure(state="disabled")
                self.username = self.username_entry.get()
                gmail = self.gmail_entry.get()
                if self.username and gmail:
                    self.userdata = database_extractor(app, userdata=True, username=self.username.strip())
                    if self.userdata:
                        if self.userdata['email'] == gmail.strip():
                            Mail = EmailSender(receiver_mail=gmail, mode='verify', app=app)
                            internet = Mail.check_internet_connection()
                            if internet == False:
                                self.button.configure(state="disabled")
                                self.whiteframe = CTkFrame(master=self, 
                                        width=450,
                                        height=250,
                                        fg_color=('#FFFFFF','#333333'),
                                        border_color=('#333333','#CCCCCC'),
                                        border_width=1
                                        )
                                meh_image = CTkImage(dark_image=Image.open(app.meh_image_path), size=(40,40))
                                self.error_e = CTkLabel(self.whiteframe, text='No Internet', font=('x', 25), text_color=('#333333', '#FFFFFF'))
                                self.error_e.grid(row=0, column=0, padx=20, pady=(20,5))
                                self.error_e_image = CTkLabel(master=self.whiteframe, text="", image=meh_image)
                                self.error_e_image.grid(row=1, column=0, padx=(5,20), pady=(15,20))
                                self.whiteframe.grid(row=0, column=0, padx=20, pady=30)    
                                self.whiteframe.after(2000, error_back) 
                            else:
                                Mail.send_email()
                                self.code = Mail.get_code()
                                if self.code :
                                    self.userdata['verificationcode'] = self.code
                                    # self.userdata['verifiedcode']
                                    self.userdata['verificationtime'] = datetime.now()
                                    update_userdata(self=app, userdata=self.userdata)
                                    code_subpage(self)
                                    # app.show_page('LoginPage')
                        else:
                            self.button.configure(state="disabled")
                            self.whiteframe = CTkFrame(master=self, 
                                    width=450,
                                    height=250,
                                    fg_color=('#FFFFFF','#333333'),
                                    border_color=('#333333','#CCCCCC'),
                                    border_width=1
                                    )
                            meh_image = CTkImage(dark_image=Image.open(app.meh_image_path), size=(40,40))
                            self.error_e = CTkLabel(self.whiteframe, text='Email Incorrect', font=('x', 25), text_color=('#333333', '#FFFFFF'))
                            self.error_e.grid(row=0, column=0, padx=20, pady=(20,5))
                            self.error_e_image = CTkLabel(master=self.whiteframe, text="", image=meh_image)
                            self.error_e_image.grid(row=1, column=0, padx=(5,20), pady=(15,20))
                            self.whiteframe.grid(row=0, column=0, padx=20, pady=30)    
                            self.whiteframe.after(2000, error_back) 
                    else:
                        self.button.configure(state="disabled")
                        self.whiteframe = CTkFrame(master=self, 
                                width=450,
                                height=250,
                                fg_color=('#FFFFFF','#333333'),
                                border_color=('#333333','#CCCCCC'),
                                border_width=1
                                )
                        meh_image = CTkImage(dark_image=Image.open(app.meh_image_path), size=(40,40))
                        self.error_e = CTkLabel(self.whiteframe, text='No User Found!', font=('x', 25), text_color=('#333333', '#FFFFFF'))
                        self.error_e.grid(row=0, column=0, padx=20, pady=(20,5))
                        self.error_e_image = CTkLabel(master=self.whiteframe, text="", image=meh_image)
                        self.error_e_image.grid(row=1, column=0, padx=(5,20), pady=(15,20))
                        self.whiteframe.grid(row=0, column=0, padx=20, pady=30)    
                        self.whiteframe.after(2000, error_back) 
                else:
                    # Change the colors
                    if not gmail:
                        self.gmail_entry.configure(border_color='#FF664B')
                        self.button.configure(state="normal")
                    else:
                        self.gmail_entry.configure(border_color=('#CCCCCC','#999999'))
                    if not self.username:
                        self.username_entry.configure(border_color='#FF664B')
                        self.button.configure(state="normal")
                    else:
                        self.username_entry.configure(border_color=('#CCCCCC','#999999'))

            self.username_label = CTkLabel(master=self.center_frame, text='Username', font=(Font, 25), anchor='center',text_color=('#333333', '#FFFFFF'))
            self.username_label.grid(row=2, column=0, padx=50, pady=(10,0), sticky='w')

            self.username_entry = CTkEntry(master=self.center_frame,width=400, height=40, font=(Font,23), text_color=('#333333', '#FFFFFF'), placeholder_text='Username',placeholder_text_color=("#999999", "#CCCCCC"), fg_color=("#F2F2F2",'#555555'), corner_radius=3, border_color=('#CCCCCC','#999999'), border_width=1)
            self.username_entry.grid(row=3, column=0, padx=50, pady=10, sticky='w')

            self.username_entry.configure(validate="key", validatecommand=(validation_cmd, '%S'))
            self.username_entry.focus() 
            
            self.gmail_label = CTkLabel(master=self.center_frame, text='Gmail', font=('x', 25), anchor='center',text_color=('#333333', '#FFFFFF'))
            self.gmail_label.grid(row=4, column=0, padx=50, pady=(10,0), sticky='w')

            self.gmail_entry = CTkEntry(master=self.center_frame,width=400, height=40, font=(Font,23), text_color=('#333333', '#FFFFFF'), placeholder_text='Gmail',placeholder_text_color=("#999999", "#CCCCCC"), fg_color=("#F2F2F2",'#555555'), corner_radius=3, border_color=('#CCCCCC','#999999'), border_width=1)
            self.gmail_entry.grid(row=5, column=0, padx=50, pady=10, sticky='w')
            
            self.changer = [self.username_label, self.username_entry, self.gmail_label, self.gmail_entry]
            def got_code_click(event):
                self.got_code.configure(text_color="#1877f2")
                code_subpage(self)

            def on_enter_got_code(event):
                self.got_code.configure(font=("Bold", 18), text_color="#FF6347")

            def on_leave_got_code(event):
                self.got_code.configure(font=("Bold", 17), text_color="#1877f2")
                
            self.got_code = CTkLabel(self.center_frame, text="got code?", font=("Bold", 17), text_color='#1877f2', anchor='ne', cursor='hand2')
            self.got_code.grid(row=6, column=0, padx=(0,30), sticky='e')

            self.got_code.bind('<ButtonPress>', got_code_click)
            self.got_code.bind('<Enter>', on_enter_got_code)
            self.got_code.bind('<Leave>', on_leave_got_code)

            self.button = CTkButton(self.center_frame, width=50, height=50, text="Verify", font=("Bold", 28), text_color='white', anchor='center', command=send_mail,fg_color='#1877f2')
            self.button.grid(row=7, column=0,padx=100, pady=(10,30), sticky='nswe')
            self.gmail_entry.bind('<Return>', send_mail)
                
        # Password
        def password_page():
            def change_pass():
                self.button.configure(state="disabled")
                error_messages = []
                old_password = self.userdata['password']
                password = self.password_entry.get()
                conform_password = self.conform_password_entry.get()
                if len(password) < 8 or len(password) > 25:
                    error_messages.append("Password must be between 8 and 25 characters")
                if password != conform_password:
                    print(password, conform_password)
                    error_messages.append("Passwords do not match with conform password")
                if old_password.strip() == password:
                    error_messages.append("It Matchs the old password")

                if error_messages:    
                    self.whiteframe = CTkFrame(master=self, 
                            width=450,
                            height=250,
                            fg_color=('#FFFFFF','#333333'),
                            border_color=('#333333','#CCCCCC'),
                            border_width=1
                            )
                    meh_image = CTkImage(dark_image=Image.open(app.meh_image_path), size=(40,40))
                    self.error_e = CTkLabel(self.whiteframe, text='\n'.join(error_messages), font=('x', 25), text_color=('#333333', '#FFFFFF'))
                    self.error_e.grid(row=0, column=0, padx=20, pady=(20,5))
                    self.error_e_image = CTkLabel(master=self.whiteframe, text="", image=meh_image)
                    self.error_e_image.grid(row=1, column=0, padx=20, pady=(15,20))
                    self.whiteframe.grid(row=0, column=0, padx=20, pady=30)    
                    self.whiteframe.after(2000, error_back) 
                else:
                    self.userdata['password'] = password
                    update_userdata(self=app, userdata=self.userdata)
                    # Password Change Success frame
                    self.button.configure(state='disabled')
                    self.whiteframe = CTkFrame(master=self, 
                            width=450,
                            height=250,
                            fg_color=('#FFFFFF','#333333'),
                            border_color=('#333333','#CCCCCC'),
                            border_width=1
                            )
                    self.succ_p = CTkLabel(self.whiteframe, text='Loading..', font=('x', 25), text_color=('#333333', '#FFFFFF'))
                    self.progress_bar = CTkProgressBar(master=self.whiteframe, height=10, width=120, progress_color=('#2196F3','#4CAF50'), mode='indeterminate', indeterminate_speed=1, fg_color=("#EEEEEE",'#333333'),border_color=("#F2F2F2",'#555555'))
                    self.progress_bar.grid(row=1, column=0, padx=10, pady=10)
                    self.progress_bar.set(0)
                    self.progress_bar.start()
                    self.whiteframe.grid(row=0, column=0, padx=20, pady=0)    
                    self.succ_p.grid(row=0, column=0, padx=20, pady=10)
                    def switch_to_loginpage():
                        self.whiteframe.grid_forget()
                        self.center_frame.grid_forget()
                        # print(self.userdata)
                        last_login(app, userdata=self.userdata)
                        app.show_page("LoginPage", userdata=self.userdata)
                    self.whiteframe.after(3000, switch_to_loginpage)

            def pass_check(event):
                password = self.password_entry.get()
                confirm_password = self.conform_password_entry.get()
                if len(password) > 0:
                    if password != confirm_password:
                        if len(password) <= len(confirm_password):
                            self.conform_password_entry.configure(border_color='#FF664B')
                        
                    else:
                        self.conform_password_entry.configure(border_color=('#CCCCCC','#999999'))
            if self.got_code.grid_info():
                self.got_code.grid_remove()
            if self.code_label.grid_info():    
                self.code_label.grid_remove()
                self.code_entry.grid_remove()
            if self.username_label.grid_info() :    
                self.username_label.grid_remove()
                self.username_entry.grid_remove()

            self.button.configure(text='Change', command=change_pass)
            self.password_label = CTkLabel(master=self.center_frame, text='New Password', font=('x', 25), anchor='center',text_color=('#333333', '#FFFFFF'))
            self.password_label.grid(row=2, column=0, padx=50, pady=(10,0), sticky='w')

            self.password_entry = CTkEntry(master=self.center_frame, width=400, height=40, font=("Bold",23), text_color=('#333333', '#FFFFFF'), placeholder_text='New Password',placeholder_text_color=("#999999", "#CCCCCC"), fg_color=("#F2F2F2",'#555555'), corner_radius=3, border_color=('#CCCCCC','#999999'), border_width=1, show='*')
            self.password_entry.grid(row=3, column=0, padx=50, pady=10, sticky='w')
            
            self.password_level_label = CTkLabel(master=self.center_frame, text="", font=('x', 20), anchor='center',text_color=('#333333', '#FFFFFF'))
            self.password_level_label.grid(row=2, column=0, padx=170, pady=(10,0), sticky='w')

            self.password_progressbar = CTkProgressBar(self.center_frame,width=396,height=7,border_width=0, corner_radius=3, fg_color=("#F2F2F2",'#555555'), progress_color='white', border_color='#F6F4F9')
            self.password_progressbar.grid(row=3, column=0, padx=51, pady=(32,0), sticky='w')
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
            self.conform_password_label = CTkLabel(master=self.center_frame, text='Conform Password', font=('x', 25), anchor='center',text_color=('#333333', '#FFFFFF'))
            self.conform_password_label.grid(row=4, column=0, padx=50, pady=(10,0), sticky='w')

            self.conform_password_entry = CTkEntry(master=self.center_frame, width=400, height=40, font=("Bold",23), text_color=('#333333', '#FFFFFF'), placeholder_text='Conform Password',placeholder_text_color=("#999999", "#CCCCCC"), fg_color=("#F2F2F2",'#555555'), corner_radius=3, border_color=('#CCCCCC','#999999'), border_width=1, show='*')
            self.conform_password_entry.grid(row=5, column=0, padx=50, pady=10, sticky='w')
            self.conform_password_entry.bind("<KeyRelease>", command=pass_check)
            
            self.image_eye_on = CTkImage(dark_image=Image.open(app.eye_on_light),light_image=Image.open(app.eye_on_dark), size=(20,20))
            self.image_eye_off = CTkImage(dark_image=Image.open(app.eye_off_light),light_image=Image.open(app.eye_off_dark), size=(20,20))
            self.eye_pwd_label = CTkLabel(master=self.center_frame, text="", image=self.image_eye_off, cursor='hand2', fg_color=("#F2F2F2",'#555555'))
            self.eye_pwd_label.grid(row=3, column=0, padx=57, pady=(6,10), sticky='e')
            self.eye_cnpwd_label = CTkLabel(master=self.center_frame, text="", image=self.image_eye_off, cursor='hand2', fg_color=("#F2F2F2",'#555555'))
            self.eye_cnpwd_label.grid(row=5, column=0, padx=57, pady=10, sticky='e')
            
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

        self.center_frame.grid(row=0, column=0, padx=20, pady=30)