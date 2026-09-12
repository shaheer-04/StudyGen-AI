import pypdf

def extract_text(pdf_file):
    """
    Extracts and cleans raw text from an uploaded PDF file.
    Supports both file paths (strings) and Streamlit UploadedFile objects.
    """
    try:
        reader = pypdf.PdfReader(pdf_file)
        extracted_text = ""
        
        # Extract text page by page
        for page in reader.pages:
            text = page.extract_text()
            if text:
                extracted_text += text + "\n"
        
        # Clean up excess spaces and formatting lines
        cleaned_text = " ".join(extracted_text.split())
        
        # Handle empty/scanned PDFs
        if not cleaned_text:
            return None, "No readable text found. The PDF might be scanned or image-only."
            
        return cleaned_text, None

    except Exception as e:
        return None, f"Failed to process PDF: {str(e)}"