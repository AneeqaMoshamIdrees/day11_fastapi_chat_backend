"""
Day 11

Response Models

Author:
Aneeqa Mosham Idrees
"""

from pydantic import BaseModel


class ChatResponse(BaseModel):
    session_id: str
    response: str
    model: str