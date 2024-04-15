from customtkinter import *
from PIL import Image
from ..Utilities.DatabaseMethods import last_login, database_extractor

class LoginPage(CTkFrame):
    def __init__(self, master, app):
        super().__init__(master)
        master.configure(fg_color=('#333333','#1E1E1E'))
        self.configure(fg_color=('#FFFFFF','#333333'))
        self.logger = app.logger
        self.login_frame = CTkFrame(
            master=self,
            width=600,
            height=600,
            fg_color=('#FFFFFF','#333333')
        )

        self.login_label = CTkLabel(self.login_frame, text="Sign In",font=("Bold",29), text_color=('#333333', '#FFFFFF'), anchor='w')
        self.login_frame.columnconfigure(0, weight=1)
        self.login_frame.rowconfigure((0,1,2,3,4,5,6,7,8), weight=1)
        
        self.login_label.grid(row=0, column=0, padx=30, pady=20, sticky='nswe')  
        
        self.username_label = CTkLabel(self.login_frame, text="Username", font=("Bold",20), text_color=('#333333', '#FFFFFF'), anchor='w')
        self.username_label.grid(row=1, column=0, padx=30, pady=5, sticky='nswe')  

        self.username_input = CTkEntry(self.login_frame, height=40,width=400, font=("Bold",23), text_color=('#333333', '#FFFFFF'), placeholder_text='Username',placeholder_text_color=("#999999", "#CCCCCC"), fg_color=("#F2F2F2",'#555555'), corner_radius=3, border_color=('#CCCCCC','#999999'), border_width=1)
        self.username_input.grid(row=2, column=0, padx=30, pady=5, sticky='nswe')    
        self.username_input.focus()
        
        self.password_label = CTkLabel(self.login_frame, text="Password", font=("Bold",20), text_color=('#333333', '#FFFFFF'),anchor="w")
        self.password_label.grid(row=3, column=0, padx=30, pady=(20,5), sticky='nswe')    

        
        self.password_input = CTkEntry(self.login_frame, height=40, font=("Bold", 23), text_color=('#333333', '#FFFFFF'), show="*", placeholder_text='Password',placeholder_text_color=("#999999", "#CCCCCC"), fg_color=("#F2F2F2",'#555555'), corner_radius=3, border_color=('#CCCCCC','#999999'), border_width=1)#, textvariable=self.password_var)
        self.password_input.grid(row=4, column=0, padx=30, pady=5, sticky='nswe')  
        
        self.image_eye_off = CTkImage(dark_image=Image.open(app.eye_off_light),light_image=Image.open(app.eye_off_dark), size=(20,20))
        self.eye_label = CTkLabel(master=self.login_frame, text="", image=self.image_eye_off, cursor='hand2', fg_color=("#F2F2F2",'#555555'))
        self.eye_label.grid(row=4, column=0, padx=40, pady=10, sticky='e')
        
        def validate_space(char):
            return char != " "

        self.username_input.configure(validate="key", validatecommand=(self.login_frame.register(validate_space), '%S'))
        self.password_input.configure(validate="key", validatecommand=(self.login_frame.register(validate_space), '%S'))


        def reveal_password(event):
            self.image_eye_on = CTkImage(dark_image=Image.open(app.eye_on_light),light_image=Image.open(app.eye_on_dark), size=(20,20))
            self.eye_label.configure(image=self.image_eye_on)
            self.password_input.configure(show="")

        def hide_password(event):
            self.eye_label.configure(image=self.image_eye_off)
            self.password_input.configure(show="*")

        self.password_input.bind('<KeyRelease>', validate_space)
        self.username_input.bind('<KeyRelease>', validate_space)
        self.eye_label.bind("<ButtonPress>", reveal_password)
        self.eye_label.bind("<ButtonRelease>", hide_password)
        self.username_input.focus() 

        def on_forget_password_click(event):
            self.forget_password_label.configure(text_color="#1877f2")
            app.show_page("ForgetPage")

        def on_enter_forget_password(event):
            self.forget_password_label.configure(font=("Bold", 18), text_color="#FF6347")

        def on_leave_forget_password(event):
            self.forget_password_label.configure(font=("Bold", 16), text_color="#1877f2")
            
        self.forget_password_label = CTkLabel(self.login_frame, text="forgot password?", font=("Bold", 16), text_color='#1877f2', anchor='ne', cursor='hand2')
        self.forget_password_label.grid(row=5, column=0, padx=(0,30), sticky='e')

        self.forget_password_label.bind('<ButtonPress>', on_forget_password_click)
        self.forget_password_label.bind('<Enter>', on_enter_forget_password)
        self.forget_password_label.bind('<Leave>', on_leave_forget_password)
        
        def login_button(event=None):
            username = self.username_input.get()
            password = self.password_input.get()
            self.button.configure(state="disabled")
            def handle_error_display():
                self.whiteframe.grid_forget() 
                self.button.configure(state="normal")
            if username and password:
                try:
                    self.userdata = database_extractor(app, userdata=True, username=username.strip())
                    if self.userdata:
                        def hide_whiteframe():
                            try:
                                self.whiteframe.grid_forget()
                                self.whiteframe.master.update()
                                self.button.configure(state="normal")
                            except Exception as e:
                                app.logger.error("Error hiding whiteframe:", e)
                        if password != self.userdata['password']:
                            self.whiteframe = CTkFrame(master=app.side_page, 
                                    width=450,
                                    height=250,
                                    fg_color=('#FFFFFF','#333333'),
                                    border_color=('#333333','#CCCCCC'),
                                    border_width=1
                                    )
                            password_incorrect = CTkImage(dark_image=Image.open(app.password_incorrect_image_path), size=(40,40))
                            self.whiteframe.grid(row=0, column=0, padx=20, pady=30)    
                            self.error_p = CTkLabel(self.whiteframe, text='Incorrect Password', font=('x', 25), text_color=('#333333', '#FFFFFF'))
                            self.error_p.grid(row=0, column=0, padx=20, pady=10)
                            self.error_p_image = CTkLabel(master=self.whiteframe, text="", image=password_incorrect)
                            self.error_p_image.grid(row=1, column=0, padx=20, pady=(15,20))
                            self.whiteframe.after(2000, lambda : hide_whiteframe())

                        else:
                            self.button.configure(state="disabled")
                            # print(self.userdata)
                            self.whiteframe = CTkFrame(master=app.side_page, 
                                    width=450,
                                    height=250,
                                    fg_color=('#FFFFFF','#333333'),
                                    border_color=('#333333','#CCCCCC'),
                                    border_width=1
                                    )
                            self.error_p = CTkLabel(self.whiteframe, text='Loading..', font=('x', 25), text_color=('#333333', '#FFFFFF'))
                            self.progress_bar = CTkProgressBar(master=self.whiteframe, height=10, width=120, progress_color=('#2196F3','#4CAF50'), mode='indeterminate', indeterminate_speed=1, fg_color=("#EEEEEE",'#333333'),border_color=("#F2F2F2",'#555555'))
                            self.progress_bar.grid(row=1, column=0, padx=10, pady=10)
                            self.progress_bar.set(0)
                            self.progress_bar.start()
                            self.error_p.grid(row=0, column=0, padx=20, pady=10)
                            self.whiteframe.grid(row=0, column=0, padx=20, pady=30)    
                            def switch_to_homepage():
                                self.whiteframe.grid_forget()
                                self.login_frame.grid_forget()
                                # print(self.userdata)
                                last_login(app, userdata=self.userdata)
                                app.show_page("HomePage", userdata=self.userdata)
                            self.whiteframe.after(3000, switch_to_homepage)
                    else:
                        self.whiteframe = CTkFrame(master=app.mainpage, 
                                width=450,
                                height=250,
                                fg_color=('#FFFFFF','#333333'),
                                border_color=('#333333','#CCCCCC'),
                                border_width=1,
                                )
                        username_incorrect = CTkImage(dark_image=Image.open(app.password_incorrect_image_path), size=(40,40))
                        self.error_p = CTkLabel(self.whiteframe, text='No User Found', font=('x', 25), text_color=('#333333', '#FFFFFF'))
                        self.error_p.grid(row=0, column=0, padx=20, pady=10)
                        self.error_p_image = CTkLabel(master=self.whiteframe, text="", image=username_incorrect)
                        self.error_p_image.grid(row=1, column=0, padx=20, pady=(15,20))
                        self.whiteframe.after(2000, handle_error_display)
                        self.whiteframe.grid(row=0, column=0, padx=20, pady=30)    
                except Exception as e:
                    app.logger.error(f"Error in Login Button: {e}")
        
            if not password:
                self.password_input.configure(border_color='#FF664B')
                self.button.configure(state="normal")
            else:
                self.password_input.configure(border_color=('#CCCCCC','#999999'))
            if not username:
                self.username_input.configure(border_color='#FF664B')
                self.button.configure(state="normal")
            else:
                self.username_input.configure(border_color=('#CCCCCC','#999999'))

        self.button = CTkButton(self.login_frame, width=50, height=50, text="Login", font=("Bold", 28), text_color='white', anchor='center', command=login_button,fg_color='#1877f2')
        self.button.grid(row=6, column=0,padx=100, pady=5, sticky='nswe')
        self.password_input.bind('<Return>', login_button)

        def on_signup_click(event):
            self.signup_label.configure(text_color="black")
            app.show_page("RegisterPage")

        def on_enter(event):
            self.signup_label.configure(font=("Bold", 24), text_color="#FF6347")
            
        def on_leave(event):
            self.signup_label.configure(font=("Bold", 22), text_color="#1877f2")
        
        self.or_label = CTkLabel(self.login_frame, text="or", font=("Bold",20), text_color=('#333333', '#FFFFFF'), anchor='w')
        self.or_label.grid(row=7, column=0, padx=100, pady=5, sticky='s')

        self.signup_label = CTkLabel(self.login_frame, width=50, height=50, text="Sign Up", font=("Bold",22), text_color='#1877f2', anchor='n', cursor='hand2')
        self.signup_label.grid(row=8, column=0 ,padx=100, pady=5, sticky='s')
        self.signup_label.bind('<ButtonPress>', on_signup_click)
        self.signup_label.bind('<Enter>', on_enter)
        self.signup_label.bind('<Leave>', on_leave)
        self.login_frame.grid(row=0, column=0, padx=10, pady=10)