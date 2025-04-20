from Adafruit_ADS1x15 import ADS1115

adc = ADS1115(address=0x48, busnum=1)
GAIN = 1

MQ2_channel = 1

ADC_MAX = 32767.0  
V_REF = 4.096     

clean_air_voltage = 0.24 

no_smoke_threshold = 0.40  
mild_smoke_threshold = 0.90  
high_smoke_threshold = 1.5  

def read_sensor():
    raw_adc_value = adc.read_adc(MQ2_channel, gain=GAIN)

    vol = raw_adc_value * (V_REF / ADC_MAX)
    return vol

def get_smoke_level():
    
    vol = read_sensor()

    if vol <= no_smoke_threshold:
        return "None"
    elif vol <= mild_smoke_threshold:
        return "Mild"
    else:
        return "High"
