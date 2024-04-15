from json import dumps, loads
from datetime import datetime, date
from ..Base import WaterDatabase as WD
from ..Utilities.LevelingSystem import LevelingSystem

def update_userdata(self, userdata):
    try:
        db = WD.Database()
        db.update_values(tablename='userdata', data=userdata)
    except Exception as e:
        self.logger.error("Error update_exp_levl: inserting data into userdata table:", e)
    finally:
        db.close_connection()
        # print('updated successfully')

def update_widgets(self, page: str = 'home', app=None):
    try:
        if page == 'home':
            self.drank_amount_label.configure(text=f"{self.FinalData['currentwaterintake']:.1f} L")
            self.drink_amount_label.configure(text=f"{self.FinalData['dailyintakegoal']:.1f} L")
            drank_amout = float(abs(float(self.FinalData['dailyintakegoal']) - float(self.FinalData['currentwaterintake'])))
            if self.FinalData['currentwaterintake'] > self.FinalData['dailyintakegoal']:
                drank_amout = 0.0
            self.need_to_drink_amount_label.configure(text=f"{drank_amout:.1f} L")

            perce = self.FinalData['currentwaterintake'] / self.FinalData['dailyintakegoal'] *100 
            perce = max(0, min(perce, 100))
            self.perce_label.configure(text=f'{perce:.1f}%')
            self.center_progress_bar1.set(perce/100)

            perce_points = int(self.FinalData['currentpoints'])
            perce_points = max(0, min(perce_points, 100))
            self.perce_point_label.configure(text=f'{perce_points}')
            self.center_progress_bar2.set(perce_points/100)
            level_me = LevelingSystem(userdata=self.userdata,app=self)
            if app:
                data= level_me.check_level_up(app=app)
                if data:
                    self.userdata = data
                    self.level_label.configure(text=f'Level: {self.userdata["level"]}')
                th = level_me.generate_level_threshold(current_level=self.userdata["level"])
                experience_points = int(self.userdata.get('experiencepoints', 0))
                next_level_threshold = th.get(self.userdata['level'] + 1, 0)  # Default to 0 if the key is not found
                difference = next_level_threshold - experience_points
                progress_percentage = 1 - min(difference / next_level_threshold, 1.0)  # Ensure progress is capped at 1.0
                self.progr.set(progress_percentage)

        elif page == 'history':
            # print(len(self.values))
            # print(self.values)
            dates = [] # dates data
            self.finalvalues = {'currentpoints': 0, 'dailypoints': 0, 'drank': 0.0, 'drink': 0.0}
            for value in self.values:
                for key, val in value.items():
                    if key == 'day':
                        dates.append(val)
                    elif key == 'data':
                        for item, vl in val.items():
                            if item in self.finalvalues:
                                self.finalvalues[item] += vl 
            # Box 1 : Amount of water need to drink daily
            self.drink_amount_label.configure(text=f"{self.finalvalues['drink']:.1f} L")
            
            # Box 2 : Amount of water drank
            self.drank_amount_label.configure(text=f"{self.finalvalues['drank']:.1f} L")

            # Box 3 : Points Gained
            self.points_gained_amount_label.configure(text=f"{self.finalvalues['currentpoints']}")

            # Box 4 : Points Lost or Extra Points
            # pointslost = min(0, max(self.finalvalues['dailypoints'] - self.finalvalues['currentpoints'], 0))
            pointslost = self.finalvalues['dailypoints'] - self.finalvalues['currentpoints']
            if pointslost > 0:
                pointslost = f"{pointslost}"
                self.points_lost_label.configure(text='Points Need to Gain')
            elif pointslost < 0:
                pointslost = abs(pointslost)
                pointslost = f"{pointslost}"
                self.points_lost_label.configure(text='Extra Points')

            self.points_lost_amount_label.configure(text=f"{pointslost}")
    except Exception as e:
        self.logger.error(f"Error update_widgets: In DatabaseMethods: {e}")

def last_login(self, userdata):
    userdata['lastlogin'] = datetime.now()
    update_userdata(self, userdata=userdata)

def reset_daily_values(self):
    now = datetime.now()
    last_reset_time = self.FinalData.get('lastresettime')
    # If last reset time is not set or it's before today's midnight, reset values
    if last_reset_time is None or last_reset_time.date() < now.date():
        self.FinalData['currentpoints'] = 0
        self.FinalData['currentwaterintake'] = 0
        # Set last reset time to today's midnight
        self.FinalData['lastresettime'] = datetime(now.year, now.month, now.day)
        # print("Daily values reset successfully.")

