from pydantic import BaseModel
from typing import Optional, Dict, Any

class VoiceInput(BaseModel):
    text : str
    email_id : Optional[str] = None
    state : Optional[Dict[str,Any]] = None
    
    to: Optional[str] = None
    subject: Optional[str] = None
    body: Optional[str] = None