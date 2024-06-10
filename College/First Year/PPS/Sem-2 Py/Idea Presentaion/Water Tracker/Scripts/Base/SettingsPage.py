from tkinter import filedialog, ttk
from typing import Any
from PIL import Image, ImageDraw
import os
import shutil
from datetime import datetime
from customtkinter import CTkFrame, CTkLabel, CTkButton, CTkOptionMenu, CTkScrollableFrame, CTkImage, set_appearance_mode, get_appearance_mode
from ..Utilities.DatabaseMethods import update_data,database_extractor
from ..Utilities.JsonMethods import load_data_mode, save_data
from ..Utilities.LevelingSystem import LevelingSystem

BackgroundFgColor = ('#ffffff', '#111b21')
FrameFgColor = ('#f0f2f5', '#202c33')
SubFramsFgColor = '#7D7D7D'
TextColor = '#FFFFFF'
FontName = 'Arial'


class SettingsPage(CTkFrame):
    def __init__(self, master: Any, app: Any):
        super().__init__(master)
        self.app = app

        # Configure app's color scheme
        app.configure(fg_color=BackgroundFgColor)

        # Data from the login or registerpage.
        self.userdata: dict = app.userdata

        # To make sure there are no changes in the data.
        self.userdata : dict = database_extractor(app, userdata=True, username=self.userdata['username'].strip())
        
        # Extracting Userstats From Raw - Organized.
        self.userstats : dict = database_extractor(app, userstats=True, userid=self.userdata['userid'].strip())

        # Frame configuration
        self.grid_configure(sticky='nsew')
        app.configure(fg_color=('#d8e2eb', '#202c33'))

        # Scrollable frame for profile settings
        self.profile_scroll_bar = CTkScrollableFrame(
            master=self, corner_radius=10, fg_color=('#ffffff', '#111b21'))
        self.profile_scroll_bar.grid(
            row=0, column=0, padx=2, pady=2, sticky='nsew')
        self.profile_scroll_bar.rowconfigure([0, 1, 2, 3, 4], weight=1)
        self.profile_scroll_bar.columnconfigure([0, 1, 2], weight=1)

        # Title label
        self.title_label = CTkLabel(master=self.profile_scroll_bar, text="Settings", font=(
            'Arial', 44), fg_color='transparent', text_color=('#333333', '#FFFFFF'))
        self.title_label.grid(row=0, column=0, padx=10, pady=10)

        # User details frame
        self.user_details_frame = CTkFrame(
            master=self.profile_scroll_bar, corner_radius=10, fg_color=FrameFgColor)

        # Function to create label-value pair
        def create_label_value_pair(frame, label_text, value_text, row):
            label = CTkLabel(frame, text=label_text, anchor="w", font=(
                "Bold", 20), text_color=('#333333', '#FFFFFF'))
            label.grid(row=row, column=0, padx=10, pady=(10, 0), sticky='nw')
            value_label = CTkLabel(frame, text=value_text, anchor="w", font=(
                "Arial", 18), text_color=('#333333', '#FFFFFF'))
            value_label.grid(row=row, column=1, padx=10,
                             pady=(10, 0), sticky='nw')
            separator = ttk.Separator(frame, orient='horizontal')
            separator.grid(row=row + 1, columnspan=2,
                            sticky='ew', padx=10, pady=(0, 10))

        last_login_str = self.userdata['lastlogin'].strftime(
            "%d-%m-%Y %H:%M:%S") if self.userdata['lastlogin'] else "Now"
        
        last_dp = self.userstats['lastprofileupdate'].strftime(
            "%d-%m-%Y %H:%M:%S") if self.userstats['lastprofileupdate'] else "Never"
        last_reset = self.userstats['lastresettime'].strftime(
            "%d-%m-%Y %H:%M:%S") if self.userstats['lastresettime'] else "Never"
        level_me = LevelingSystem(userdata=self.userdata,app=app)
        th = level_me.generate_level_threshold(current_level=self.userdata["level"])
        next_level_threshold = th.get(self.userdata['level'] + 1, 0)
        
        # Labels for user details
        create_label_value_pair(
            self.user_details_frame, "Name:", self.userdata['name'], 1)
        create_label_value_pair(
            self.user_details_frame, "Email:", self.userdata['email'], 3)
        create_label_value_pair(
            self.user_details_frame, "Weight:", str(self.userdata['weight']), 5)
        create_label_value_pair(
            self.user_details_frame, "Height:", str(self.userdata['height']), 7)
        create_label_value_pair(
            self.user_details_frame, "Date of birth:", self.userdata['dob'], 9)
        create_label_value_pair(
            self.user_details_frame, "Gender:", self.userdata['gender'], 11)
        create_label_value_pair(
            self.user_details_frame, "Level:", self.userdata['level'], 13)
        create_label_value_pair(
            self.user_details_frame, "Experience Points:", f'{self.userdata['experiencepoints']} / {next_level_threshold}', 15)
        create_label_value_pair(
            self.user_details_frame, "Activity Level:", self.userdata['activity_level'], 17)
        create_label_value_pair(
            self.user_details_frame, "Last login:", last_login_str, 19)
        create_label_value_pair(
            self.user_details_frame, "Last DP Upload:", last_dp, 21)
        create_label_value_pair(
            self.user_details_frame, "Last reset Time:", last_reset, 23)

        # Logo label for profile picture
        self.logo_label = CTkLabel(master=self.user_details_frame, text="")
        self.logo_label.grid(row=0, column=1, rowspan=4,
                             padx=5, pady=5, sticky='ne')

        # Update profile picture
        self.img_upda()

        # Configure row and column weights
        self.user_details_frame.rowconfigure(
            [0, 2, 4, 6, 8, 10, 12, 14, 16], weight=1)
        self.user_details_frame.columnconfigure([0, 1], weight=1)

        # Grid the user details frame
        self.user_details_frame.grid(
            row=1, column=0, padx=10, pady=10, sticky='nsew')

        # Settings frame
        self.settings_frame = CTkFrame(
            master=self.profile_scroll_bar, corner_radius=10, fg_color=FrameFgColor)
        self.settings_frame.grid(
            row=3, column=0, padx=10, pady=10, sticky='nw')

        # Appearance mode label and option menu
        self.appearance_mode_label = CTkLabel(
            self.settings_frame, text="Appearance Mode", anchor="w", font=('Arial', 30), fg_color='transparent', text_color=('#333333', '#FFFFFF'))
        self.appearance_mode_label.grid(
            row=0, column=0, padx=20, pady=20, sticky='nw')
        self.appearance_mode_optionemenu = CTkOptionMenu(self.settings_frame, values=[
                                                         "System", "Dark", "Light"], command=self.change_appearance_mode_event, width=140, height=40, font=('Ariral', 15))
        self.appearance_mode_optionemenu.set(get_appearance_mode())
        self.appearance_mode_optionemenu.grid(
            row=0, column=1, padx=20, pady=20)

        # Profile settings
        self.profile_label = CTkLabel(
            self.profile_scroll_bar, text="Profile Picture:", anchor="w", font=('Arial', 30), fg_color='transparent', text_color=('#333333', '#FFFFFF'))
        self.profile_label.grid(
            row=6, column=0, sticky='nw', pady=10, padx=10)

        self.profile_frame = CTkFrame(
            master=self.profile_scroll_bar, corner_radius=10, fg_color=FrameFgColor, height=300, width=300)
        self.profile_frame.grid(
            row=7, column=0, padx=10, pady=10, sticky='nw')

        self.profile_upload_label = CTkLabel(
            self.profile_frame, text="Upload Picture: ", anchor="w", font=('Arial', 20), fg_color='transparent', text_color=('#333333', '#FFFFFF'))
        self.status_profile_upload_label = CTkLabel(
            self.profile_frame, text="", anchor="w", font=('Arial', 20), fg_color='transparent', text_color=('#333333', '#FFFFFF'))

        self.profile_upload_button = CTkButton(
            self.profile_frame, width=50, height=50, text="Upload", font=("Bold", 28), text_color='white', anchor='center', command=self.upload_picture, fg_color='#1877f2')
        self.profile_upload_button.grid(
            row=0, column=1, sticky='nw', pady=10, padx=40)
        self.profile_upload_label.grid(
            row=0, column=0, sticky='nw', pady=10, padx=10)
        self.status_profile_upload_label.grid(
            row=1, column=0, sticky='nw', pady=10, padx=10, columnspan=2)

        self.profile_frame.rowconfigure([0, 1, 2], weight=1)
        self.profile_frame.columnconfigure(1, weight=1)

        self.timer_frame = CTkFrame(
            master=self.profile_scroll_bar, corner_radius=10, fg_color=FrameFgColor)
        self.timer_frame.grid(
            row=8, column=0, padx=10, pady=10, sticky='nw')

        self.password_frame = CTkFrame(
            master=self.profile_scroll_bar, corner_radius=10, fg_color=FrameFgColor)
        self.password_frame.grid(
            row=9, column=0, padx=10, pady=10, sticky='nw')

    def img_upda(self):
        def check_profile_pic(user_id, assets_folder=self.app.Assets):
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
            user_image_before = Image.open(self.app.user_image_path)
        user_image_after = Image.new("RGBA", user_image_before.size)
        draw = ImageDraw.Draw(user_image_after)
        draw.pieslice([(0, 0), user_image_before.size], 0,
                      360, fill="black")
        draw.pieslice([(10, 10), user_image_before.size], 0,
                      360, fill="white")
        user_image_after.paste(
            user_image_before, (0, 0), mask=user_image_after)
        user_image = CTkImage(
            dark_image=user_image_after, size=(100, 100))
        self.logo_label.configure(image=user_image)

    def upload_picture(self):
        self.filename = filedialog.askopenfilename(
            initialdir=os.getcwd(),
            title="Select Image",
            filetypes=[("images files", "*.png *.jpg *.jpeg"), ]
        )
        if self.filename:
            filenameSplitted = self.filename.split('.')
            folder = os.path.join(self.app.Assets, "UserProfile")
            os.makedirs(os.path.dirname(folder), exist_ok=True)
            # Delete existing files with the same name
            for file in os.listdir(folder):
                if file.startswith(f'{self.userdata["userid"]}') and os.path.splitext(file)[1].lower() in ['.png', '.jpg', '.jpeg']:
                    os.remove(os.path.join(folder, file))

            folder = os.path.join(
                self.app.Assets, "UserProfile", f'{self.userdata["userid"]}.{filenameSplitted[-1]}')

            # Copy the new file
            shutil.copy(self.filename, rf'{folder}')
            self.status_profile_upload_label.configure(
                text='Successfully Uploaded The Image!')
            self.userstats['lastprofileupdate'] = datetime.today()
            # Update all the data from above
            self.app.FinalData = self.userstats
            update_data(self=self.app)
            self.img_upda()

    def change_appearance_mode_event(self, new_appearance_mode: str):
        set_appearance_mode(new_appearance_mode)
        da = {'mode': new_appearance_mode}
        save_data(self=self.app, data=da)


