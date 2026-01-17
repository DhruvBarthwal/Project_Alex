from pydantic import BaseModel

class VoiceInput(BaseModel):
    text : str