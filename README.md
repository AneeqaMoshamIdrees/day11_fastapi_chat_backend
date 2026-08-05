# Day 11 - FastAPI Backend & Chat State Management

## Objective

Build a production-ready FastAPI backend that exposes a Large Language Model (LLM) through HTTP APIs while maintaining conversation history using server-side session management.

---

## Technologies Used

- Python 3.12
- FastAPI
- Uvicorn
- Gemini API
- Pydantic
- python-dotenv

---

## Project Structure

```
day11_fastapi_chat_backend/
│
├── app.py
├── .env
├── requirements.txt
├── README.md
│
├── models/
│   ├── request_models.py
│   └── response_models.py
│
├── services/
│   ├── gemini_service.py
│   ├── session_manager.py
│   └── logger.py
│
├── logs/
│   └── chat_server.log
│
└── reports/
    └── day11_report.md
```

---

## Features

- FastAPI Backend
- POST /api/chat
- GET /api/sessions
- In-memory Session Store
- Gemini API Integration
- Structured Logging
- HTTP Error Handling
- Swagger Documentation

---

## Endpoints

### POST /api/chat

Generate an AI response.

Request

```json
{
  "session_id": "abc123",
  "message": "What is Artificial Intelligence?"
}
```

Response

```json
{
  "session_id": "abc123",
  "response": "...",
  "model": "gemini-3.5-flash-lite"
}
```

---

### GET /api/sessions

Returns all active sessions.

---

## Error Handling

- 200 OK
- 400 Bad Request
- 404 Not Found
- 500 Internal Server Error

---

## Logging

The backend records

- Timestamp
- Session ID
- Model Name
- User Prompt
- Latency

Logs are stored inside

```
logs/chat_server.log
```

---

## Run

```bash
python -m venv venv

source venv/bin/activate

pip install -r requirements.txt

uvicorn app:app --reload
```

Swagger

```
http://127.0.0.1:8000/docs
```

---

Author

Aneeqa Mosham Idrees