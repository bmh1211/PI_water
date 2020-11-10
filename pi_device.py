import RPi.GPIO as GPIO
import time
import requests

GPIO.setmode(GPIO.BCM)

GPIO.setup(6, GPIO.OUT)
GPIO.setup(21, GPIO.IN)

try:
    while True:
        inputIO = GPIO.input(21)

        if inputIO == False:
            GPIO.output(6, GPIO.HIGH)
            res = requests.get('http://localhost:5000/btn_status/on', timeout=5)
            #print(res.text)
            time.sleep(1)

        else:
            GPIO.output(6, GPIO.LOW)
            res = requests.get('http://localhost:5000/btn_status/off', timeout=5)
            #print(res.text)
            time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()