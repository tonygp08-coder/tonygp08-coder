import streamlit as st
import pdfplumber
import re

st.set_page_config(page_title="PDF Field Extractor", layout="centered")
st.title("📄 PDF Field Extractor")

def extract_fields(text):
    data = {}

    date_match = re.search(r"Date[:\. ]+(\d{2}/\d{2}/\d{4})", text)
    customer_match = re.search(r"Customer\s+(MR\.\w+)", text, re.IGNORECASE)
    agreement_match = re.search(r"AgreementNo\.\s*(\d+)", text)
    loan_type_match = re.search(r"LoanType\s+([A-Z]+)", text)
    tenure_match = re.search(r"Tenure[.:]?\s*(\d+)", text)
    amount_match = re.search(r"AmountFinanced\s+([\d,]+\.\d+)", text)
    instl_match = re.search(r"TotalInstl\.\s*(\d+)", text)
    freq_match = re.search(r"Frequency\s+(\w+)", text)

    data["Date"] = date_match.group(1) if date_match else "Not found"
    data["Customer"] = customer_match.group(1) if customer_match else "Not found"
    data["Agreement No"] = agreement_match.group(1) if agreement_match else "Not found"
    data["Loan Type"] = loan_type_match.group(1) if loan_type_match else "Not found"
    data["Tenure"] = tenure_match.group(1) if tenure_match else "Not found"
    data["Amount Financed"] = amount_match.group(1) if amount_match else "Not found"
    data["Total Installments"] = instl_match.group(1) if instl_match else "Not found"
    data["Frequency"] = freq_match.group(1) if freq_match else "Not found"

    return data

uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file:
    with pdfplumber.open(uploaded_file) as pdf:
        full_text = ""
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                full_text += text + "\n"

    st.subheader("Extracted Text Preview:")
    st.text_area("Full Text", full_text, height=300)

    fields = extract_fields(full_text)
    st.subheader("Extracted Key Fields:")
    for key, val in fields.items():
        st.write(f"**{key}:** {val}")

    st.download_button(
        label="📥 Download full extracted text as .txt",
        data=full_text,
        file_name="extracted_text.txt",
        mime="text/plain"
    )
