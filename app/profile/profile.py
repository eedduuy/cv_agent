import streamlit as st
import json
from ..LLM.model import generate_text
from app.config import DATA_DIR

from dotenv import load_dotenv

from ..utils import make_json

load_dotenv()

# --- Load user profile ---
def load_user_profile():
    uploaded = st.file_uploader("Upload your profile (JSON format)", type=["json"], key="upload_profile")
    if uploaded:
        profile = json.load(uploaded)
        st.success("Profile loaded successfully!")
        return profile
    return None

# --- Generate profile from raw input or CV text ---
def generate_profile_from_text(raw_text : str):
    prompt = f"""You are an assistant that extracts structured user profile data from unstructured text.
    Given the following text:
    {raw_text}
    
    Extract the user's profile into the following JSON format:
    - name
    - title
    - contact (email, phone, linkedin, github)
    - photo (optional)
    - summary
    - experience (list of roles, companies, start date, end date, descriptions)
    - education (list of degrees, institutions, years, qualification)
    - courses
    - languages (list of languages, levels)
    - skills
    
    Respond only with a valid JSON object."""
        
    # Generar respuesta
    response = generate_text(prompt)
    generated_text = response.choices[0].message.content

    try:
        profile_json = json.loads(generated_text)
    except json.JSONDecodeError as e:
        profile_json = json.loads(make_json(generated_text))


    
    return profile_json

