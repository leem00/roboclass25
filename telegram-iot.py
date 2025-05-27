import telepot
from telepot.loop import MessageLoop
import RPi.GPIO as GPIO
from time import sleep 

# dipercobaan ini saya pake led dan sensor inframerah. 
# sesuaikan aja ya ges ya pin sama komponennya!
led = 15
cek = 14

# variabel state dari sensor
kondisi = ""

# biasa lah ya
GPIO.setmode(GPIO.BCM)      
GPIO.setwarnings(False)
GPIO.setup(led, GPIO.OUT) 
GPIO.setup(cek, GPIO.IN) 

# nah, ini kode buat handle input dari telegram
def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    # ini buat print command yang diterima telegram ke raspi
    print ('Received:')
    print(command)

    # ini buat custom isi respon dari telegramnya mau diapain
    # gak usah diajarin kan ya cara nyalain lampu sama baca sensor?
    # lengkapnya pahamin sendiri aja ya!
    if command == '/hi':
        bot.sendMessage (chat_id, str("Hi! Ucim\nSaatnya mulai program dengan bismillah"))
    elif command == '/bismillah':
        bot.sendMessage (chat_id, str("Command Tersedia:\n/led_1 = menyalakan lampu\n" + 
        "/led_0 = mematikan lampu\n" + "/state = cek sensor"))
    elif command == '/led_1':
        bot.sendMessage(chat_id, str("Lampu nyala, terang"))
        GPIO.output(led, True)
    elif command == '/led_0':
        bot.sendMessage(chat_id, str("Lampu mati, innalillahi"))
        GPIO.output(led, False)
    elif command == '/state':
        if GPIO.input(cek) == 1:
            kondisi = "Aman aja"
        else:
            kondisi = "Ada objek terdeteksi!"
        bot.sendMessage(chat_id, str("Keadaan saat ini : {}").format(kondisi))
    else:
        bot.sendMessage(chat_id, str("Plisss deh, \nkeyword itu kagak ada di list perintah" + 
        "Kalau mau cek listnya, coba aja ketik /bismillah deh!"))

# Masukkin token telegram anda disini ya!
bot = telepot.Bot('TOKEN BOT TELEGRAM ANDA MASING-MASING')
print (bot.getMe())

# pokoknya ini mulai telegram
MessageLoop(bot, handle).run_as_thread()
print ('Listening....')

while 1:
    sleep(10)
