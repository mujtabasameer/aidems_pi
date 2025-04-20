import firebase_admin
from firebase_admin import credentials, messaging

creds=credentials.Certificate("/home/pi/Desktop/fyp/Firebase/key/aidems-firebase-adminsdk-fbsvc-08b2271e91.json")
firebase_admin.initialize_app(creds)

def send_notification(title, message):
    notification = messaging.Message(
        notification = messaging.Notification(
            title=title,
            body=message
        ),
        topic="alerts"
    )

    response = messaging.send(notification)

send_notification("aa","bb")