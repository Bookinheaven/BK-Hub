import time
from ..Base import WaterDatabase as WD
import platform

def update_exp_levl(self, userdata):
    try:
        db = WD.Database()
        db.update_values(tablename='userdata', data=userdata)
    except Exception as e:
        self.logger.error("Error update_exp_levl: inserting data into userdata table:", e)
    finally:
        db.close_connection()
        # print('updated successfully')

def send_notification(self,app, title, message):
    current_platform = platform.system()
    
    if current_platform == 'Windows':
        from winotify import Notification
        import os
        toast = Notification(app_id='Water Intake', title=title, msg=message, icon=f'{os.path.join(app.Assets, "Images", "ICO", "water-drop.ico")}')
        toast.show()
    elif current_platform == 'Darwin':
        import os
        os.system(f'terminal-notifier -title "{title}" -message "{message}"')
    elif current_platform == 'Linux':
        import os
        os.system(f'notify-send "{title}" "{message}"')
    else:
        self.logger.error("Unsupported operating system")

class LevelingSystem:
    def __init__(self, userdata, app):
        self.logger = app.logger
        try:
            self.userdata = userdata
            if not self.userdata['level'] or self.userdata['level'] == '' or self.userdata['level'] == None or self.userdata['level'] == 0:
                self.userdata['level'] = 1
                update_exp_levl(self=self, userdata=self.userdata)
            if not self.userdata['experiencepoints'] or self.userdata['experiencepoints'] == '' or self.userdata['experiencepoints'] == None:
                self.userdata['experiencepoints'] = 0
                update_exp_levl(self=self, userdata=self.userdata)
            self.level_threshold = self.generate_level_threshold(current_level=self.userdata['level'])
        except Exception as e:
            self.logger.error(f"Error in LevelingSystem: {e}")

    def generate_level_threshold(self, current_level):
            try:
                max_level = current_level + 1
                return {level+1:  0 if level == 0 else round(level * 100*1.2) for level in range(0, max_level)}
            except Exception as e:
                self.logger.error(f"Error in LevelingSystem (generate_level_threshold): {e}")

    def check_level_up(self,app):
        try:
            if self.userdata['level'] + 1 in self.level_threshold and self.userdata['experiencepoints'] >= self.level_threshold[self.userdata['level'] +1]:
                self.userdata["level"] += 1
                self.userdata["experiencepoints"] = 0
                send_notification(self=self, app=app, title='Level Up!', message=f"Congratulations! You reached level {self.userdata["level"]}!")
                update_exp_levl(self=self, userdata=self.userdata)
                return self.userdata
        except Exception as e:
            self.logger.error(f"Error in LevelingSystem (check_level_up): {e}")

if __name__ == '__main__':   
    st = time.time()
    from datetime import datetime         
    userdata = {'userid': 'BK19021140937', 'name': 'tanvik123', 'username': 'tanvik123', 'password': 'tanvik123', 'dob': datetime.date(2005, 3, 1), 'gender': 'Male', 'email': 'tanviksriram@gmail.com', 'activity_level': 'Medium Level',
                'weight': 40, 'height': 90, 'register_time': datetime.datetime(2024, 3, 31, 22, 1, 26, 183891), 'level': 1, 'experiencepoints': 120,
                'lastlogin': datetime.datetime(2024, 4, 3, 9, 53, 49, 66786), 'verificationcode': None, 'verifiedcode': None, 'recoveryemail': None, 'recoverycode': None}
    a = LevelingSystem(userdata=userdata)
    levelUP,level = a.check_level_up()
    if levelUP:
        print(f"Congratulations! You reached level {level}!")

    et = time.time()
    elapsed_time = et - st
    print('Execution time:', elapsed_time, 'seconds')