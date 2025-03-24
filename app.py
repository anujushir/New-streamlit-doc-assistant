import streamlit as st

st.title("📘 DocuMind AI")
st.markdown("### Your Intelligent Document Assistant")
st.write("Upload a PDF, ask questions, and get AI-powered answers!")

uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_file:
    st.success("✅ File uploaded successfully!")
    st.write("Further processing will be done here...")
