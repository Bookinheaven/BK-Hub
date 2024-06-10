from typing import Any
from customtkinter import *
from PIL import Image, ImageDraw 
from ..Utilities.Generator import WaterIntake
from ..Utilities.DatabaseMethods import *
from ..Utilities.LevelingSystem import LevelingSystem
from ..Utilities.GraphManger import pie_graph
from tkinter import ttk

# Dark theme & Light theme
BackgroundFgColor = ('#ffffff', '#111b21')
SubFramsFgColor = ('#3EA1FF','#3EA1FF')
SegmentFramesFgColor = ('#FFFFFF', '#202c33')
SubSegmentFramesFgColor = ('#f0f2f5','#2a3942')
TextColor = ('#333333', '#FFFFFF')
SubTextColor = ('#333333', '#FFFFFF')
FontName = 'Ariral'
FrameFgColor = ('#C0E1FF','#00c8fb')
ProgressBar = '#86bbd8'

def update_pie_graph(self, app):
    # Clear the current plot
    # Extracting Userstats From Raw - Organized.
    self.userstats = database_extractor(app, userstats=True, userid=self.userdata['userid'].strip())
    history = self.userstats['waterintakehistory']
    def for_single_date():
            valuex = [] # Default / Pre-Defined
            for key, value in history.items():
                if key == date.today().strftime('%m/%d/%Y'):  
                    valuex.append({
                        key: value}) # Adding to the list
            return valuex
    
    data = for_single_date()[0]
    if self.graph_pie != None:
        self.ax.clear()
    if len(data) > 0:
        finval = data
    else:
        finval = {'No Data': {'currentpoints': 0, 'dailypoints': 0, 'drank': 0, 'drink': 0}}
    self.graph_pie, self.ax = pie_graph(self=self.piechart, rawdata=finval)
    self.graph_pie_tk = self.graph_pie.get_tk_widget()
    self.graph_pie_tk.grid_propagate(False)
    self.graph_pie_tk.grid_rowconfigure(0, weight=1) 
    self.graph_pie_tk.grid_columnconfigure(0, weight=1)
    self.graph_pie_tk.config(height=400, width=400)
    self.graph_pie_tk.config(bg='#202c33')
    
    self.graph_pie_tk.grid(row=0, column=0, padx=5, pady=5)

