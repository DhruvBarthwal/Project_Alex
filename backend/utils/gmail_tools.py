import base64
from email.message import EmailMessage


def read_latest_email(service):
    """
    Returns:
        {
            "id": msg_id,
            "from": sender,
            "subject": subject,
            "body": body
        }
    """

    # 1️⃣ Get latest email ID
    msgs = service.users().messages().list(
        userId="me",
        maxResults=1,
        labelIds=["INBOX"]
    ).execute()

    messages = msgs.get("messages", [])
    if not messages:
        return None

    msg_id = messages[0]["id"]

    # 2️⃣ Get full email
    msg = service.users().messages().get(
        userId="me",
        id=msg_id,
        format="full"
    ).execute()

    headers = msg["payload"].get("headers", [])

    sender = ""
    subject = ""

    for h in headers:
        if h["name"] == "From":
            sender = h["value"]
        elif h["name"] == "Subject":
            subject = h["value"]

    # 3️⃣ Extract email body
    body = ""

    payload = msg["payload"]

    if "parts" in payload:
        for part in payload["parts"]:
            if part["mimeType"] == "text/plain":
                data = part["body"].get("data")
                if data:
                    body = base64.urlsafe_b64decode(data).decode("utf-8")
                    break
    else:
        data = payload["body"].get("data")
        if data:
            body = base64.urlsafe_b64decode(data).decode("utf-8")

    return {
        "id": msg_id,
        "from": sender,
        "subject": subject,
        "body": body.strip()
    }


def delete_email(service, msg_id):
    service.users().messages().delete(
        userId="me",
        id=msg_id
    ).execute()


def send_email(service, to, subject, body):
    message = EmailMessage()
    message.set_content(body)
    message["To"] = to
    message["Subject"] = subject

    encoded = base64.urlsafe_b64encode(
        message.as_bytes()
    ).decode()

    service.users().messages().send(
        userId="me",
        body={"raw": encoded}
    ).execute()
