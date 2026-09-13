SUMMARY_PROMPT = """
You are an educational revision assistant.

Using only the study material below, write a concise revision summary.
Use clear, simple language.
Do not add information that is not present in the material.

Study material:
{study_text}
"""


KEY_POINTS_PROMPT = """
Using only the study material below, extract up to 10 important
concepts, definitions, facts, and processes.

- Use short bullet points.
- Include only distinct, useful points.
- Keep closely related facts together.
- Return fewer points when the material is short.
- Do not repeat information or add outside facts.
- Return only the bullet points, without an introduction.

Study material:
{study_text}
"""


MCQ_PROMPT = """
Using only the study material below, generate {count} multiple-choice questions
that test important concepts.

For every question:
- Provide exactly four options: A, B, C, and D.
- State the correct answer.
- Give a one-sentence explanation based only on the material.

Do not add information outside the material.

Study material:
{study_text}
"""


PRACTICE_QUESTIONS_PROMPT = """
Using only the study material below, create up to 5 short-answer
practice questions.

- Focus on important definitions, concepts, comparisons, and processes.
- Each question must test a distinct idea or relationship.
- Do not ask the same question using different wording.
- Return fewer questions if the material cannot support 5 useful ones.
- Every question must be answerable from the supplied material.
- Return only numbered questions, without answers or an introduction.

Study material:
{study_text}
"""
FLASHCARDS_PROMPT = """
Using ONLY the following study material, create 8 flashcards for revision.

Format each flashcard EXACTLY like this:

Q: <short question or term>
A: <concise answer or definition, one or two sentences>

Do not include anything else outside this format.

Study material:
{study_text}
"""