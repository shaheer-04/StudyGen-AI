"""
NOTE FOR THE TEAM:
These are MOCK (fake) functions. They let Member 1 build and test the
Streamlit UI today without needing an AI API key yet.

Member 2 (Generative AI Lead) will later replace the INSIDE of each
function with a real call to the Generative AI API, using the prompt
templates in prompts.py.

IMPORTANT: Keep the function names and return formats exactly the same
as below, so app.py does not need to change when Member 2's real
version is merged in.
"""


def generate_summary(study_text: str) -> str:
    # Returns: a single string
    return ("This is a placeholder summary of the uploaded material. "
            "Member 2 will connect this to the real AI API.")


def generate_key_points(study_text: str) -> list:
    # Returns: a list of strings
    return [
        "Placeholder key point 1",
        "Placeholder key point 2",
        "Placeholder key point 3",
    ]


def generate_mcqs(study_text: str, num_questions: int = 5) -> list:
    # Returns: a list of dicts, each shaped like:
    # {"question": "...", "options": {"A": "...", "B": "...", "C": "...", "D": "..."}, "answer": "B"}
    mcqs = []
    for i in range(num_questions):
        mcqs.append({
            "question": f"Placeholder question {i + 1}?",
            "options": {"A": "Option A", "B": "Option B", "C": "Option C", "D": "Option D"},
            "answer": "B",
        })
    return mcqs


def generate_questions(study_text: str) -> list:
    # Returns: a list of strings
    return [
        "Placeholder practice question 1",
        "Placeholder practice question 2",
        "Placeholder practice question 3",
    ]
