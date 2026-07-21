from pydantic import BaseModel
from datetime import datetime



class ChatRequest(BaseModel):

    question: str



class ChatResponse(BaseModel):

    question: str

    answer: str

    sources: list | None = None

    created_date: datetime | None = None