import streamlit as st

# --- Upload job description ---
def upload_job_description():
    file = st.file_uploader("Upload Job Description (txt or pdf)", type=["txt"], key="upload_job")
    if file:
        content = file.read().decode("utf-8")
        st.text_area("Job Description", content, height=200)
        return content
    return ""

