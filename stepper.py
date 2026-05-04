# import library
import RPi.GPIO as GPIO
import time

# setup
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# inisialisasi pin
in1 = 26
in2 = 13
in3 = 6
in4 = 5

# setup pinMode
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(in3, GPIO.OUT)
GPIO.setup(in4, GPIO.OUT)

# buat fungsi
def menyalaCW(delay):
    GPIO.output(in1, GPIO.HIGH)
    GPIO.output(in2, GPIO.LOW)
    GPIO.output(in3, GPIO.LOW)
    GPIO.output(in4, GPIO.LOW)
    time.sleep(delay);

    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.HIGH)
    GPIO.output(in3, GPIO.LOW)
    GPIO.output(in4, GPIO.LOW)
    time.sleep(delay);
    
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.LOW)
    GPIO.output(in3, GPIO.HIGH)
    GPIO.output(in4, GPIO.LOW)
    time.sleep(delay);
    
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.LOW)
    GPIO.output(in3, GPIO.LOW)
    GPIO.output(in4, GPIO.HIGH)
    time.sleep(delay);

# loop
try:
    while True:
        menyalaCW(2/1000)
except KeyboardInterrupt:
    print("interuption")
finally:
    print("Ended")
GPIO.cleanup()
