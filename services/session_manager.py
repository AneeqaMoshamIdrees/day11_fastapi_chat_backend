"""
Day 11

Session Manager

Author:
Aneeqa Mosham Idrees
"""

chat_sessions = {}

SYSTEM_PROMPT = """
You are a helpful AI assistant.
Answer clearly and politely.
"""

def create_session(session_id: str):

    if session_id not in chat_sessions:

        chat_sessions[session_id] = [

            {

                "role": "system",

                "content": SYSTEM_PROMPT

            }

        ]


def add_user_message(session_id: str, message: str):

    chat_sessions[session_id].append(

        {

            "role": "user",

            "content": message

        }

    )


def add_assistant_message(session_id: str, message: str):

    chat_sessions[session_id].append(

        {

            "role": "assistant",

            "content": message

        }

    )


def get_history(session_id: str):

    return chat_sessions.get(session_id, [])


def get_all_sessions():

    return chat_sessions