from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from services.gemini_service import generate_title


router = APIRouter()


class TitleRequest(BaseModel):

    message: str


class TitleResponse(BaseModel):

    title: str


@router.post("/api/generate-title", response_model=TitleResponse)
def generate_chat_title(request: TitleRequest):

    if not request.message.strip():

        raise HTTPException(
            status_code=400,
            detail="Message cannot be empty."
        )

    try:

        title = generate_title(request.message)

        return TitleResponse(
            title=title
        )

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )