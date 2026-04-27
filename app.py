import streamlit as st
from chatbot_logic import get_response
from confidence import estimate_confidence
from logger import log, update_feedback

st.set_page_config(page_title="Assignment Chatbot")

st.title("📘 Assignment 2 Help Bot")
st.caption("Clarifies requirements only — does not generate assignment content")

question = st.text_input("Ask your question:")

if question != st.session_state.get("last_question"):
    st.session_state["feedback_given"] = False

if question:
    answer, score, intent = get_response(question)
    confidence = estimate_confidence(score, answer)

    if "last_question" not in st.session_state or st.session_state["last_question"] != question:
        log_id = log(question, answer, confidence, intent, score)
        st.session_state["last_log_id"] = log_id
        st.session_state["last_question"] = question


    st.markdown("### 💬 Answer")
    st.write(answer)

    st.markdown("### 🔍 Confidence")
    st.progress(confidence)

    if confidence < 0.55:
        st.warning("⚠️ Please confirm this with your tutor.")
    else:
        st.success("✅ This answer is likely correct.")

    if "feedback_given" not in st.session_state:
        st.session_state["feedback_given"] = False

    if not st.session_state["feedback_given"]:

        st.markdown("### 👍 Was this helpful?")

        col1, col2 = st.columns(2)

        if col1.button("👍 Yes"):
            update_feedback(st.session_state["last_log_id"], "positive")
            st.session_state["feedback_given"] = True
            st.success("Thanks for your feedback!")

        if col2.button("👎 No"):
            update_feedback(st.session_state["last_log_id"], "negative")
            st.session_state["feedback_given"] = True
            st.warning("Thanks! We'll improve this.")

st.markdown("---")
st.caption("This tool supports understanding of assignment requirements.")
