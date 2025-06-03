import sys
sys.path.append("./blynk-library-python")

import BlynkLib
import RPi.GPIO as GPIO
import time

BLYNK_AUTH = 'zC44GTm_BmjJQEOKysPvBvksb31myuaX'
blynk = BlynkLib.Blynk(BLYNK_AUTH)

lampu = 16
infra = 21

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(lampu, GPIO.OUT)
GPIO.setup(infra, GPIO.IN)

try:
    # activate electronic
    @blynk.on("V5")
    def led1_handler(value):
        if int(value[0]) == 1:
            GPIO.output(lampu, GPIO.HIGH)
        else:
            GPIO.output(lampu, GPIO.LOW)

    while True:
        blynk.run()
        infraRead = GPIO.input(infra)
        blynk.virtual_write(1, infraRead) # read sensor data
        time.sleep(1)

except KeyboardInterrupt:
    print("Kelarrr")
finally:
    GPIO.cleanup()
