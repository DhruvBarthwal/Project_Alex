def collect_to_node(state):
    
    print("📬 COLLECTING TO")
    
    state["to"] = state["user_input"]
    state["awaiting_field"] = "subject"
    state["intent"] = "COLLECT_SUBJECT"
    state["response"] = "Got it. What is the subject of the email?"

    return state