def compose_email_node(state):
    
    print("✉️ COMPOSE EMAIL STARTED")
    
    state["to"] = None
    state["subject"] = None
    state["body"] = None

    state["awaiting_field"] = "to"
    state["intent"] = "COLLECT_TO"
    state["response"] = "Sure. Who do you want to send the email to?"

    return state