class HomePage(CTkFrame):    
    def __init__(self, master: Any, app: Any):
        super().__init__(master)
        self.configure(fg_color='transparent')
        # Data from the login or registerpage.
        self.userdata : dict = app.userdata
        self.piechart = None
        self.graph_pie = None
        self.logger = app.logger
        
        # To make sure there are no changes in the data.
        self.userdata : dict = database_extractor(app, userdata=True, username=self.userdata['username'].strip())
        
        # Extracting Userstats From Raw - Organized.
        self.ExtractedData : dict = database_extractor(app, userstats=True, userid=self.userdata['userid'].strip())
        
        # Setting up daily amount from formula.
        WaterStatsChanger : dict = WaterIntake(userdata=self.userdata, userstats=self.ExtractedData)
        
        # Uploading the water stats and other unchanged data.
        self.FinalData : dict = WaterStatsChanger.set_userstats()

        # Resets the 24hr timer if timer is not set.
        reset_daily_values(self=self)
        LevelingSystem(self.userdata, app=app)
        # Update all the data from above
        update_data(self=self)

        # Basic Configure in master(waterintake base) and self
        master.configure(fg_color=BackgroundFgColor,border_width=0,corner_radius=10)
        self.configure(fg_color=BackgroundFgColor)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_configure(sticky='nsew')
        
        # Main scrollable frame
        self.top_level_scroll_bar =  CTkScrollableFrame(master=self,corner_radius=10,fg_color=FrameFgColor)
        
        # Top frame for tile and user profile
        self.top_tag_frame = CTkFrame(master=self.top_level_scroll_bar,corner_radius=10,fg_color=SubSegmentFramesFgColor)
        
        # Top frame sub frame: 1 (right side) for give a fake space
        self.right_top_tag = CTkFrame(master=self.top_tag_frame,corner_radius=10,fg_color='transparent')
        null_label = CTkLabel(master=self.right_top_tag, text='          ')
        null_label.grid(row=0, column=0, padx=90, pady=10)
        

        # Top frame sub frame: 2 (center) for title
        self.center_top_tag = CTkFrame(master=self.top_tag_frame,corner_radius=10,fg_color='transparent')    
        self.title_label = CTkLabel(master=self.center_top_tag, text="Water Intake", font=('Arial',44), fg_color='transparent', text_color=('#333333', '#FFFFFF'))
        self.title_label.grid(row=0, column=0, padx=10, pady=10)

        # Top frame sub frame: 3 (left) for username and profile picture
        self.left_top_tag = CTkFrame(master=self.top_tag_frame,corner_radius=10,fg_color='transparent')
        
        # User profile image 
        def check_profile_pic(user_id, assets_folder=app.Assets):
            profile_pic_folder = os.path.join(assets_folder, "UserProfile")
            image_extensions = [".png", ".jpg", ".jpeg"] 

            for ext in image_extensions:
                pic_file = f"{user_id}{ext}"  
                profile_pic_path = os.path.join(profile_pic_folder, pic_file)
                if os.path.exists(profile_pic_path):
                    return profile_pic_path  # Return the path if the profile picture is found
            return None
        
        check_pr = check_profile_pic(user_id=self.userdata['userid'])
        if check_pr:
            user_image_before = Image.open(check_pr)
        else:
            user_image_before = Image.open(app.user_image_path)
        user_image_after = Image.new("RGBA", user_image_before.size)
        draw = ImageDraw.Draw(user_image_after)
        draw.pieslice([(0, 0), user_image_before.size], 0, 360, fill="black")
        draw.pieslice([(10, 10), user_image_before.size], 0, 360, fill="white")
        user_image_after.paste(user_image_before, (0, 0), mask=user_image_after)
        user_image = CTkImage(dark_image=user_image_after, size=(42,42))
        self.logo_label = CTkLabel(master=self.left_top_tag, text="", image=user_image,text_color=TextColor, font=("Ariral", 20))
        self.logo_label.grid(row=0, column=3,sticky='ne', padx=10, pady=10)
        
        # Username Label 
        self.user_name_label = CTkLabel(master=self.left_top_tag, text=self.userdata["username"], text_color=TextColor, font=("Ariral", 20), cursor='hand2')
        self.user_name_label.grid(row=0, column=2,sticky='ne', padx=(0,10), pady=(10, 5))
        
        # Username Labels effects
        def on_username_click(event):
            self.user_name_label.configure(text_color=('#333333', '#FFFFFF'))
            app.logger.info("on_username_click: show settings")
            
        def on_enter(event):
            self.user_name_label.configure(font=("Ariral", 20), text_color=('#333333', '#FFFFFF'))
            
        def on_leave(event):
            self.user_name_label.configure(font=("Ariral", 20), text_color=('#333333', '#FFFFFF'))
        
        # Binding username label for effects
        self.user_name_label.bind('<ButtonPress>', on_username_click)
        self.user_name_label.bind('<Enter>', on_enter)
        self.user_name_label.bind('<Leave>', on_leave)

        # Progress Bar for level
        self.progr = CTkProgressBar(master=self.left_top_tag, orientation='horizontal', width=140, height=5, progress_color='#B4FF88', border_color='black',fg_color='black')
        self.progr.grid(row=0, column=2,sticky='se', padx=10, pady=20)
        level_me = LevelingSystem(userdata=self.userdata,app=app)
        level_me.check_level_up(app=app)
        th = level_me.generate_level_threshold(current_level=self.userdata["level"])
        experience_points = int(self.userdata.get('experiencepoints', 0))

        # Retrieve the threshold for the next level
        next_level_threshold = th.get(self.userdata['level'] + 1, 0)
        difference = next_level_threshold - experience_points
        progress_percentage = 1 - min(difference / next_level_threshold, 1.0)  # Ensure progress is capped at 1.0
        self.progr.set(progress_percentage)

        # Label for level number 
        self.level_label = CTkLabel(master=self.left_top_tag, text=f'Level: {self.userdata["level"]}', text_color=TextColor, font=("Ariral", 20), cursor='hand2')
        self.level_label.grid(row=0, column=1,sticky='se', padx=(0,20), pady=(30,10))
        
        
        # Grid for Top frame sub: 1
        self.right_top_tag.grid(row=0, column=0,padx=10,pady=10,sticky='nsew')
        self.right_top_tag.columnconfigure(0,weight=1)
        self.right_top_tag.rowconfigure(0,weight=1)
        
        # Grid for Top frame sub: 2
        self.center_top_tag.grid(row=0, column=1,padx=10,pady=10, sticky='nsew')
        self.center_top_tag.columnconfigure(0,weight=1)
        self.center_top_tag.rowconfigure(0,weight=1)
        
        # Grid for Top frame sub: 3
        self.left_top_tag.grid(row=0, column=2, sticky='nsew',padx=10,pady=10)
        self.left_top_tag.columnconfigure(0,weight=1)
        self.left_top_tag.rowconfigure(0,weight=1)
        
        # Grid for Top frame
        self.top_tag_frame.grid(row=0, column=0, sticky='nsew',padx=10,pady=5)
        self.top_tag_frame.columnconfigure([0,1,2],weight=1)
        self.top_tag_frame.rowconfigure(0,weight=1)

        self.mini_bar_frame = CTkFrame(
            master=self.top_level_scroll_bar,
            corner_radius=10,
            fg_color=SubSegmentFramesFgColor, #'#00c8fb',
            height=600
        )
        self.mini_bar_frame.rowconfigure([0,1], weight=1)
        self.mini_bar_frame.columnconfigure([0,1,2], weight=1)
        self.drink_frame = CTkFrame(
            master=self.mini_bar_frame,
            corner_radius=10,
            fg_color=SegmentFramesFgColor
        )
        self.drink_frame.grid(row=1, column=0, sticky='nsew', padx=20, pady=20)
        self.drink_frame.rowconfigure([0,1], weight=1)
        self.drink_frame.columnconfigure(0, weight=1)
        self.drink_label = CTkLabel(master=self.drink_frame, text="Drink", text_color=SubTextColor,bg_color="transparent", font=("Ariral", 20))
        self.drink_label.grid(row=0, column=0,padx=20, pady=(5, 1))
        self.drink_amount_label = CTkLabel(master=self.drink_frame, text=f"{self.FinalData['dailyintakegoal']:.1f} L", text_color=SubTextColor,bg_color="transparent",font=("Ariral", 20))
        self.drink_amount_label.grid(row=1, column=0,padx=20, pady=(1, 5))

        self.drank_frame = CTkFrame(
            master=self.mini_bar_frame,
            corner_radius=10,
            fg_color=SegmentFramesFgColor
        )
        self.drank_frame.grid(row=1, column=1, sticky='nsew', padx=20, pady=20)
        self.drank_frame.rowconfigure([0,1], weight=1)
        self.drank_frame.columnconfigure(1, weight=1)
        self.drank_label = CTkLabel(master=self.drank_frame, text="Drank", text_color=SubTextColor,bg_color="transparent", font=("Ariral", 20))
        self.drank_label.grid(row=0, column=1,padx=20, pady=(5, 1))
        self.drank_amount_label = CTkLabel(master=self.drank_frame, text=f"{self.FinalData['currentwaterintake']:.1f} L", text_color=SubTextColor,bg_color="transparent",font=("Ariral", 20))
        self.drank_amount_label.grid(row=1, column=1,padx=20, pady=(1, 5))

        self.need_to_drink_frame = CTkFrame(
            master=self.mini_bar_frame,
            corner_radius=10,
            fg_color=SegmentFramesFgColor
        )
        drank_amout = float(abs(float(self.FinalData['dailyintakegoal']) - float(self.FinalData['currentwaterintake'])))
        if self.FinalData['currentwaterintake'] > self.FinalData['dailyintakegoal']:
            drank_amout = 0.0
        self.need_to_drink_frame.grid(row=1, column=2, sticky='nsew', padx=20, pady=20)
        self.need_to_drink_frame.rowconfigure([0,1], weight=1)
        self.need_to_drink_frame.columnconfigure(2, weight=1)
        self.need_to_drink_label = CTkLabel(master=self.need_to_drink_frame, text="Need to drink", text_color=SubTextColor,bg_color="transparent", font=("Ariral", 20))
        self.need_to_drink_label.grid(row=0, column=2,padx=20, pady=(5, 1))
        self.need_to_drink_amount_label = CTkLabel(master=self.need_to_drink_frame, text=f"{drank_amout:.1f} L", text_color=SubTextColor,bg_color="transparent",font=("Ariral", 20))
        self.need_to_drink_amount_label.grid(row=1, column=2,padx=20, pady=(1, 5))
        self.mini_bar_frame.grid(row=1, column=0, padx=10,pady=10,sticky='nsew')

        self.mid_page_frame = CTkFrame(
            master=self.top_level_scroll_bar,
            fg_color=SubSegmentFramesFgColor,#'#53C6FF', 
            corner_radius=10
            )
        self.left_mid_frame = CTkFrame(
            master=self.mid_page_frame,
            corner_radius=10,
            fg_color='transparent')
        self.left_mid_frame.rowconfigure([0,1], weight=1)
        self.left_mid_frame.columnconfigure(0, weight=2)
        self.start_label = CTkLabel(master=self.left_mid_frame, text='Start', text_color=TextColor,bg_color="transparent", font=("Ariral", 20))
        self.start_label.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)
        self.point_label = CTkLabel(master=self.left_mid_frame, text='Points', text_color=TextColor,bg_color="transparent", font=("Ariral", 20))
        self.point_label.grid(row=1, column=0, sticky='nsew', padx=10, pady=(25,10))
        self.center_mid_frame = CTkFrame(
            master=self.mid_page_frame,
            corner_radius=10,
            fg_color='transparent')
        self.center_mid_frame.rowconfigure([0,1,2], weight=1)
        self.center_mid_frame.columnconfigure(0, weight=1)
        widt : int = int(self.center_mid_frame.winfo_screenmmwidth() * 0.05)
        hight : int = int(self.center_mid_frame.winfo_screenmmheight() * 20/100)
        perce = self.FinalData['currentwaterintake'] / self.FinalData['dailyintakegoal'] *100 
        perce = max(0, min(perce, 100))
        self.perce_label = CTkLabel(master=self.center_mid_frame, text=f'{perce:.1f}%', text_color=TextColor,bg_color="transparent", font=("Ariral", 20))
        self.perce_label.grid(row=0, column=0, sticky='nsew', padx=10, pady=(10,5))

        self.center_progress_bar1 = CTkProgressBar(master=self.center_mid_frame, orientation='horizontal', width=widt, height=hight, progress_color=ProgressBar, border_color='black',fg_color='white')
        self.center_progress_bar1.set(perce/100)
        self.center_progress_bar1.grid(row=1, column=0, padx=10, pady=(0, 10), sticky='nsew')
        # print(self.data1['currentpoints'], self.data1['dailypoints'])
        perce_points : int = int(self.FinalData['currentpoints'])
        perce_points = max(0, min(perce_points, 100))
        # print(perce_points)
        self.perce_point_label = CTkLabel(master=self.center_mid_frame, text=f'{perce_points}', text_color=TextColor,bg_color="transparent", font=("Ariral", 20))
        self.perce_point_label.grid(row=2, column=0, sticky='nsew', padx=(5,0), pady=10)

        self.center_progress_bar2 = CTkProgressBar(master=self.center_mid_frame, orientation='horizontal', width=widt, height=hight, progress_color=ProgressBar, border_color='black',fg_color='white')
        self.center_progress_bar2.set(0)
        self.center_progress_bar2.set(perce_points/100)
        
        self.center_progress_bar2.grid(row=3, column=0, padx=10, pady=(5,20), sticky='nsew')
        
        self.right_mid_frame = CTkFrame(
            master=self.mid_page_frame,
            corner_radius=10,
            fg_color='transparent')
        
        self.right_mid_frame.rowconfigure([0,1], weight=1)
        self.right_mid_frame.columnconfigure(0, weight=1)
        self.end_label = CTkLabel(master=self.right_mid_frame, text='End', text_color=TextColor,bg_color="transparent", font=("Ariral", 20))
        self.end_label.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)
        self.end_point_label = CTkLabel(master=self.right_mid_frame, text='100', text_color=TextColor,bg_color="transparent", font=("Ariral", 20))
        self.end_point_label.grid(row=1, column=0, sticky='nsew', padx=10, pady=10)

        self.left_mid_frame.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')
        self.center_mid_frame.grid(row=0, column=1, padx=10, pady=10, sticky='nsew', columnspan=6) 
        self.right_mid_frame.grid(row=0, column=7, padx=10, pady=10, sticky='nsew')
        self.mid_page_frame.grid(row=2, column=0, padx=10, pady=10, sticky='nsew', columnspan=7)
        self.mid_page_frame.columnconfigure([0, 1, 2, 3, 4, 5, 6, 7], weight=1)
        self.mid_page_frame.rowconfigure(0, weight=1)

        self.amount = ['100 ml', '250 ml', '500 ml', '750 ml', '1 L', '2 L', '4 L']
        self.step = 0
        self.down_frame = CTkFrame(
            master=self.top_level_scroll_bar,
            fg_color=SubSegmentFramesFgColor, 
            corner_radius=10
            )
        self.left_mid_label2 = CTkLabel(master=self.down_frame, text='Status', text_color=TextColor, font=(FontName, 40))
        def left_label(event):
            item = self.amount[self.step]
            if 'ml' in item:
                inc_value(self=self, valx=int(item.split(' ')[0]), measure='ml')
            if 'L' in item:
                inc_value(self=self, valx=int(item.split(' ')[0]), measure='l')
            update_data(self=self)
            update_widgets(self=self, app=app)
            if self.piechart != None:
                update_pie_graph(self=self,app=app)
        self.left_down_frame = CTkFrame(
            master=self.down_frame,
            corner_radius=10, fg_color='transparent')
        separator = ttk.Separator(self.down_frame, orient='vertical')
        separator.grid(row=1,column=1,
                            sticky='ns', padx=(0,10), pady=(0, 10))
        self.left_down_frame.rowconfigure([0,1], weight=1)
        self.left_down_frame.columnconfigure(0, weight=1)
        self.waterdrop_img = CTkImage(dark_image=Image.open(app.waterdrop_image), size=(300,300))
        self.left_drop_label = CTkLabel(master=self.left_down_frame, text='', image=self.waterdrop_img, cursor='hand2', fg_color='transparent')
        self.left_drop_label.grid(row=0, column=0, padx=10, pady=10)
        self.left_label_ml = CTkLabel(master=self.left_down_frame, text=f'{self.amount[self.step]}', cursor='hand2', text_color=TextColor, font=('Ariral', 30), fg_color='#3bb8e4')
        self.left_label_ml.grid(row=0, column=0, padx=5, pady=(55,5), ipadx=0, ipady=0,rowspan=3)
        self.left_drop_label.bind('<ButtonPress>',left_label)
        self.left_label_ml.bind('<ButtonPress>', left_label)
        
        def plus_button_callback():
            if self.step < len(self.amount) -1 :
                if self.step >= 0:
                    self.step += 1
                    self.left_label_ml.configure(text=f'{self.amount[self.step]}')
                self.minus_button.configure(state='normal')
            else:
                self.plus_button.configure(state='disabled')
        
        def minus_button_callback():
            if self.step <= len(self.amount) - 1:
                if self.step >= 0:
                    if self.step > 0:
                        self.step -= 1
                    self.left_label_ml.configure(text=f'{self.amount[self.step]}')
                self.plus_button.configure(state='normal')
            if self.step == 0:
                self.minus_button.configure(state='disabled')

        self.button_frame = CTkFrame(
            master=self.left_down_frame,
            corner_radius=10,
            fg_color='transparent') 
        self.plus_button= CTkButton(self.button_frame, text="+",width=30,height=30,command=plus_button_callback,font=(FontName, 30), text_color=TextColor,hover_color=SubSegmentFramesFgColor,corner_radius=2,fg_color=BackgroundFgColor)
        self.minus_button= CTkButton(self.button_frame, text="-",width=30,height=30,command=minus_button_callback,font=(FontName, 30), text_color=TextColor,hover_color=SubSegmentFramesFgColor,corner_radius=2,fg_color=BackgroundFgColor, state='disabled')
        
        self.plus_button.grid(row=0, column=0, padx=10, pady=5, ipadx=10, ipady=10)
        self.minus_button.grid(row=1, column=0, padx=10, pady=5, ipadx=10, ipady=10)

        self.piechart = CTkFrame(
            master=self.down_frame,
            corner_radius=10,
            fg_color=SegmentFramesFgColor)
        update_pie_graph(self=self,app=app)
        self.piechart.grid(row=1, column=2, padx=10, pady=10)
        self.button_frame.grid(row=0, column=1, padx=(5, 10), pady=60)
        self.left_mid_label2.grid(row=0, column=2, padx=10, pady=12)
        self.left_down_frame.grid(row=0, column=0, padx=5, pady=10, rowspan=2)
        self.down_frame.columnconfigure([0, 1,2], weight=1)
        self.down_frame.rowconfigure([0,1], weight=1)
        self.down_frame.grid(row=3, column=0, padx=10, pady=10, sticky='nsew')

        # Main scrollable frame grid
        self.top_level_scroll_bar.grid_columnconfigure(0,weight=1)
        self.top_level_scroll_bar.rowconfigure([2,3], weight=1)
        self.top_level_scroll_bar.grid(row=0, column=0, sticky='nsew',padx=2,pady=2)