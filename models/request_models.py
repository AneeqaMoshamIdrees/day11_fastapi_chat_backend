"""
Day 11

Request Models

Author:
Aneeqa Mosham Idrees
"""

from pydantic import BaseModel


class ChatRequest(BaseModel):
    session_id: str
    message: str