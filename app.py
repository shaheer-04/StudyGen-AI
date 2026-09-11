import streamlit as st
from pdf_utils import extract_text_from_pdf
from ai_functions import generate_summary, generate_key_points, generate_mcqs, generate_questions

st.set_page_config(page_title="StudyGen AI", page_icon="📚", layout="centered")

st.title("📚 StudyGen AI")
st.subheader("Turn Your Study Material Into a Revision Kit")
st.markdown("---")

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
            study_text = extract_text_from_pdf(uploaded_file)
        if study_text:
            st.success(f"Extracted {len(study_text)} characters from the PDF.")
        else:
            st.error("Could not extract text from this PDF. Try another file.")

with tab2:
    pasted_text = st.text_area("Paste your notes here", height=250)
    if pasted_text:
        study_text = pasted_text

st.markdown("---")

# --------------------------------------------------------------------
# 2. GENERATE BUTTON
# --------------------------------------------------------------------
st.header("2. Generate Your Revision Kit")

if st.button("🚀 Generate Revision Kit", type="primary"):
    if not study_text or len(study_text.strip()) < 50:
        st.warning("Please upload a PDF or paste at least a few sentences of study material first.")
    else:
        try:
            with st.spinner("AI is analyzing your material..."):
                summary = generate_summary(study_text)
                key_points = generate_key_points(study_text)
                mcqs = generate_mcqs(study_text, num_questions=5)
                questions = generate_questions(study_text)

            st.markdown("---")

            st.header("📄 Exam Revision Summary")
            st.write(summary)

            st.header("🔑 Key Concepts")
            for point in key_points:
                st.markdown(f"- {point}")

            st.header("📝 MCQs")
            for i, mcq in enumerate(mcqs, start=1):
                st.markdown(f"**Q{i}. {mcq['question']}**")
                for letter, option in mcq["options"].items():
                    st.markdown(f"- {letter}) {option}")
                with st.expander("Show Answer"):
                    st.write(f"Answer: {mcq['answer']}")

            st.header("❓ Practice Questions")
            for i, q in enumerate(questions, start=1):
                st.markdown(f"{i}. {q}")

        except Exception as e:
            st.error("Something went wrong while generating your revision kit. Please try again.")
            st.caption(f"(Technical detail: {e})")

st.markdown("---")
st.caption("StudyGen AI — Built for Aspire Pakistan Hackathon 🇵🇰")
