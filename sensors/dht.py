import adafruit_dht
import board

dht_sensor = adafruit_dht.DHT11(board.D17)

def get_temp_humid():
    try:
        temperature_c = dht_sensor.temperature
        humidity = dht_sensor.humidity

        if humidity is not None and temperature_c is not None:
            return int(temperature_c), int(humidity)
        else:
            return 0, 0
    except RuntimeError as error:
        return 0, 0


