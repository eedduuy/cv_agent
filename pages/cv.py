import streamlit as st
import json

from app.job.cv_gen import generate_cv

st.title("📄 AI-Powered CV & Cover Letter Generator")

if st.session_state.get("profile"):
    profile = st.session_state.profile
else:
    uploaded = st.file_uploader("Upload your profile (JSON format)", type=["json"], key="upload_profile")
    if uploaded:
        profile = json.load(uploaded)
        st.success("Profile loaded successfully!")
        st.session_state.profile = profile


job_description = st.text_area("Job Description", key="job_description")

if st.session_state.get("profile") and job_description and st.button("Generate CV"):
    cv = generate_cv(profile, job_description)

    st.subheader("Generated CV")

    # Show the cv
    st.markdown(cv, unsafe_allow_html=True)

    st.download_button(
        label="💾 Download CV",
        data=cv,
        file_name="cv.md",
        mime="text/markdown",
    )

