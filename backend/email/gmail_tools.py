import base64
from email.message import EmailMessage

def read_latest_email(service):
    msgs = service.users().messages().list(userID = "me", maxResult = 1).execute()
    msg_id = msgs["message"][0]["id"]
    msg = service.users().messages().get(userId = "me", id = msg_id).execute()
    return msg

def delete_email(service, msg_id):
    service.users().message().delete(userId="me", id = msg_id).execute()
    
def send_email(service, to , subject, body):
    message = EmailMessage()
    message.set_content(body)
    message["To"] = to
    message["Subject"] = subject
    
    encoded = base64.urlsafe_b64encode(message.as_bytes()).decode()
    service.users().messages().send(
        userId = "me",
        body = {"raw" : encoded}
    ).execute()