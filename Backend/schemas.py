
from pydantic import BaseModel
from datetime import datetime

class ChatRequest(BaseModel):
    prompt: str

class ChatResponse(BaseModel):
    response: str
    timestamp: datetime
