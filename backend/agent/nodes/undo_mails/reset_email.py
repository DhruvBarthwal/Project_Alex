def reset_node(state):
    print("🔄 RESET NODE CALLED")

    state["awaiting_field"] = None
    state["sender_filter"] = None

    state["response"] = "Okay, I've reset the conversation. What would you like to do next?"
    return state
