from RPLCD.i2c import CharLCD
import time

# inisialisasi instance (ALAMAT LCD jangan lupa diganti)
lcd = CharLCD('PCF8574', ALAMAT LCD)
lcd.backlight_enabled = False # mati nyalain backlit lcd

while True:
    try:
      # clear display dulu
      # supaya gak ada print lcd program lalu yang nyangkut
      lcd.clear()
  
      lcd.write_string('Hello, World!') # tulis
      time.sleep(2)  # tidur
  
      lcd.crlf()  # geser ke baris 2
      lcd.write_string('Raspi + LCD') # tulis
      time.sleep(5)  # nunggu
  
      lcd.clear()  # clear lagi
      lcd.write_string('Goodbye!') # sayonara
      time.sleep(2) # tidur
    except KeyboardInterrupt:
      print("kelarrrrrr")
      lcd.close() # tutup instance lcd. penting banget dilakuin
      break # usir dari loop

# setelah selesai, 
lcd.backlight_enabled = False # oke ges ya, dah tau kan?
lcd.close() # tau kan buat apa?
