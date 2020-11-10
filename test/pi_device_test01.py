import time
import requests
import sys

flag = True;
interval_timer = 5;

try:
    while True:

        if flag == False:
            res = requests.get('http://localhost:5000/btn_status/on', timeout=5)
            #print(res.text)
            time.sleep(interval_timer)
            flag = True

        elif flag == True:
            res = requests.get('http://localhost:5000/btn_status/off', timeout=5)
            #print(res.text)
            time.sleep(interval_timer)
            flag = False

except KeyboardInterrupt:
    print("terminate system")
    sys.exit()

except Exception as e:
    print(e)