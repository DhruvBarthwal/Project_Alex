def delete_email_node(state):
    
    print("➡️ DELETE_EMAIL FLOW HIT")
    
    if not state.get("email_id"):
        
        print("❌ NO EMAIL_ID — CANNOT DELETE")
        
        state["response"] = "No email selected to delete"
        return state
    
    print("✅ EMAIL_ID PRESENT — ASKING CONFIRMATION")
    state["response"] = "Are you sure you want to delete this email?"
    return state