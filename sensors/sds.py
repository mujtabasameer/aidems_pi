from sds011lib import SDS011QueryReader

sensor = SDS011QueryReader('/dev/ttyUSB0')

def get_pm_values():
    try:
        sensor.base_reader.wake()

        aqi = sensor.query()

        if aqi:
            pm25 = aqi.pm25 
            return int(pm25)
        else:
            return 0

    except Exception:
        return 0

def calculate_aqi(pm25):
    breakout_points=[
        (0,12.0,0,50),
        (12.1,35.4,51,100),
        (35.5,55.4,101,150),
        (55.5,150.4,151,200),
        (150.5,250.4,201,300),
        (250.5,350.4,301,400),
        (350.5,500.4,401,500)
    ]

    for c_low,c_high,i_low,i_high in breakout_points:
        if c_low<=pm25<=c_high:
            aqi=((i_high-i_low)/(c_high-c_low))*(pm25-c_low)+i_low
            return round(aqi)


def stop_sensor():
    sensor.sleep()
    return
