import Adafruit_DHT

while True:
    humidity, temp = Adafruit_DHT.read_retry(11,11)
    print("Temp: {0:0.1f} C\n Humidity: {1:0.1f} %".format(temp, humidity))