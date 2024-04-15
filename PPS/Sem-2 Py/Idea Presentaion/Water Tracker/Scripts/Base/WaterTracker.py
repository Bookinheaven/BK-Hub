from customtkinter import *
from PIL import Image
import ctypes
from ..Utilities.window import center_screen
from .HistoryPage import HistoryPage
from .RegisterPage import RegisterPage
from .LoginPage import LoginPage
from .HomePage import HomePage
from .SettingsPage import SettingsPage
from .ForgetPage import ForgetPage
from ..Utilities.JsonMethods import load_data_mode
import logging

class WaterIntake(CTk):
    def Logger_setup(self):
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(filename)s | %(message)s', datefmt='%d-%m-%Y | %I:%M:%S %p')
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

        file_handler = logging.FileHandler('logfile.log')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        return logger
    def __init__(self):
        super().__init__()
        self.logger = self.Logger_setup()    
        self.logger.info("WaterIntake Base Script Loaded!")
        self.home_slider = 0
        self.sidebar_frame = None
        self.x=0
        self.zoom_set = 0
        deactivate_automatic_dpi_awareness()
        self.title('Water Intake')
        self.minsize(700,700)
        # self.maxsize(500,500)
        # change_scaling_event()
        
        try :
            myappid = 'BurnKnuckle_Head_Up!'
            self.Assets = os.path.dirname(__file__).replace(r'Scripts\Base', 'Assets')
            ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
            self.iconbitmap(f"{os.path.join(self.Assets, "Images", "ICO", "water-drop.ico")}")
            self.background_image_path = os.path.join(self.Assets, "Images", "Background", "background.jpg")
            # Regiser Page
            self.arrow_left_dark = os.path.join(self.Assets, "Images","RegiserPage", "arrow_left_dark.png")
            self.arrow_left_light = os.path.join(self.Assets, "Images","RegiserPage", "arrow_left_light.png")
            self.meh_image_path = os.path.join(self.Assets, "Images","RegiserPage", "meh.png") # #FF664B
            self.fail_register_image_path = os.path.join(self.Assets, "Images","RegiserPage", "thumbs_down.png")
            self.success_register_image_path = os.path.join(self.Assets, "Images","RegiserPage", "thumbs_up.png")

            self.password_incorrect_image_path = os.path.join(self.Assets, "Images","LoginPage", "alert_circle.png")
            # Login Page
            self.eye_on_dark = os.path.join(self.Assets, "Images", "LoginPage", "eye_on_dark.png")
            self.eye_off_dark = os.path.join(self.Assets, "Images", "LoginPage", "eye_off_dark.png")
            self.eye_on_light = os.path.join(self.Assets, "Images", "LoginPage", "eye_on_light.png")
            self.eye_off_light = os.path.join(self.Assets, "Images", "LoginPage", "eye_off_light.png")
            # Home Page
            self.menu_light = os.path.join(self.Assets, "Images", "HomePage", "menu_light.png")
            self.menu_dark = os.path.join(self.Assets, "Images", "HomePage", "menu_dark.png")
            self.user_image_path = os.path.join(self.Assets, "Images", "HomePage", "user.png")
            self.waterdrop_image = os.path.join(self.Assets, "Images", "HomePage", "waterdrop.png")
            self.logout_light = os.path.join(self.Assets, "Images", "HomePage", "log-out_light.png")
            self.logout_dark = os.path.join(self.Assets, "Images", "HomePage", "log-out_dark.png")
            # Hisotry Page
            self.calendar_light_image = os.path.join(self.Assets, "Images", "HistoryPage", "calendar_light.png")
            self.calendar_dark_image = os.path.join(self.Assets, "Images", "HistoryPage", "calendar_dark.png")
            
            #Json File
            self.json_mode_file = os.path.join(self.Assets, "mode.json")
            mode = get_appearance_mode()
            data = load_data_mode(self=self, mode=mode)
            
            if data :
                self.logger.info("Mode Data Loaded!")
                set_appearance_mode(data['mode'])
            else:
                set_appearance_mode('System')
        except Exception as e:
            self.logger.error(f"Error in assets: {e}")
        self.configure(fg_color = ('#333333','#1E1E1E'))
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.mainpage = CTkFrame(
            master=self,
            fg_color=('#FFFFFF','#1E1E1E')
        )
        self.mainpage.grid(row=0, column=0, padx=0, pady=0)
        self.side_page = CTkFrame(self.mainpage, corner_radius=10,fg_color=('#FFFFFF','#1E1E1E'))
        self.side_page.grid(row=0, column=1, sticky="nsew",padx=0,pady=0)
    
        self.current_page = None
        # print(self.state())
        self.show_page("LoginPage")
        # self.show_page("HomePage",userdata=None)

    def set_sidebar(self):
        self.mainpage.grid_configure(sticky='nsew')
        def hide_slidebar(event):             
            # if self.sidebar_frame.grid_info() and self.home_slider == 0:
                # print("error")   
            if self.sidebar_frame.grid_info():
                self.sidebar_frame.grid_forget()
                self.home_slider = 0
                self.mainpage.grid_remove()
                self.side_page.grid_configure(row=0, column=0, sticky="nsew",padx=(70,0),pady=0)
                self.side_page.grid_rowconfigure(0, weight=1)
                self.side_page.grid_columnconfigure(0, weight=1)
                self.side_page.grid_columnconfigure(1, weight=0)
                self.mainpage.grid_columnconfigure(0, weight=1)
                self.mainpage.grid_columnconfigure(1, weight=0)
                self.mainpage.grid()
            else:
                self.home_slider = 1
                self.mainpage.grid_remove()
                self.side_page.grid_configure(row=0, column=1, sticky="nsew",padx=0,pady=0)
                self.side_page.grid_rowconfigure(0, weight=1)
                self.side_page.grid_columnconfigure(1, weight=0)
                self.side_page.grid_columnconfigure(0, weight=1)
                self.mainpage.grid_columnconfigure(0, weight=0)
                self.mainpage.grid_columnconfigure(1, weight=1)
                self.mainpage.grid()
                self.set_sidebar()

        self.sidebar_frame = CTkFrame(self.mainpage, corner_radius=10,fg_color=('#ffffff','#111b21'))
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nws")

        self.null_label = CTkLabel(master=self.sidebar_frame, text="")
        self.null_label.grid(row=0, column=0, padx=10,pady=(10,20))
        
        self.sidebar_option_1 = CTkLabel(self.sidebar_frame, text="Home", font=CTkFont(size=30), width=180,height=50, corner_radius=4)
        self.sidebar_option_1.grid(row=1, column=0, sticky='w',padx=10,pady=10)
        self.sidebar_option_1.bind("<Enter>", lambda event, label=self.sidebar_option_1: label.configure(fg_color=("#f0f2f5",'#2a3942')))
        self.sidebar_option_1.bind("<Leave>", lambda event, label=self.sidebar_option_1: label.configure(fg_color=("#ffffff",'#111b21')))
        # self.sidebar_option_1.bind("<Button-1>", lambda event: self.show_page("HomePage", userdata=None))
        self.sidebar_option_1.bind("<Button-1>", lambda event, label=self.sidebar_option_1: (
                                            self.show_page("HomePage", userdata=None),
                                            label.configure(fg_color=("#f5f6f6",'#202c33'))
                                            ))

        self.sidebar_option_2 = CTkLabel(self.sidebar_frame, text="History", font=CTkFont(size=30), width=180,height=50, corner_radius=4)
        self.sidebar_option_2.grid(row=2, column=0, sticky='w',padx=10,pady=12)
        self.sidebar_option_2.bind("<Enter>", lambda event, label=self.sidebar_option_2: label.configure(fg_color=("#f0f2f5",'#2a3942')))#202c33
        self.sidebar_option_2.bind("<Leave>", lambda event, label=self.sidebar_option_2: label.configure(fg_color=("#ffffff",'#111b21')))
        self.sidebar_option_2.bind("<Button-1>", lambda event: self.show_page("HistoryPage"))
        
        self.sidebar_option_3 = CTkLabel(self.sidebar_frame, text="Settings", font=CTkFont(size=30), width=180,height=50, corner_radius=4)
        self.sidebar_option_3.grid(row=3, column=0, sticky='w',padx=10,pady=12)
        self.sidebar_option_3.bind("<Enter>", lambda event, label=self.sidebar_option_3: label.configure(fg_color=("#f0f2f5",'#2a3942')))
        self.sidebar_option_3.bind("<Leave>", lambda event, label=self.sidebar_option_3: label.configure(fg_color=("#ffffff",'#111b21')))
        self.sidebar_option_3.bind("<Button-1>", lambda event: self.show_page("SettingsPage"))
        
        menu_image = CTkImage(dark_image=Image.open(self.menu_light),light_image=Image.open(self.menu_dark), size=(40,40))
        self.backtosingup_label = CTkLabel(master=self.mainpage, text= '', text_color='black', fg_color=('#f5f6f6','#202c33'),bg_color=('#f5f6f6','#202c33'), width=50, height=50,font=('x',25), image=menu_image,cursor='hand2', corner_radius=4)
        self.backtosingup_label.grid(row=0, column=0, padx=10,pady=10,sticky='nw')
        self.backtosingup_label.bind("<Button-1>", command=hide_slidebar)
        
        def set_logout(event):
            self.home_slider = 0
            for wid in self.mainpage.winfo_children():
                wid.grid_remove()
            self.side_page.grid_forget()
            self.mainpage.grid(row=0, column=0, sticky='nsew')
            self.show_page('LoginPage')
        logout_image = CTkImage(dark_image=Image.open(self.logout_light),light_image=Image.open(self.logout_dark), size=(40,40))
        self.logout_label = CTkLabel(master=self.mainpage, text= '', text_color='black', fg_color=("#ffffff",'#111b21'),bg_color=("#ffffff",'#111b21'), width=50, height=50,font=('x',25), image=logout_image,cursor='hand2', corner_radius=4)
        self.logout_label.grid(row=0, column=0, padx=10,pady=10,sticky='sw')
        self.logout_label.bind("<Button-1>", command=set_logout)
    
    def show_page(self, page_name, userdata=None):
        if not userdata and page_name != 'LoginPage' and page_name != 'RegisterPage':
            # print("Error showpages: No UserData ")
            pass
        else:
            self.userdata = userdata
        self.pages = {
            "HomePage": lambda: HomePage(master=self.side_page,app=self),
            "LoginPage": lambda: LoginPage(master=self.side_page,app=self),
            "HistoryPage": lambda: HistoryPage(master=self.side_page,app=self),
            "RegisterPage": lambda: RegisterPage(master=self.side_page,app=self),
            "SettingsPage": lambda: SettingsPage(master=self.side_page,app=self),
            "ForgetPage": lambda: ForgetPage(master=self.side_page, app=self)
        }
        if self.current_page:
            self.logger.info("{} --> {}".format((self.current_page.__class__).__name__, page_name))
            if (self.current_page.__class__).__name__ != page_name:
                for widget in self.current_page.winfo_children():
                    widget.destroy()
                self.current_page.grid_forget()
                self.current_page = self.pages[page_name]()
                self.current_page.grid(row=0, column=0)
        else:
            self.current_page = self.pages[page_name]()
            self.current_page.grid(row=0, column=0)
        self.current_page.grid_rowconfigure(0, weight=1)
        self.current_page.grid_columnconfigure(0, weight=1)

        if page_name == 'LoginPage' or page_name == 'RegisterPage' or page_name == 'ForgetPage':
            self.zoom_set = 0
            self.mainpage.grid_forget()
            self.side_page.grid_forget()
            self.mainpage.grid(row=0, column=0, sticky='nsew')
            self.mainpage.rowconfigure(0, weight=1)
            self.mainpage.columnconfigure(0, weight=1)
            self.mainpage.columnconfigure(1, weight=0)
            self.side_page.grid(row=0, column=0, sticky='nsew')
            self.side_page.rowconfigure(0, weight=1)
            self.side_page.columnconfigure(0, weight=1)
            center_screen(self, 1100, 1100)
        else:
            self.mainpage.grid_columnconfigure(0, weight=0)
            self.mainpage.grid_columnconfigure(1, weight=1)
            self.side_page.grid_configure(row=0, column=1, sticky="nsew",padx=0,pady=0)
            self.side_page.grid_rowconfigure(0, weight=1)
            self.side_page.grid_columnconfigure(1, weight=0)
            self.side_page.grid_columnconfigure(0, weight=1)
            if not self.home_slider or self.home_slider == 0 or self.sidebar_frame == None:
                self.home_slider = 1
                self.set_sidebar()
            else:
                self.home_slider = 0
                self.sidebar_frame.grid_remove()
            if not self.zoom_set:
                self.resizable(True, True)
                self.after(0, lambda:self.state('zoomed'))
                self.zoom_set = 1
