import sys
sys.path.append("PATH DIREKTORI LIBRARY BLYNK KAMU")
# misal "./blynk-library-python"

import BlynkLib
import RPi.GPIO as GPIO
import time

BLYNK_AUTH = 'AUTH TOKEN BLYNK ANDA'
blynk = BlynkLib.Blynk(BLYNK_AUTH)

# variabel GPIO sensor atau komponen anda
lampu = 16
infra = 21

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# set mode input atau output
GPIO.setup(lampu, GPIO.OUT)
GPIO.setup(infra, GPIO.IN)

try:
    
    # kode aktivasi komponen elektronik dari virtual pin Blynk
    @blynk.on("V5")
    def lampu_handler(value):  # menyalakan lampu (Nama fungsi bisa diganti)
        if int(value[0]) == 1:
            GPIO.output(lampu, GPIO.HIGH)
        else:
            GPIO.output(lampu, GPIO.LOW)

    while True:
        # run blynk agar terus terhubung
        blynk.run()  

        # input sensor 
        infraRead = GPIO.input(infra)

        # baca input sensor, kemudian upload ke virtual pin yang dituju
        blynk.virtual_write(1, infraRead)
        time.sleep(1)

except KeyboardInterrupt:
    print("Kelarrr")
finally:
    GPIO.cleanup()
