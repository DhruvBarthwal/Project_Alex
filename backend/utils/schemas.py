from pydantic import BaseModel
from typing import Optional

class VoiceInput(BaseModel):
    text : str
    email_id : Optional[str] = None