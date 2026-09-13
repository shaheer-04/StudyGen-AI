import re
import streamlit as st
from pdf_utils import extract_text
from ai_functions import (
    generate_summary,
    generate_key_points,
    generate_mcqs,
    generate_practice_questions,
    generate_flashcards,
)

st.set_page_config(page_title="StudyGen AI", page_icon="📚", layout="centered")

MAX_CHARS = 15000

st.title("📚 StudyGen AI")
st.subheader("Turn Your Study Material Into a Revision Kit")
st.markdown("---")


def show_text(content: str):
    """Displays AI-generated text with line breaks preserved properly in Streamlit."""
    st.markdown(content.replace("\n", "  \n"))


def parse_flashcards(text: str):
    """Parses 'Q: ... / A: ...' blocks into a list of (question, answer) tuples."""
    cards = []
    blocks = re.split(r"\n\s*\n", text.strip())
    for block in blocks:
        q_match = re.search(r"Q:\s*(.+)", block)
        a_match = re.search(r"A:\s*(.+)", block, re.DOTALL)
        if q_match and a_match:
            cards.append((q_match.group(1).strip(), a_match.group(1).strip()))
    return cards


# --------------------------------------------------------------------
# 1. INPUT SECTION
# --------------------------------------------------------------------
st.header("1. Add Your Study Material")

tab1, tab2 = st.tabs(["📄 Upload PDF", "✍️ Paste Text"])

study_text = ""

with tab1:
    uploaded_file = st.file_uploader("Upload your lecture PDF", type=["pdf"])
    if uploaded_file is not None:
        with st.spinner("Extracting text from PDF..."):
            study_text, pdf_error = extract_text(uploaded_file)
        if pdf_error:
            st.error(pdf_error)
        elif study_text:
            st.success(f"Extracted {len(study_text)} characters from the PDF.")

with tab2:
    pasted_text = st.text_area("Paste your notes here", height=250)
    if pasted_text:
        study_text = pasted_text

st.markdown("---")

# --------------------------------------------------------------------
# 2. GENERATE BUTTON
# --------------------------------------------------------------------
st.header("2. Generate Your Revision Kit")

include_flashcards = st.checkbox("🎴 Also generate flashcards", value=True)

if st.button("🚀 Generate Revision Kit", type="primary"):
    if not study_text or len(study_text.strip()) < 50:
        st.warning("Please upload a PDF or paste at least a few sentences of study material first.")
    else:
        if len(study_text) > MAX_CHARS:
            st.info(
                f"Your material is quite long ({len(study_text)} characters). "
                f"Using the first {MAX_CHARS} characters to keep things fast and reliable."
            )
            study_text = study_text[:MAX_CHARS]

        try:
            with st.spinner("AI is analyzing your material..."):
                summary = generate_summary(study_text)
                key_points = generate_key_points(study_text)
                mcqs = generate_mcqs(study_text, count=5)
                questions = generate_practice_questions(study_text)
                flashcards_raw = generate_flashcards(study_text) if include_flashcards else None

            st.markdown("---")

            tab_names = ["📄 Summary", "🔑 Key Concepts", "📝 MCQs", "❓ Practice Questions"]
            if include_flashcards and flashcards_raw:
                tab_names.append("🎴 Flashcards")

            result_tabs = st.tabs(tab_names)

            with result_tabs[0]:
                show_text(summary)
            with result_tabs[1]:
                show_text(key_points)
            with result_tabs[2]:
                show_text(mcqs)
            with result_tabs[3]:
                show_text(questions)

            if include_flashcards and flashcards_raw:
                with result_tabs[4]:
                    st.caption("Click a card to reveal the answer.")
                    cards = parse_flashcards(flashcards_raw)
                    if cards:
                        cols = st.columns(2)
                        for i, (q, a) in enumerate(cards):
                            with cols[i % 2]:
                                with st.expander(f"🔹 {q}"):
                                    st.write(a)
                    else:
                        show_text(flashcards_raw)

        except Exception as e:
            if "429" in str(e) or "quota" in str(e).lower():
                st.error("The AI service is temporarily busy (rate limit reached). Please wait a minute and try again.")
            else:
                st.error("Something went wrong while generating your revision kit. Please try again.")
            with st.expander("Technical details (for debugging)"):
                st.code(str(e))

st.markdown("---")
st.caption("StudyGen AI — Built for Aspire Pakistan Hackathon 🇵🇰")