"""
Day 11

Gemini Service

Author:
Aneeqa Mosham Idrees
"""

import os

from dotenv import load_dotenv
from google import genai
from google.genai import types


# Load environment variables
load_dotenv()


# Create Gemini client
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


# Gemini model
MODEL_NAME = "gemini-3.5-flash-lite"


# System instruction
SYSTEM_INSTRUCTION = """
You are a helpful AI assistant.

Answer the user's questions clearly, accurately, and politely.

For technical questions, explain concepts step by step
and use simple language when appropriate.
"""


def generate_reply(history):
    """
    Generate a response using the conversation history.

    Our application stores messages like:

    {
        "role": "user",
        "content": "Hello"
    }

    or:

    {
        "role": "assistant",
        "content": "Hello! How can I help?"
    }

    We convert them into Gemini Content objects.
    """

    try:

        print("\n========== GEMINI CHAT DEBUG ==========")

        print("Original history:")
        print(history)

        # -------------------------------------------------
        # Convert application history into Gemini history
        # -------------------------------------------------

        contents = []

        for message in history:

            role = message.get("role")
            text = message.get("content", "")

            # Ignore empty messages
            if not text:
                continue

            # Gemini uses:
            #
            # user  -> user
            # assistant -> model
            #
            if role == "user":

                gemini_role = "user"

            elif role == "assistant":

                gemini_role = "model"

            else:

                # Ignore system messages because our
                # system instruction is passed separately.
                continue

            contents.append(
                types.Content(
                    role=gemini_role,
                    parts=[
                        types.Part.from_text(
                            text=text
                        )
                    ]
                )
            )

        print("\nConverted Gemini contents:")
        print(contents)

        # -------------------------------------------------
        # Make sure there is something to send
        # -------------------------------------------------

        if not contents:

            return "Please enter a message."

        # -------------------------------------------------
        # Send conversation to Gemini
        # -------------------------------------------------

        response = client.models.generate_content(

            model=MODEL_NAME,

            contents=contents,

            config=types.GenerateContentConfig(

                system_instruction=SYSTEM_INSTRUCTION

            )

        )

        print("\nGemini response:")
        print(response)

        # -------------------------------------------------
        # Extract response text
        # -------------------------------------------------

        if response.text:

            reply = response.text.strip()

            print("\nGemini text:")
            print(reply)

            return reply

        return "Gemini returned an empty response."

    except Exception as e:

        print("\n========== GEMINI CHAT ERROR ==========")

        print(type(e).__name__)

        print(str(e))

        print("=======================================\n")

        raise


def generate_title(message):
    """
    Generate a short 3-5 word title for a chat session.
    """

    prompt = f"""
Generate a short title for this conversation.

Rules:

- Use exactly 3 to 5 words.
- Do not use quotation marks.
- Do not add explanations.
- Return only the title.

User message:
{message}
"""

    response = client.models.generate_content(

        model=MODEL_NAME,

        contents=prompt

    )

    if response.text:

        return response.text.strip()

    return "New Chat"