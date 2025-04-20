from influxdb import InfluxDBClient

client = InfluxDBClient(
    host="localhost", 
    port=8086, 
    database="sensor_data"
    )

def get_daily_avg():
    query = '''
        SELECT 
            MEAN("pm25") AS "avg_pm25", 
            MEAN("aqi") AS "avg_aqi"
        FROM "sensor_readings"
        WHERE time >= now() - 1d
    '''
    
    result = client.query(query)
    points = list(result.get_points())

    if points:
        return points[0]  
    return None

def store_avg_daily_data():
    try:
        avg_values = get_daily_avg()

        if not avg_values:
            print("No data found for today.")
            return

        data_point = [
            {
                "measurement": "daily_readings",
                "fields": {
                    "pm25": avg_values["avg_pm25"],
                    "aqi": avg_values["avg_aqi"],
                },
            }
        ]

        client.write_points(data_point)
        print("successful")

    except Exception as e:
        print(f"Error {e}")

if __name__ == "__main__":
    store_avg_daily_data()
