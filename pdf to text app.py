import streamlit as st
import pdfplumber
import io

st.set_page_config(page_title="PDF to Text Extractor", layout="centered")

st.title("📄 PDF to Text Extractor")

uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file:
    st.info("Extracting text...")

    # Read PDF
    with pdfplumber.open(uploaded_file) as pdf:
        extracted_text = ""
        for page in pdf.pages:
            extracted_text += page.extract_text() + "\n"

    st.success("✅ Text extracted!")

    # Show text on screen
    st.subheader("Extracted Text:")
    st.text_area("Text Content", value=extracted_text, height=300)

    # Download button for text file
    st.download_button(
    label="📥 Download as .txt file",
    data=extracted_text,
    file_name="extracted_text.txt",
    mime="text/plain"
    )