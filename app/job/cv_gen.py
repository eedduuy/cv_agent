from app.LLM.embedding import build_embeddings, get_relevant_info
from app.LLM.model import generate_text



def generate_cv(profile: dict, job_desc: str) -> str:
    relevant = get_relevant_info(profile, job_desc)

    prompt = f"""
You are a CV and cover-letter generation assistant.
Using the following RELEVANT user profile information:
{relevant}

And the following job description:
{job_desc}

Generate a one-page resume in Markdown format with these sections:
- Header (name, title, contact info)
- Professional Summary 
- Relevant Work Experience
- Education
- Courses & Certifications 
- Languages
- Skills

Then, write a personalized cover letter addressing the hiring manager about why the user is a great fit.

Respond only with the complete Markdown document.
"""


    response = generate_text(prompt)
    return response