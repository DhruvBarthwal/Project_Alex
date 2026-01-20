from typing import TypedDict

class AgentState(TypedDict, total=False):
    user_input : str
    intent : str
    email_id : str
    email_from : str
    email_subject : str
    email_body : str
    to : str
    
    pending_delete : bool
    
    
    