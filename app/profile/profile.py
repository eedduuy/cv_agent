import streamlit as st
import json
import os
import requests
from ..LLM.model import get_model




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
def generate_profile_from_text():
    st.subheader("🔍 Generate Profile from Text or CV")
    raw_text = st.text_area("Paste your existing CV or descriptive text")
    if st.button("Extract Profile Info") and raw_text:
        
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
        
        try:
            with st.spinner("Loading model and generating profile..."):
                # Obtener el modelo
                llama_pipe = get_model()
                
                # Generar respuesta
                response = llama_pipe(prompt, max_new_tokens=1024, temperature=0.3, do_sample=True)
                generated_text = response[0]['generated_text']
                
                # Extraer solo la parte generada (sin el prompt)
                response_only = generated_text[len(prompt):].strip()
                
                # Limpiar la respuesta para extraer solo el JSON
                response_clean = response_only
                if response_clean.startswith("```json"):
                    response_clean = response_clean[7:-3].strip()
                elif response_clean.startswith("```"):
                    response_clean = response_clean[3:-3].strip()
                
                profile_json = json.loads(response_clean)
                st.success("Profile generated successfully!")
                st.json(profile_json)
                st.download_button(
                    "Download Profile as JSON", 
                    json.dumps(profile_json, indent=2), 
                    file_name="user_profile.json"
                )
                return profile_json
                
        except json.JSONDecodeError as e:
            st.error(f"Failed to parse response as JSON: {e}")
            st.text("Raw response:")
            st.text(response_only if 'response_only' in locals() else "No response")
        except Exception as e:
            st.error(f"Error generating profile: {e}")
            
    return None
