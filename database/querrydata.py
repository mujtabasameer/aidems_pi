from influxdb import InfluxDBClient

client=InfluxDBClient(
    host="localhost",
    port=8086,
    database="sensor_data"
)


def querry_sensor_data():
    try:
        query='SELECT * FROM "sensor_readings"'

        result=client.query(query)

        if result:
            for point in result.get_points():
                print(f" Time: {point['time']}, Temperature: {point['temperature']}, "
                      f"Humidity: {point['humidity']}, PM2.5: {point['pm25']}, "
                      f"AQI: {point['aqi']}, Smoke: {point['smoke']}, NO: {point['no']}")
        else:
            print("data not found")

    except Exception as e:
        print(e)

        
querry_sensor_data()