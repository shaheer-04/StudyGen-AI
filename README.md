# StudyGen AI 📚

Turn your own study material into a complete revision kit using Generative AI.

## Problem

Students have lecture PDFs, notes, and textbooks, but spend a lot of time manually
turning them into summaries, key points, and practice questions before exams.

## Solution

Upload a PDF or paste your notes, click **Generate Revision Kit**, and StudyGen AI
creates:

- 📄 An exam revision summary
- 🔑 Key concepts
- 📝 MCQs with answers
- ❓ Practice questions

All generated **only from your own uploaded material** — not generic AI answers.

## How It Works

```
Student
  ↓
Upload PDF / Paste Text
  ↓
Text Extraction
  ↓
Generative AI (Gemini)
  ↓
Summary + Key Points + MCQs + Practice Questions
  ↓
Revision Kit
```

## Tech Stack

- Python
- Streamlit — web interface
- Gemini API — content generation
- PyPDF — PDF text extraction

## Team

| Member | Role |
|---|---|
| Member 1 | Streamlit UI & Integration |
| Member 2 | Generative AI Integration |
| Member 3 | PDF Processing |
| Member 4 | Testing, QA & Documentation |

## Running Locally

1. Clone this repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the project folder with:
   ```
   GEMINI_API_KEY=your_api_key_here
   GEMINI_MODEL=gemini-3.6-flash
   ```
4. Run the app:
   ```bash
   streamlit run app.py
   ```
5. Open the local URL shown in your terminal (usually `http://localhost:8501`)

## Future Improvements

- Flashcards
- Interactive quiz mode with scoring
- Difficulty level selector
- Support for more document formats

---

Built for the Aspire Pakistan Hackathon 🇵🇰