# main.py
import streamlit as st
import json

from app.config import MODEL_ID
from app.profile.profile import load_user_profile
from app.job.job_description import upload_job_description
from app.LLM.embedding import extract_text_chunks
from app.profile.profile import generate_profile_from_text




# --- Streamlit tabs ---
tabs = st.tabs(["📄 Generate CV", "🧠 Create Profile"])

with tabs[0]:
    st.title("📄 AI-Powered CV & Cover Letter Generator")

    profile = load_user_profile()
    job_description = upload_job_description()

    include_summary = st.checkbox("Include Professional Summary", value=True)
    include_photo = st.checkbox("Include Photo in Resume", value=False)
    include_courses = st.checkbox("Include Courses & Certifications", value=True)

'''
    if profile and job_description:
        # Prepare data for similarity search
        texts = extract_text_chunks(profile)
        embeddings = HuggingFaceEmbeddings(model_name=MODEL_ID)
        vector_store = FAISS.from_texts(texts, embeddings)

        # Get top relevant entries
        docs = vector_store.similarity_search(job_description, k=8)
        relevant_profile = "\n".join([doc.page_content for doc in docs])

        # Prompt template
        prompt_template = PromptTemplate(
            input_variables=["profile", "job", "include_summary", "include_photo", "include_courses"],
            template="""
You are a CV generation assistant. Using the provided user profile and job description, generate:

1. A one-page resume in Markdown format with sections:
   - Header (name, title, contact info, {include_photo})
   - Professional Summary ({include_summary})
   - Relevant Work Experience
   - Education
   - Courses & Certifications ({include_courses})
   - Languages
   - Skills

Only include sections if the user profile contains relevant information. Tailor the experience and wording to the job description provided.

User Profile:
{profile}

Job Description:
{job}
"""
        )

        llm = HuggingFaceHub(
            repo_id="meta-llama/Meta-Llama-3-8B-Instruct",
            model_kwargs={"temperature": 0.5, "max_new_tokens": 1024}
        )

        chain = LLMChain(llm=llm, prompt=prompt_template)
        result = chain.run(
            profile=relevant_profile,
            job=job_description,
            include_summary=str(include_summary),
            include_photo=str(include_photo),
            include_courses=str(include_courses)
        )

        st.markdown("## ✨ Generated Resume and Cover Letter")
        st.markdown(result)
        st.download_button("Download as Markdown", result, file_name="resume_and_letter.md")
'''
with tabs[1]:
    st.title("🧠 Interactive Profile Builder")
    st.subheader("🔍 Generate Profile from Text or CV")
    raw_text = st.text_area("Paste your existing CV or descriptive text")
    profile = generate_profile_from_text(raw_text)


