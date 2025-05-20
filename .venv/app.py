import streamlit as st
from summarizer import summarize_text
from extractor import extract_from_url, extract_from_pdf
import os
from datetime import datetime

st.title("📚 Daily Reading Digest - Text Summarizer")

st.sidebar.header("Add to your Digest")

# Option 1: Paste URL
url = st.sidebar.text_input("Paste an article URL")
if url and st.sidebar.button("Summarize URL"):
    with st.spinner("Extracting and summarizing..."):
        content = extract_from_url(url)
        summary = summarize_text(content)
        st.success("Summary:")
        st.write(summary)
        with open(f"summaries/{datetime.today().date()}_summary.txt", "a") as f:
            f.write(f"\n\n[From URL: {url}]\n{summary}")

# Option 2: Upload PDF
pdf_file = st.sidebar.file_uploader("Upload a PDF", type=["pdf"])
if pdf_file and st.sidebar.button("Summarize PDF"):
    with st.spinner("Reading and summarizing PDF..."):
        content = extract_from_pdf(pdf_file)
        summary = summarize_text(content)
        st.success("Summary:")
        st.write(summary)
        with open(f"summaries/{datetime.today().date()}_summary.txt", "a") as f:
            f.write(f"\n\n[From PDF: {pdf_file.name}]\n{summary}")

# View Digest
st.subheader("📰 Your Daily Digest")
digest_path = f"summaries/{datetime.today().date()}_summary.txt"
if os.path.exists(digest_path):
    with open(digest_path, "r") as f:
        st.text(f.read())
else:
    st.info("No digest yet. Add something from the sidebar!")

