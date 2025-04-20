from influxdb import InfluxDBClient

client=InfluxDBClient(
    host="localhost",
    port=8086,
    database="sensor_data"
)

def store_sensor_data(temperature,humidity,pm25,aqi,smoke,no):

    try:
        data_point=[
            {
                "measurement": "sensor_readings",
                "fields": {
                    "temperature": temperature,
                    "humidity": humidity,
                    "pm25": pm25,
                    "aqi": aqi,
                    "smoke": smoke,
                    "no": no,
                },
            }
        ]

        client.write_points(data_point)

        print("Success")

    except Exception as e:
        print(e)
