import streamlit as st
from chatbot_logic import get_response
from confidence import estimate_confidence
from logger import log

st.set_page_config(page_title="Assignment Chatbot")

st.title("📘 Assignment 2 Help Bot")
st.caption("Clarifies requirements only — does not generate assignment content")

question = st.text_input("Ask your question:")

if question:
    answer, score = get_response(question)
    confidence = estimate_confidence(score, answer)

    log(question, answer, confidence)

    st.markdown("### 💬 Answer")
    st.write(answer)

    st.markdown("### 🔍 Confidence")
    st.progress(float(confidence))

    if confidence < 0.55:
        st.warning("⚠️ Please confirm this with your tutor.")
    else:
        st.success("✅ This answer is likely correct.")

st.markdown("---")
st.caption("This tool supports understanding of assignment requirements.")
