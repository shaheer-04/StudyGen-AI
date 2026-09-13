import os
from pathlib import Path

from dotenv import load_dotenv
from google import genai

from prompts import (
    SUMMARY_PROMPT,
    KEY_POINTS_PROMPT,
    MCQ_PROMPT,
    PRACTICE_QUESTIONS_PROMPT,
    FLASHCARDS_PROMPT,
)


# Read .env from the same folder as this file.
load_dotenv(Path(__file__).with_name(".env"))


def call_ai(prompt: str) -> str:
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError("GEMINI_API_KEY is missing from .env.")

    model = os.getenv("GEMINI_MODEL")

    if not model:
        raise ValueError("GEMINI_MODEL is missing from .env.")

    client = genai.Client(api_key=api_key)

    response = client.interactions.create(
        model=model,
        input=prompt,
    )

    if not response.output_text:
        raise RuntimeError("Gemini returned no text. Please try again.")

    return response.output_text.strip()


def generate_summary(study_text: str) -> str:
    if not study_text.strip():
        raise ValueError("Please provide some study material.")

    prompt = SUMMARY_PROMPT.format(study_text=study_text)
    return call_ai(prompt)


def generate_key_points(study_text: str) -> str:
    if not study_text.strip():
        raise ValueError("Please provide some study material.")

    prompt = KEY_POINTS_PROMPT.format(study_text=study_text)
    return call_ai(prompt)


def generate_mcqs(study_text: str, count: int = 5) -> str:
    if not study_text.strip():
        raise ValueError("Please provide some study material.")

    if not isinstance(count, int) or not 1 <= count <= 10:
        raise ValueError("MCQ count must be between 1 and 10.")

    prompt = MCQ_PROMPT.format(
        study_text=study_text,
        count=count,
    )
    return call_ai(prompt)


def generate_practice_questions(study_text: str) -> str:
    if not study_text.strip():
        raise ValueError("Please provide some study material.")

    prompt = PRACTICE_QUESTIONS_PROMPT.format(
        study_text=study_text,
    )
    return call_ai(prompt)

def generate_flashcards(study_text: str) -> str:
    if not study_text.strip():
        raise ValueError("Please provide some study material.")

    prompt = FLASHCARDS_PROMPT.format(study_text=study_text)
    return call_ai(prompt)




# Runs only when you execute this file directly.
if __name__ == "__main__":
    sample_text = """
    HTML defines the structure of a web page.
    CSS controls its appearance and layout.
    JavaScript adds interactivity to web pages.
    """

    try:
        print("Generating key points...\n")
        print(generate_key_points(sample_text))

        #print("\nGenerating MCQs...\n")
        #print(generate_mcqs(sample_text, count=3))

        #print("\nGenerating practice questions...\n")
        #print(generate_practice_questions(sample_text))
    except Exception as error:
        # Show the error type without exposing request details or secrets.
        print(f"Test failed: {type(error).__name__}")
        print("Check your .env settings and API access.")