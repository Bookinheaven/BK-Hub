import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

trigPin = 11
echoPin = 12
GPIO.setup(trigPin, GPIO.OUT)
GPIO.setup(echoPin, GPIO.IN)

try :
    while True:
        GPIO.output(trigPin, GPIO.LOW)
        time.sleep(2)
        GPIO.output(trigPin, GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(trigPin, GPIO.LOW)
        while GPIO.input(echoPin, GPIO.HIGH):
            startTime = time.time()
        while GPIO.input(echoPin, GPIO.LOW):
            bounceTime = time.time()
        pulseDuration = bounceTime - startTime
        distance = round(pulseDuration * 17150, 2)
        print("Distance: ", distance, " cm")
except Exception:
    print('Stopped!')
finally:
    GPIO.cleanup()
