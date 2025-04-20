from Firebase.firebase_sender import send_notification, store_alerts
import time

cooldown_time=3600
last_aqi_alert = None
last_smoke_alert = None
last_no_alert = None

def notification(aqi,smoke_level,NO):
    global last_aqi_alert, last_smoke_alert, last_no_alert
    current_time = time.time()
    if last_aqi_alert is None or current_time-last_aqi_alert>cooldown_time:
        if aqi>=150 and aqi<=200:
            send_notification("AQI Alert", f"Unhealthy AQI: {aqi}. Stay indoors!")
            last_aqi_alert=current_time
            store_alerts("AQI Alert", "High AQI Detected!", aqi)
        elif 200 <= aqi < 300:
            send_notification("AQI Alert", f"Very Unhealthy AQI: {aqi}. Stay indoors!")
            last_aqi_alert=current_time
            store_alerts("AQI Alert", "High AQI Detected!", aqi)
        elif 300 <= aqi < 400:
            send_notification("AQI Alert", f"Hazardous AQI: {aqi}. Emergency conditions!")
            last_aqi_alert=current_time
            store_alerts("AQI Alert", "High AQI Detected!", aqi)
        elif aqi >= 400:
            send_notification("AQI Alert", f"Severe Hazard! AQI: {aqi}. Health emergency!")
            last_aqi_alert=current_time
            store_alerts("AQI Alert", "High AQI Detected!", aqi)

    if last_smoke_alert is None or current_time-last_smoke_alert>cooldown_time:
        if smoke_level == "Mild":
            send_notification("Smoke Alert", "Mild smoke detected. Air quality may be affected.")
            last_smoke_alert=current_time
            store_alerts("Smoke Alert", "Smoke Detected!", smoke_level)
        elif smoke_level == "High":
            send_notification("Smoke Alert", "High smoke levels detected! Reduce exposure.")
            last_smoke_alert=current_time
            store_alerts("Smoke Alert", "Smoke Detected!", smoke_level)

    if last_no_alert is None or current_time-last_no_alert>cooldown_time:
        if NO == "Mild":
            send_notification("NO Alert", "Mild nitrogen oxide levels detected. Be cautious.")
            last_no_alert=current_time
            store_alerts("NO Alert", "NO Detected!", NO)
        elif NO == "High":
            send_notification("NO Alert", "High NO levels detected! Potential health risk.")
            last_no_alert=current_time
            store_alerts("NO Alert", "NO Detected!", NO)