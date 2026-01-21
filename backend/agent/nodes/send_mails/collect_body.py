def collect_body_node(state):
    
    print("📄 COLLECTING BODY")
    
    state["body"] = state["user_input"]
    state["awaiting_field"] = "confirm"
    state["intent"] = "SEND_EMAIL"
    state["response"] = "Do you want me to send this email now?"

    return state