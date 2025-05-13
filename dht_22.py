import time
import board
import adafruit_dht

# buat instance dari kelas adafruit_dht
# nama instance bebas, disini saya kasih nama dhtDevice
dhtDevice = adafruit_dht.DHT22(board.D17)

while True:
    try:
        # inisialisasi variabel untuk simpan data 
        temperature_c = dhtDevice.temperature
        temperature_f = temperature_c * (9 / 5) + 32
        humidity = dhtDevice.humidity

        # Print hasilnya dalam format yang bersesuaian
        print(
            "Temp: {:.1f} F / {:.1f} C    Humidity: {}% ".format(
                temperature_f, temperature_c, humidity
            )
        )

    # sedikit exception, untuk menangani error kalau misalnya sensor gak terbaca
    except RuntimeError as error:
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        dhtDevice.exit()
        raise error

    time.sleep(2.0)
