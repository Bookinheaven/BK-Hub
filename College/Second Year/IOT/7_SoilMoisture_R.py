import RPi.GPIO as GPIO
import time

channel = 11
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

def callback(channel):
    if GPIO.input(channel) == 1:
        print("Water detected!")
    else:
        print("Water detected!")
        
GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)
GPIO.add_event_callback(channel, callback)

while True:
    time.sleep(0)
GPIO.cleanup()