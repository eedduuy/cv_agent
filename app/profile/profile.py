import json
from ..LLM.model import generate_text

from dotenv import load_dotenv

from ..utils import make_json

load_dotenv()

# --- Generate profile from raw input or CV text ---
def generate_profile_from_text(raw_text : str) -> dict:
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
    generated_text = generate_text(prompt)

    try:
        profile_json = json.loads(generated_text)
    except json.JSONDecodeError as e:
        profile_json = json.loads(make_json(generated_text))


    
    return profile_json

def generate_profile_from_file(file):
    pass

def generate_profile_from_cv(file):
    pass