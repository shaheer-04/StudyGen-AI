# Product Requirements Document (PRD)
## StudyGen AI

### 1. Problem Statement
Students have lecture PDFs, notes, and textbooks, but spend significant time
manually converting them into summaries, key points, and practice questions
before exams.

### 2. Solution
StudyGen AI lets a student upload their own study material (PDF or pasted
text) and automatically generates a complete revision kit — grounded only in
that material, not generic AI knowledge.

### 3. Target Users
University, college, and school students preparing for exams.

### 4. Core Features
- PDF upload and text extraction
- Paste study text directly
- AI-generated exam revision summary
- AI-generated key concepts
- AI-generated MCQs with answers
- AI-generated practice questions
- AI-generated flashcards for quick review
- Clean, tabbed results interface for easy navigation

### 5. How It Works
```
Student
  ↓
Upload PDF / Paste Text
  ↓
Text Extraction (PyPDF)
  ↓
Generative AI (Groq API)
  ↓
Summary + Key Points + MCQs + Practice Questions + Flashcards
  ↓
Revision Kit (Streamlit UI)
```

### 6. Technology Stack
- Python
- Streamlit (web interface)
- Groq API (content generation)
- PyPDF (PDF text extraction)
- Git / GitHub (version control and collaboration)
- Streamlit Community Cloud (deployment)

### 7. Team & Responsibilities
| Member | Responsibility |
|---|---|
| Member 1 | Streamlit UI, application flow, integration |
| Member 2 | Generative AI integration, prompt engineering |
| Member 3 | PDF handling and text extraction |
| Member 4 | Testing, QA, documentation, demo preparation |

### 8. Key Design Decisions
- Output is grounded strictly in the student's own uploaded material, avoiding
  generic AI answers unrelated to their coursework.
- Kept the architecture intentionally simple (no RAG, no database, no
  authentication) to prioritize a stable, demoable MVP within the hackathon
  timeframe.
- API keys are never hardcoded or committed to source control; they are
  loaded via environment variables (`.env` locally, Secrets on deployment).

### 9. Limitations (Current MVP)
- Best suited for standard text-based PDFs; scanned/image-only PDFs are
  detected and flagged rather than processed.
- Long documents are truncated to a safe length to keep generation fast and
  reliable.
- Uses a shared/free-tier AI API key, subject to standard rate limits.

### 10. Future Improvements
- Interactive quiz mode with scoring
- Difficulty level selector for generated questions
- Support for additional document formats (Word, PPT, images via OCR)
- Personalized study plans based on quiz performance
- Progress tracking across multiple study sessions

### 11. Impact
By automating the repetitive work of converting study material into revision
content, StudyGen AI gives students back time to focus on actual learning and
practice, rather than manual note preparation.

---
Built for the HEC-NCEAC & PEC Generative & Agentic AI Training — Cohort 11
Midterm Hackathon.
