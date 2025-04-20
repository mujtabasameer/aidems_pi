import time
from sensors.dht import get_temp_humid
from sensors.mq2 import get_smoke_level
from sensors.sds import get_pm_values
from sensors.sds import stop_sensor
from sensors.sds import calculate_aqi
from database.storedata import store_sensor_data
from Firebase.check_metrics import notification
try:
    
    while True:
        temperature, humidity = get_temp_humid()
        smoke_level=get_smoke_level()
        pm25=get_pm_values()
        aqi=calculate_aqi(pm25)
        NO="None"

        if temperature is not None and humidity is not None:
            store_sensor_data(temperature,humidity,pm25,aqi,smoke_level,NO)
            notification(aqi,smoke_level,NO)

        else:
            print("Failed to read sensor data")
        time.sleep(30)

except KeyboardInterrupt:
    stop_sensor()
