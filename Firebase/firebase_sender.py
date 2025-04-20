import firebase_admin
from firebase_admin import credentials, messaging, db
from datetime import datetime

creds=credentials.Certificate("/home/pi/Desktop/fyp/Firebase/key/aidems-firebase-adminsdk-fbsvc-08b2271e91.json")
firebase_admin.initialize_app(creds, {
    'databaseURL': 'https://aidems-default-rtdb.firebaseio.com'
})

def send_notification(title, message):
    notification = messaging.Message(
        notification = messaging.Notification(
            title=title,
            body=message
        ),
        topic="alerts"
    )

    response = messaging.send(notification)

def store_alerts(title, text, value):
    ref = db.reference("alerts")
    ref.push({
        "title": title,
        "text": text,
        "value": value,
        "timestamp": datetime.now().isoformat()
    })
