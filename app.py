import streamlit as st
from rag_pipeline import query_rag
import sqlite3

st.set_page_config(page_title="Tracxn Assistant")
st.title("Financial Assistant (Q&A + Metrics)")

question = st.text_input("Ask your question (e.g., revenue trend, CEO statement):")

if question:
    answer = query_rag(question)
    st.subheader("Answer")
    st.write(answer)

st.subheader("Metrics Extracted")
conn = sqlite3.connect("financials.db")
c = conn.cursor()
c.execute("SELECT * FROM metric_table")
rows = c.fetchall()
for row in rows:
    st.write(f"{row[0]} — {row[1]}: ₹ {row[2]}")
