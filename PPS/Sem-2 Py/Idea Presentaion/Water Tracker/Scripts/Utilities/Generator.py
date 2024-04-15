from time import time
from random import randint
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import requests
import datetime
Assets = os.path.dirname(__file__).replace(r'Scripts\Utilities', 'Assets')

class UserIDGenerator:
    def __init__(self, prefix='BK'):
        self.prefix = prefix

    def generate_user_id(self):
        timestamp = int(time() ** 1/9) 
        random_2_digits = randint(0, 99) 
        user_id = f"{self.prefix}{timestamp}{random_2_digits:02d}"
        return user_id

class VerifyCodeGenerator:
    @staticmethod
    def generate_code():
        random_6_digits = randint(0, 999999)
        code = f"{random_6_digits:06d}"
        return code

class EmailSender:
    def check_internet_connection(self):
        try:
            response = requests.get('https://www.google.com', timeout=5)
            response.raise_for_status()
            # print('Internet there')
            return True
        except requests.RequestException as e:
            print(e)
            # print('No Internet')
            return False
        
    def __init__(self, sender_mail='burnknuckle.loop@gmail.com', receiver_mail=None, mode=None, app=None):
        if app:
            self.logger = app.logger
        self.sender_email = sender_mail
        self.receiver_email = receiver_mail
        self.password = "amsu glyw vomf dkam"
        if mode == 'verify':
            self.verify_code = VerifyCodeGenerator.generate_code()
            self.message_subject = f"Verification Code: [{self.verify_code}]"
            self.message = self.__load_email_template(self, name='verify')

        elif mode == 'welcome':
            self.message = self.__load_email_template(self, name='welcome')
            self.message_subject = f"Welcome to our App!"

    def get_code(self):
        if self.verify_code:
            return self.verify_code
    @staticmethod
    def __load_email_template(self, name):
        if name == 'verify':
            file_path = os.path.join(Assets, "html", "verifycode.html")
        if name == 'welcome':
            file_path = os.path.join(Assets, "html", "welcome.html")
        # self.logger.info(file_path)

        with open(file=file_path, mode="r") as file:
            template_content = file.read()
            if name == 'verify':
                template_content = template_content.replace('{', '{{').replace('}', '}}').replace('<strong></strong>', '<strong>{}</strong>')
                return template_content.format(self.verify_code)
            else:
                return template_content

    def send_email(self):
        try:
            self.check_internet_connection()
            message = MIMEMultipart()
            message['From'] = self.sender_email
            message['To'] = self.receiver_email
            message['Subject'] = self.message_subject

            message.attach(MIMEText(self.message, 'html'))
            try: 
                with smtplib.SMTP('smtp.gmail.com', 587) as server:
                    server.starttls()
                    server.login(self.sender_email, self.password)
                    server.sendmail(self.sender_email, self.receiver_email, message.as_string())
            except smtplib.SMTPConnectError:
                self.logger.info('Internet Connection Error!')
            except smtplib.SMTPException:
                self.logge.error("SMTP: Error in send_email")

            except Exception as e:
                return e
                
            # self.logger.info("send_email: Message sent successfully!")

        except Exception as e:
            self.logger.error("Error in send_email: unable to send email:", e)

class WaterIntake:
    def __init__(self, userdata, userstats):
        self.userdata = userdata
        self.userstats = userstats
    def set_userstats(self):
        if self.userstats is None or 'currentwaterintake' not in self.userstats or self.userstats['currentwaterintake'] == '' or self.userstats['currentwaterintake'] == 0:
            self.userstats['currentwaterintake'] = 0.00
        if self.userstats is None or 'dailypoints' not in self.userstats or self.userstats['dailypoints'] == '' or self.userstats['dailypoints'] == 0:
            self.userstats['dailypoints'] = 100
        if self.userstats is None or 'currentpoints' not in self.userstats or self.userstats['currentpoints'] == '' or self.userstats['currentpoints'] == 0:
            self.userstats['currentpoints'] = 0
        if self.userstats is None or 'dailyintakegoal' not in self.userstats or self.userstats['dailyintakegoal'] == '' or self.userstats['dailyintakegoal'] == 0:
            self.userstats['dailyintakegoal'] = round(float(self.NeedtoDrink()), 2)
        # print(self.userstats)
        return self.userstats
    def water_formula(self):
        gender = self.userdata['gender'].strip()
        weight = self.userdata['weight']
        activity_level = self.userdata['activity_level']
       
        if gender == 'Male':
            base_intake = weight * 0.035
            base_intake = round(base_intake,2)
        elif gender == 'Female':
            base_intake = weight * 0.035
            base_intake = round(base_intake,2)
       
        if activity_level == 'Low Level':
            intake_adder = 0
        elif activity_level == 'Medium Level':
            intake_adder = 0.5
        elif activity_level == 'High Level':
            intake_adder = 1.0
       
        recommended_intake = base_intake + intake_adder
       
        return recommended_intake
    
    def NeedtoDrink(self):
        recommended_intake = self.water_formula()
        return recommended_intake


if __name__ == '__main__':
    data = {'name': 'tanvik123', 'username': 'tanvik123', 'password': 'tanvik123', 'dob': datetime.date(2005, 3, 1), 'gender': 'Male      ', 'email': 'tanvik123', 'activity_level': 'Medium Level', 'weight': 90, 'height': 20, 'register_time': datetime.datetime(2024, 3, 9, 21, 54, 34, 979568)}
    water_intake = WaterIntake(data)
    water_intake.NeedtoDrink()