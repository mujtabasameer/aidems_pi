from influxdb import InfluxDBClient
from datetime import datetime, timedelta, timezone

client = InfluxDBClient(
    host="localhost", 
    port=8086, 
    database="sensor_data"
    )

def get_today_avg():
    today = datetime.now(timezone.utc).date()
    start_time = datetime.combine(today, datetime.min.time(), tzinfo=timezone.utc)
    end_time = datetime.now(timezone.utc)

    start_time_str = start_time.isoformat() 
    end_time_str = end_time.isoformat()
    
    query = f'''
        SELECT 
            MEAN("pm25") AS "avg_pm25", 
            MEAN("aqi") AS "avg_aqi"
        FROM "sensor_readings"
        WHERE time >= '{start_time_str}' AND time <= '{end_time_str}'
    '''
    
    result = client.query(query)
    points = list(result.get_points())

    print(f"Query result: {points}")

    if points:
        return points[0]  
    return None

def store_avg_daily_data():
    try:
        avg_values = get_today_avg()

        if not avg_values:
            print("No data found for today.")
            return
        
        today_date = datetime.now(timezone.utc).date().strftime("%Y-%m-%d")
        timestamp = f"{today_date}T00:00:00Z" 

        data_point = [
            {
                "measurement": "daily_readings",
                "time": timestamp,
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
