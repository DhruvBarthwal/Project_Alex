def collect_subject_node(state):
    
    print("📝 COLLECTING SUBJECT")
    
    state["subject"] = state["user_input"]
    state["awaiting_field"] = "body"
    state["intent"] = "COLLECT_BODY"
    state["response"] = "Okay. What should the email say?"
    
    return state