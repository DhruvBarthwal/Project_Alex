from utils.gmail_tools import read_latest_email
from utils.gmail_auth import get_gmail_service

def read_email_node(state):
    service = get_gmail_service()
    email = read_latest_email(service)
    
    if not email:
        state['email_body'] = "Inbox is empty."
        return state
    
    state["email_id"] = email["id"]
    state["email_from"] = email["from"]
    state["email_subject"] = email["subject"]
    state["email_body"] = email["body"]
    
    print("READ NODE EMAIL_ID:", email["id"])
    
    return state