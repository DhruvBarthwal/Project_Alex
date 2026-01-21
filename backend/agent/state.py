from typing import TypedDict, Optional, List

class AgentState(TypedDict, total=False):
    user_input : str
    intent : str
    
    #email reading
    email_id : str
    email_from : str
    email_subject : str
    email_body : str
    
    #email composing
    to : Optional[str]
    subject : Optional[str]
    body : Optional[str]
    attachments : Optional[List[str]]
    awaiting_field : Optional[str]  # stores the previous question asked
        
    response: str
    
    
    