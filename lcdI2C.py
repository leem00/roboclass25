### LCD I2C Raspi Code Version 2.0 ###

# import library
import RPi.GPIO as GPIO
from RPLCD.i2c import CharLCD
import time

# setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.cleanup()

# instantiate CharLCD object as lcd
lcd = CharLCD(i2c_expander = "PCF8574", address = 0x27, cols = 16, rows = 2) # i2C_expander itu jenis I2Cnya
lcd.backlight_enabled = False # turn off LCD backlight for 5 second
time.sleep(5)

# loop
try:
    lcd.backlight_enabled = True # turn on LCD backlight
    while True:
        lcd.clear(); # clear the LCD display
        lcd.cursor_pos = (0, 0) # set the LCD cursor
        lcd.write_string("Hello World") # write the string
        time.sleep(3)

        lcd.clear();
        lcd.cursor_pos = (1, 0)
        lcd.write_string("Im Ucim")
        time.sleep(3)
        
except KeyboardInterrupt:
    console.log("interuption")
finally:
    GPIO.cleanup()
