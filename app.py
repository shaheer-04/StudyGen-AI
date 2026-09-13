import hashlib
import time

import streamlit as st
from groq import APIConnectionError, APIStatusError, AuthenticationError, RateLimitError

from ai_functions import generate_revision_kit
from pdf_utils import extract_text

st.set_page_config(page_title="StudyGen AI", page_icon="📚", layout="centered")
st.title("📚 StudyGen AI")
st.subheader("Turn Your Study Material Into a Revision Kit")

st.header("1. Add Your Study Material")
source = st.radio("Input method", ["Upload PDF", "Paste text"], horizontal=True)
study_text = ""
if source == "Upload PDF":
    uploaded = st.file_uploader("Upload a text-based lecture PDF", type=["pdf"])
    if uploaded is not None:
        with st.spinner("Reading PDF..."):
            text, error = extract_text(uploaded)
        if error:
            st.error("Could not read this PDF. Try an unencrypted, text-based PDF.")
        else:
            study_text = text or ""
            st.caption(f"Read {len(study_text):,} characters.")
else:
    study_text = st.text_area("Paste your notes", height=250)

study_text = study_text.strip()
too_long = len(study_text) > 15000
if too_long:
    st.warning("This version accepts up to 15,000 characters. Use a shorter excerpt or PDF.")

st.header("2. Generate Your Revision Kit")
include_flashcards = st.checkbox("Also generate flashcards", value=False)
st.caption("Compact kit: summary, key points, up to 3 MCQs and practice questions, plus optional flashcards.")
fingerprint = hashlib.sha256((study_text + str(include_flashcards)).encode()).hexdigest()

if st.button("Generate Revision Kit", type="primary", disabled=too_long):
    if len(study_text) < 50:
        st.warning("Please provide at least 50 characters of study material.")
    elif st.session_state.get("kit_key") == fingerprint and isinstance(st.session_state.get("kit", {}).get("mcqs"), list):
        st.info("Showing your existing kit for these notes.")
    elif time.time() < st.session_state.get("next_attempt", 0):
        seconds = int(st.session_state.next_attempt - time.time()) + 1
        st.warning(f"Please wait about {seconds} seconds before generating another kit.")
    else:
        # A per-session pause reduces bursts; provider-wide quotas still apply.
        st.session_state.next_attempt = time.time() + 65
        try:
            with st.spinner("Preparing your revision kit..."):
                kit = generate_revision_kit(study_text, include_flashcards)
            st.session_state.kit = kit
            st.session_state.kit_key = fingerprint
        except RateLimitError:
            st.error("AI quota reached. A minute limit may reset shortly; a daily limit needs its scheduled reset. Check Groq usage before retrying.")
        except AuthenticationError:
            st.error("The API key was rejected. Check the Groq key in your local or deployment settings.")
        except APIConnectionError:
            st.error("Could not reach Groq. Check your connection and try again later.")
        except APIStatusError:
            st.error("Groq could not process the request. Check model access and service status.")
        except (ValueError, RuntimeError) as error:
            st.error(str(error))
        except Exception:
            st.error("An unexpected error occurred. Your previous kit is still available.")

if "kit" in st.session_state:
    if st.session_state.kit_key != fingerprint:
        st.info("Showing the previous kit. Generate a new kit to apply your changed input or options.")
    kit = st.session_state.kit
    labels = ["Summary", "Key Concepts", "MCQs", "Practice Questions"]
    if kit["flashcards"]:
        labels.append("Flashcards")
    tabs = st.tabs(labels)
    for tab, key in [(tabs[0], "summary"), (tabs[1], "key_points"), (tabs[3], "practice_questions")]:
        with tab:
            st.markdown(kit[key])
    with tabs[2]:
        if not isinstance(kit["mcqs"], list):
            st.info("Generate a new revision kit to use the interactive quiz format.")
        else:
            st.caption("Choose one option, then check your answer.")
            quiz_id = hashlib.sha256((st.session_state.kit_key + repr(kit["mcqs"])).encode()).hexdigest()
            for index, question in enumerate(kit["mcqs"]):
                prefix = f"quiz_{quiz_id}_{index}"
                st.markdown(f"**Question {index + 1}: {question['question']}**")
                options = question["options"]
                selected = st.radio(
                    "Choose an answer",
                    options=list(options),
                    index=None,
                    format_func=lambda letter, choices=options: f"{letter}) {choices[letter]}",
                    key=prefix + "_choice",
                )
                if st.session_state.get(prefix + "_checked") != selected:
                    st.session_state.pop(prefix + "_checked", None)
                if st.button("Check answer", key=prefix + "_check", disabled=selected is None):
                    st.session_state[prefix + "_checked"] = selected
                if selected is not None and st.session_state.get(prefix + "_checked") == selected:
                    correct = question["answer"]
                    if selected == correct:
                        st.success("Correct!")
                    else:
                        st.error("Incorrect.")
                    st.write(f"Correct answer: {correct}) {options[correct]}")
                st.divider()
    if kit["flashcards"]:
        with tabs[4]:
            for question, answer in kit["flashcards"]:
                with st.expander(question):
                    st.write(answer)
    st.caption("Review AI-generated answers against your source material.")

st.divider()
st.caption("HEC-NCEAC & PEC Generative & Agentic AI Training — Cohort 11 Midterm Hackathon")
