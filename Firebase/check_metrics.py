from firebase_sender import send_notification

def notification(aqi,smoke_level,NO):
    if aqi>=150 and aqi<=200:
        send_notification("AQI Alert", f"Unhealthy AQI: {aqi}. Stay indoors!")
    elif 200 <= aqi < 300:
        send_notification("AQI Alert", f"Very Unhealthy AQI: {aqi}. Stay indoors!")
    elif 300 <= aqi < 400:
        send_notification("AQI Alert", f"Hazardous AQI: {aqi}. Emergency conditions!")
    elif aqi >= 400:
        send_notification("AQI Alert", f"Severe Hazard! AQI: {aqi}. Health emergency!")


    if smoke_level == "Mild":
        send_notification("Smoke Alert", "Mild smoke detected. Air quality may be affected.")
    elif smoke_level == "High":
        send_notification("Smoke Alert", "High smoke levels detected! Reduce exposure.")


    if NO == "Mild":
        send_notification("NO Alert", "Mild nitrogen oxide levels detected. Be cautious.")
    elif NO == "High":
        send_notification("NO Alert", "High NO levels detected! Potential health risk.")