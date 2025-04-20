from influxdb import InfluxDBClient
from typing import List

client = InfluxDBClient(
    host="localhost", 
    port=8086,
    database="sensor_data"
)

def get_latest_sensor_data():

    query = f'SELECT * FROM "sensor_readings" ORDER BY time DESC LIMIT 1'
    result = client.query(query) 
    
    points = list(result.get_points())
    if not points:
        return [] 
    
    json = points[0]
    
    if 'time' in json:
        del json['time']

    return json

def get_historical_sensor_data():
    query = f'SELECT * FROM "daily_readings" ORDER BY time DESC LIMIT 7'
    result=client.query(query)

    points = list(result.get_points())
    if not points:
        return []
    
    json = points
    for point in json:
        if 'time' in point:
            del point['time']

    return json
