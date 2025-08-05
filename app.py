# main.py
import streamlit as st
import json

from app.config import MODEL_ID
from app.profile.profile import load_user_profile
from app.job.job_description import upload_job_description
from app.LLM.embedding import extract_text_chunks
from app.profile.profile import generate_profile_from_text




st.title("🧠 Personalized Curriculum Vitae Generator")
st.subheader("📄 Generate a personalized CV based on your profile and job description")