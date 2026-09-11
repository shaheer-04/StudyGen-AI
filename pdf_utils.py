from pypdf import PdfReader


def extract_text_from_pdf(uploaded_file):
    """
    Extracts text from an uploaded PDF file.

    NOTE FOR THE TEAM:
    This is a simple starter version so Member 1 (UI) can test the app
    end-to-end today without waiting on anyone else.
    Member 3 (PDF/Data Lead) will improve this later: cleaning messy text,
    handling scanned/empty PDFs, handling very long PDFs, etc.
    The function name and what it returns (a string of text) should stay
    the same so app.py keeps working without changes.
    """
    try:
        reader = PdfReader(uploaded_file)
        text = ""
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
        return text.strip()
    except Exception:
        return ""
