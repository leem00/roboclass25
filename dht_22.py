import time
import board
import adafruit_dht

# buat instance dari kelas adafruit_dht
# nama instance bebas, disini saya kasih nama dhtDevice
dhtDevice = adafruit_dht.DHT22(board.D17) # D17 Maksudnya GPIO 17

# btw, kalau ada yang nanya kenapa gak pake GPIO.setup(NOMOR PIN, TIPE_PIN)
# itu karena library DHT emang cara inisialisasi pinoutnya pake format board.D17

# looping terus sampe keyboard interrupt
while True:
    try:
        # inisialisasi variabel untuk simpan data
        temperature_c = dhtDevice.temperature # jadi dht22 di raspi cek suhu dalam celcius
        temperature_f = temperature_c * (9 / 5) + 32 # terus di konversi ke fahrenheit pake rumus. Kalau ditanya rumus reamur, saya lupa. cek aja di internet
        humidity = dhtDevice.humidity # ini fungsi dht buat cek kelembapan. tinggal panggil ya ges ya

        # Print hasilnya dalam format yang bersesuaian
        print("Temp: {:.1f} F / {:.1f} C    Humidity: {}% ".format(temperature_f, temperature_c, humidity)) # cetakkk

    # sedikit exception, untuk menangani error kalau misalnya sensor gak terbaca
    except RuntimeError as error:
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        dhtDevice.exit()
        raise error
    
    # sekarang kita bikin exception supaya kalau klik ctrl+c di terminal program bakal selesai
    # kemudian instance dht bakal dilupain raspi
    # kalau gak ada kode dibawah ini, pin DHT yang dipake sebelumnya bakal nyangkut
    except KeyboardInterrupt:
        print("kelarrrrrr") # kelarrrrrrrr
        dhtDevice.exit() # keluarin instance dht biar pin gak nyangkut
        break

    time.sleep(3) # dht 22 perlu waktu setidaknya minimal 2 detik agar optimal dalam pembacaan suhu dan kelempapan. di note ya ges ya!
