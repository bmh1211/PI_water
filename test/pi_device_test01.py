import RPi.GPIO as GPIO
import time
import requests

flag = True;

try:
    while True:

        if flag == False:
            res = requests.get('http://localhost:5000/btn_status/on', timeout=5)
            #print(res.text)
            time.sleep(1)
            flag = True

        else if flag == True:
            res = requests.get('http://localhost:5000/btn_status/off', timeout=5)
            #print(res.text)
            time.sleep(1)
            flag = False

except KeyboardInterrupt:
    GPIO.cleanup()