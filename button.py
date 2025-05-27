import RPi.GPIO as GPIO
import time

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Loop utama
while True:
    button_state = GPIO.input(17)
    if button_state == False:
        print('Button Pressed...')
        time.sleep(1)
