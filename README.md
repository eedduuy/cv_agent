# CV Agent (WIP)
[![Python Version](https://img.shields.io/badge/python-3.12%2B-blue)](https://www.python.org)
[![Streamlit](https://img.shields.io/badge/streamlit-1.47.0-orange)](https://streamlit.io)
[![License: MIT](https://img.shields.io/badge/license-MIT-green)](LICENSE)

A Streamlit web application that generates a personalized CV and cover letter tailored to a specific job offer using large language models (LLMs) and similarity search.

## Features

* **Profile Generation**: Create a JSON-based user profile from an existing CV, containing personal information, education, courses, and work experience.
* **Personalized CV & Cover Letter**: Input a job offer and obtain a customized CV and cover letter by leveraging similarity search and LLMs on your saved profile data.
* **Easy-to-Use Web Interface**: Two main pages accessible via Streamlit:

  * **Profile Setup** (`profile.py`): Upload and parse your CV to build `profile.json`.
  * **CV & Cover Letter Generator** (`cv.py`): Provide a job description to generate tailored application documents.
* **Persistent Data Storage**: All generated files (profile JSON, CV, cover letter) are stored in the `data/` directory.

## Project Structure

```
cv_agent/
├── app.py               # Streamlit entry point
├── pages/               # Streamlit page modules
│   ├── profile.py       # Profile JSON generation page
│   └── cv.py            # CV & cover letter generation page
├── app/                 # Core application modules
│   ├── LLM/
│   │   ├── model.py     # LLM prompt & generation logic
│   │   └── embedding.py # Embedding & similarity setup
│   ├── job/
│   │   └── cv_gen.py    # CV & cover letter creation functions
│   └── profile/
│       └── profile.py   # Profile parsing & JSON builder
├── data/                # Output directory for JSON, CVs, letters
├── requirements.txt     # Python dependencies
└── space.yaml           # Deployment configuration WIP
```

## Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/eedduuy/cv_agent.git
   cd cv_agent
   ```

2. **Create and activate a virtual environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the Streamlit app from the project root:

```bash
streamlit run app.py
```

1. **Profile Page**: Upload your existing CV file to automatically extract and save relevant information into `data/profile.json`.
2. **CV Page**: Paste or upload the job offer description. The app will use your saved profile and LLMs to generate:

   * A tailored CV (`data/<timestamp>_cv.txt`)
   * A matching cover letter (`data/<timestamp>_cover_letter.txt`)

## Configuration

* Environment variables (e.g., API keys) can be set in a `.env` file.
* Adjust LLM or embedding model settings in `app/LLM/model.py` and `app/LLM/embedding.py` as needed.
* Model selection (LLM and embedding) in `app/config.py`

## Dependencies

* python-dotenv\~=1.1.0
* huggingface-hub\~=0.34.3
* streamlit\~=1.47.0
* langchain\~=0.3.25
* langchain-community\~=0.3.27
* langchain-huggingface\~=0.3.1
* sentence-transformers\~=4.1.0
* faiss-cpu\~=1.11.0post1

## License

This project is available under the [MIT License](LICENSE).


