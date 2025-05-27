import RPi.GPIO as GPIO
import time

# Definisi pin untuk rotary encoder
CLK_PIN = 18    # Pin CLK (clock) dari rotary encoder
DT_PIN = 15     # Pin DT (data) dari rotary encoder
SW_PIN = 14     # Pin tombol (switch) dari rotary encoder

# Konstanta arah putaran
DIRECTION_CW = 0     # Clockwise (searah jarum jam)
DIRECTION_CCW = 1    # Counter-clockwise (berlawanan arah jarum jam)

# Variabel untuk menyimpan jumlah putaran dan arah
counter = 0
direction = DIRECTION_CW

# Variabel untuk menyimpan status pin CLK
CLK_state = 0
prev_CLK_state = 0

# Status tombol rotary encoder
button_pressed = False
prev_button_state = GPIO.HIGH  # Tombol tidak ditekan (karena pull-up)

# Konfigurasi mode GPIO menggunakan penomoran BCM
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Konfigurasi pin-pin input
GPIO.setup(CLK_PIN, GPIO.IN)
GPIO.setup(DT_PIN, GPIO.IN)
GPIO.setup(SW_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Tombol menggunakan pull-up resistor internal

# Baca status awal dari pin CLK
prev_CLK_state = GPIO.input(CLK_PIN)

try:
    while True:
        # Baca status CLK saat ini
        CLK_state = GPIO.input(CLK_PIN)

        # Jika terjadi perubahan pada pin CLK dari LOW ke HIGH
        if CLK_state != prev_CLK_state and CLK_state == GPIO.HIGH:
            # Baca pin DT untuk menentukan arah putaran
            if GPIO.input(DT_PIN) == GPIO.HIGH:
                counter -= 1
                direction = DIRECTION_CCW  # Berputar ke kiri
            else:
                counter += 1
                direction = DIRECTION_CW   # Berputar ke kanan

            # Tampilkan arah dan jumlah putaran
            print("Rotary Encoder:: direction:", "CLOCKWISE" if direction == DIRECTION_CW else "ANTICLOCKWISE",
                  "- count:", counter)

            time.sleep(0.5)  # Delay untuk menghindari bouncing

        # Simpan status CLK untuk perbandingan di iterasi berikutnya
        prev_CLK_state = CLK_state

        # Baca status tombol
        button_state = GPIO.input(SW_PIN)

        # Jika status tombol berubah (ditekan atau dilepas)
        if button_state != prev_button_state:
            time.sleep(0.01)  # Debounce delay 10ms
            if button_state == GPIO.LOW:
                print("The button is pressed")
                button_pressed = True
            else:
                button_pressed = False

        # Simpan status tombol saat ini untuk pengecekan berikutnya
        prev_button_state = button_state

# Jika program dihentikan dengan Ctrl+C, bersihkan konfigurasi GPIO
except KeyboardInterrupt:
    GPIO.cleanup()
