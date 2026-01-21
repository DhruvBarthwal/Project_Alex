from utils.gmail_auth import get_gmail_service
from utils.gmail_tools import send_email

def send_email_node(state):
    
    print("SENDING EMAIL")
    
    service = get_gmail_service()
    
    send_email(
        service,
        to=state["to"],
        subject=state["subject"],
        body=state["body"],
    )
    
    state["awaiting_field"] = None
    state["to"] = None
    state["subject"] = None
    state["body"] = None

    state["response"] = "Your email has been sent successfully."

    return state