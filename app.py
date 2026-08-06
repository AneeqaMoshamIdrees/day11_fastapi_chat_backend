"""
Day 11

FastAPI Backend

Author:
Aneeqa Mosham Idrees
"""

from fastapi import FastAPI

from models.request_models import ChatRequest
from models.response_models import ChatResponse
from fastapi import HTTPException
from services.logger import logger
import time 
import traceback

# import session manager functions

from services.session_manager import (
    create_session,
    add_user_message,
    add_assistant_message,
    get_history,
    get_all_sessions
)

# import generate_reply function from gemini_service

from services.gemini_service import generate_reply



app = FastAPI(
    title="AI Chat Backend",
    description="Day 11 FastAPI Chat Server",
    version="1.0.0"
)

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(

    CORSMiddleware,

    allow_origins=["http://localhost:5173"],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],

)

@app.get("/")
def home():
    return {
        "message": "Welcome to Day 11 FastAPI Backend!"
    }


@app.post("/api/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    if request.message.strip() == "":
        raise HTTPException(
            status_code=400,
            detail="Message cannot be empty."
        )

    try:

        create_session(request.session_id)

        add_user_message(
            request.session_id,
            request.message
        )

        history = get_history(request.session_id)

        start = time.time()
        reply = generate_reply(history)
        latency = round(time.time() - start, 3)

        add_assistant_message(
            request.session_id,
            reply
        )

        logger.info(
           f"timestamp={time.strftime('%Y-%m-%d %H:%M:%S')} | "
           f"session_id={request.session_id} | "
           f"model=gemini-3.6-flash-lite | "
           f"user_prompt='{request.message}' | "
           f"latency_ms={latency * 1000}"
        )
        return ChatResponse(
            session_id=request.session_id,
            response=reply,
            model="gemini-3.6-flash-lite"
        )

    except Exception as e:
        traceback.print_exc()
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

@app.get("/api/sessions")
def sessions():

    data = get_all_sessions()

    if len(data) == 0:

        raise HTTPException(

            status_code=404,

            detail="No active chat sessions."

        )

    result = []

    for session_id, history in data.items():

        result.append({

            "session_id": session_id,

            "messages": len(history)

        })

    return result