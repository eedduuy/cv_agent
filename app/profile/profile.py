import streamlit as st
import json
from ..LLM.model import generate_text
from app.config import DATA_DIR

from dotenv import load_dotenv


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
- contact (email, phone, linkedin)
- photo (optional)
- summary
- experience (list of roles, companies, dates, descriptions)
- education (list of degrees, institutions, years)
- courses
- languages
- skills

Respond only with a valid JSON object."""
        
    # Generar respuesta
    response = generate_text(prompt)
    generated_text = response.choices[0].message.content
    '''
    # Extraer solo la parte generada (sin el prompt)
    response_only = generated_text[len(prompt):].strip()
    
    # Limpiar la respuesta para extraer solo el JSON
    response_clean = response_only
    if response_clean.startswith("```json"):
        response_clean = response_clean[7:-3].strip()
    elif response_clean.startswith("```"):
        response_clean = response_clean[3:-3].strip()
    '''

    profile_json = json.loads(generated_text)
    
    # Save to abilities.json in the data folder

    abilities_path = DATA_DIR / "abilities.json"
    with open(abilities_path, 'w', encoding='utf-8') as f:
        json.dump(profile_json, f, indent=2, ensure_ascii=False)
    
    return profile_json


    return None
