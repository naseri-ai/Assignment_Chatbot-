import streamlit as st
import pandas as pd

LOG_FILE = "logs/chatbot_logs.csv"

st.set_page_config(page_title="Coordinator Dashboard", layout="wide")

st.title("📊 Assignment Chatbot Analytics Dashboard")

try:
    df = pd.read_csv(LOG_FILE)
except:
    st.error("No log data found yet.")
    st.stop()

# -----------------------
# Overview Stats
# -----------------------
st.subheader("📈 Usage Overview")

col1, col2, col3 = st.columns(3)

col1.metric("Total Questions", len(df))
col2.metric("Average Confidence", round(df["confidence"].mean(), 2))
col3.metric("Low Confidence Queries", len(df[df["confidence"] < 0.5]))

# -----------------------
# Most Common Questions
# -----------------------
st.subheader("❓ Most Asked Questions")

top_questions = df["question"].value_counts().head(10)

st.dataframe(top_questions)

# -----------------------
# Low Confidence Questions
# -----------------------
st.subheader("⚠️ Low Confidence Questions (Needs Attention)")

low_conf = df[df["confidence"] < 0.5]

st.dataframe(low_conf[["question", "confidence"]])

# -----------------------
# Confidence Distribution
# -----------------------
st.subheader("📊 Confidence Distribution")

st.bar_chart(df["confidence"])

# -----------------------
# Raw Data
# -----------------------
with st.expander("🔍 View Raw Logs"):
    st.dataframe(df)