def inc_value(self, valx : int = 0, measure: str = 'l'):
    try:
        if 'currentwaterintake' not in self.FinalData or self.FinalData['currentwaterintake'] == None or self.FinalData['currentwaterintake'] == '':
            self.FinalData['currentwaterintake'] = 0.00
        if 'currentpoints' not in self.FinalData or self.FinalData['currentpoints'] == None or self.FinalData['currentpoints'] == '':
            self.FinalData['currentpoints'] = 0.00
        if 'experiencepoints' not in self.userdata or self.userdata['experiencepoints'] == None or self.userdata['experiencepoints'] == '':
            self.userdata['experiencepoints'] = 0.00
        if measure == 'l':
            self.FinalData['currentwaterintake'] += valx
            self.FinalData['currentpoints'] += valx * 8
            self.userdata["experiencepoints"] += valx * 8 / 2
            # print("L")
        elif measure == 'ml':
            # print(int(valx / 1000 * 4))
            self.FinalData['currentwaterintake'] += valx / 1000
            self.FinalData['currentpoints'] += int(valx / 1000 * 16)
            self.userdata["experiencepoints"] += valx/ 1000 * 8
        update_userdata(self=self, userdata=self.userdata)
            # print("ML")
    except Exception as e:
        self.logger.error(f"Error in inc_value homepage: {e}")

def update_data(self):
    try:
        db = WD.Database()
        waterintakehistory_update(self=self)
        # print('Data updated')
        # print('FinalData ', self.FinalData)
        db.update_values(tablename='userstats', data=self.FinalData)
    except Exception as e:
        self.logger.error("Error update_data: inserting data into userstats table:", e)
    finally:
        db.close_connection()
        # print('updated successfully')

def waterintakehistory_update(self):        
    try:
        today = date.today().strftime("%m/%d/%Y")
        current_value : float = float(self.FinalData['currentwaterintake']) 
        daily_points : int = int(self.FinalData['dailypoints']) 
        current_points : int = int(self.FinalData['currentpoints'])
        drink_value : float = float(self.FinalData['dailyintakegoal']) 
        old_data_str = self.FinalData['waterintakehistory']
        if type(old_data_str) == str:
            old_data_dict = loads(old_data_str)
        elif type(old_data_str) == dict:
            old_data_dict = old_data_str
        else:
            old_data_dict = {}
        old_data_dict[today] = {
            "currentpoints": current_points,
            "dailypoints":daily_points,
            "drank": current_value,
            "drink": drink_value}    
        update_to_json = dumps(old_data_dict)            
        self.FinalData['waterintakehistory'] = update_to_json
    except Exception as e:
        self.logger.error("Error waterintakehistory_update: ",e)

def database_extractor(self, userdata: bool = False, userstats: bool = False, username: str = None, userid: str = None):
    if userdata and username:
        try: 
            db = WD.Database()
            userdata_from_db = db.get_values('userdata', username=username)
            db.close_connection()
        except Exception as e:
            self.logger.error(f"Error in database_extractor, {username}: {e}")
            return None
        
        if userdata_from_db:
            data = {
                "userid": userdata_from_db[0][0],
                "name": userdata_from_db[0][1],
                "username": userdata_from_db[0][2],
                "password": userdata_from_db[0][3],
                "dob": userdata_from_db[0][4],
                "gender": userdata_from_db[0][5],
                "email": userdata_from_db[0][6],
                "activity_level": userdata_from_db[0][7],
                "weight": userdata_from_db[0][8],
                "height": userdata_from_db[0][9],
                "register_time": userdata_from_db[0][10],
                'level': userdata_from_db[0][11],
                'experiencepoints': userdata_from_db[0][12],
                'lastlogin': userdata_from_db[0][13],
                'verificationcode': userdata_from_db[0][14],
                'verificationtime': userdata_from_db[0][15],
                'verifiedcode': userdata_from_db[0][16],
                'recoveryemail': userdata_from_db[0][17],
                'recoverycode': userdata_from_db[0][18]
            }
            return data
        else:
            # self.logger.info(f"No userdata found for {username}")
            return None
    
    elif userid and userstats:
        try: 
            db = WD.Database()
            userstats_from_db = db.get_values(tablename='userstats', userid=userid.strip())
            db.close_connection()
        except Exception as e:
            self.logger.error(f"Error in database_extractor, {userid}: {e}")
            return None
        
        if userstats_from_db:
            data = {
                'userid': userstats_from_db[0][0],
                'dailyintakegoal': userstats_from_db[0][1],
                'currentwaterintake': userstats_from_db[0][2],
                'dailypoints': userstats_from_db[0][3],
                'currentpoints': userstats_from_db[0][4],
                'waterintakehistory': userstats_from_db[0][5],
                'lastweightupdate': userstats_from_db[0][6],
                'lastheightupdate': userstats_from_db[0][7],
                'lastprofileupdate': userstats_from_db[0][8],
                'lastresettime': userstats_from_db[0][9]
            }
            return data
        else:
            data = {
                'userid': userid.strip(),
                'dailyintakegoal': 0,
                'currentwaterintake': 0,
                'dailypoints': 100,
                'currentpoints': 0,
                'waterintakehistory': None,
                'lastheightupdate': None,
                'lastweightupdate': None,
                'lastprofileupdate': None,
                'lastresettime': None
            }
            return data