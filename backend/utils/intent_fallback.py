def fallback_intent(text: str) -> str:
    text = (text or "").lower().strip()

    if any(k in text for k in ["confirm", "yes", "send it", "go ahead", "okay"]):
        return "CONFIRM_SEND"

    if any(k in text for k in ["delete", "remove", "trash", "discard"]):
        return "DELETE_EMAIL"

    if any(k in text for k in ["create","write", "compose", "send", "send mail", "send email", "compose email"]):
        return "COMPOSE_EMAIL"

    if any(k in text for k in ["read", "open", "check", "show", "inbox"]):
        return "READ_EMAIL"
    
    return "UNKNOWN"
