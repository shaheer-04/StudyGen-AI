"""
Central place for all AI prompts.
Member 2 (Generative AI Lead) will use these inside ai_functions.py
when writing the real (non-mock) logic.
"""

SUMMARY_PROMPT = """You are an educational assistant.
Here is the student's study material:

{study_material}

Create a concise exam revision summary based ONLY on the provided material.
Do not add information that is not present in the material."""

KEY_POINTS_PROMPT = """Using ONLY the study material below, list the most
important key concepts and definitions a student should remember.

Study material:
{study_material}"""

MCQ_PROMPT = """Generate {num_questions} multiple choice questions using ONLY
the following study material. Each question must have exactly 4 options
(A, B, C, D) and one correct answer. Do not include information that is
not present in the material.

Study material:
{study_material}"""

QUESTION_PROMPT = """Generate short practice questions using ONLY the
following study material, focused on testing understanding of the key
concepts.

Study material:
{study_material}"""
