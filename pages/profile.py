import streamlit as st
from app.profile.profile import generate_profile_from_text

st.title("🧠 Interactive Profile Builder")
st.subheader("🔍 Generate Profile from Text or CV")
raw_text = st.text_area("Paste your existing CV or descriptive text")
if raw_text:
    profile = generate_profile_from_text(raw_text)