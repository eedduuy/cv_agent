
# -----------------------------------
# INPUT/OUTPUT PATHS FOR FILES
# -----------------------------------
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data"

if not DATA_DIR.exists():
    DATA_DIR.mkdir(parents=True, exist_ok=True)
if not (DATA_DIR / "raw").exists():
    (DATA_DIR / "raw").mkdir(parents=True, exist_ok=True)
if not (DATA_DIR / "processed").exists():
    (DATA_DIR / "processed").mkdir(parents=True, exist_ok=True)



# -----------------------------------
# HUGGINGFACE MODEL CONFIGURATION
# -----------------------------------
MODEL_ID = "meta-llama/Meta-Llama-3-70B-Instruct"



# -----------------------------------
# CV EXAMPLE
# -----------------------------------

CV_EXAMPLE = """
John Doe
Software Engineer
Email: john.doe@email.com
Phone: +1234567890
LinkedIn: linkedin.com/in/johndoe

Professional Summary:
Experienced software engineer with 5 years in full-stack development.

Experience:
- Senior Developer at Tech Corp (2020-2024)
  Developed web applications using Python and React
- Junior Developer at StartupXYZ (2019-2020)
  Built REST APIs and worked with databases

Education:
- Bachelor of Computer Science, University ABC (2015-2019)

Skills: Python, JavaScript, React, SQL, Git
Languages: English (native), Spanish (intermediate)
"""