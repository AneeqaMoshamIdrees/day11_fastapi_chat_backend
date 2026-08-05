"""
Day 11

Gemini Service

Author:
Aneeqa Mosham Idrees
"""

import os

from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

MODEL_NAME = "gemini-3.5-flash-lite"


def generate_reply(history):

    prompt = ""

    for message in history:

        role = message["role"].upper()

        content = message["content"]

        prompt += f"{role}: {content}\n\n"

    response = client.models.generate_content(

        model=MODEL_NAME,

        contents=prompt

    )

    return response.text