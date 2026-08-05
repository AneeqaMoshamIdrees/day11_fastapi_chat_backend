# Day 11 Report

## Student

Aneeqa Mosham Idrees

---

## Objective

Develop a FastAPI backend capable of exposing Gemini AI through REST APIs while maintaining chat sessions and conversation history.

---

## Tasks Completed

### FastAPI Server

Successfully created a FastAPI application.

---

### POST /api/chat

Implemented a chat endpoint that

- accepts user messages
- generates Gemini responses
- returns JSON responses

---

### Session Management

Implemented

- create_session()
- get_history()
- add_user_message()
- add_assistant_message()

Conversation history is maintained using an in-memory dictionary.

---

### GET /api/sessions

Displays all active sessions along with message counts.

---

### Error Handling

Implemented

- 400
- 404
- 500

using HTTPException.

---

### Logging

Created

services/logger.py

Logs include

- Timestamp
- Session ID
- Model
- User Prompt
- Latency

Output file

logs/chat_server.log

---

### Swagger Testing

Verified all APIs using

http://127.0.0.1:8000/docs

---

## Challenges Faced

- Gemini SDK validation errors
- Session history formatting
- Logging configuration

---

## Learning Outcomes

After completing Day 11, I learned

- FastAPI fundamentals
- REST API development
- HTTP methods
- Pydantic models
- Session management
- Server-side logging
- Swagger testing
- Gemini API integration

---

## Conclusion

Successfully developed a FastAPI backend with session management, Gemini integration, structured logging, and REST APIs.

---

Author

Aneeqa Mosham Idrees