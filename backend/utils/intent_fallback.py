def fallback_intent(text: str) -> str:
    text = text.lower()

    # 🔴 CONFIRM MUST COME FIRST
    if any(k in text for k in ["confirm", "yes", "send it", "go ahead", "okay send"]):
        return "CONFIRM_SEND"

    if any(k in text for k in ["delete", "remove", "trash", "discard"]):
        return "DELETE_EMAIL"

    if any(k in text for k in ["send email", "write email", "compose", "new mail"]):
        return "CREATE_EMAIL"

    if any(k in text for k in ["read", "open", "check", "show", "inbox"]):
        return "READ_EMAIL"

    return "UNKNOWN"
