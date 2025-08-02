
# -----------------------------------
# INPUT/OUTPUT PATHS FOR CSV FILES
# -----------------------------------
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = PROJECT_ROOT / "data" / "spain"

if not DATA_DIR.exists():
    DATA_DIR.mkdir(parents=True, exist_ok=True)
if not (DATA_DIR / "raw").exists():
    (DATA_DIR / "raw").mkdir(parents=True, exist_ok=True)
if not (DATA_DIR / "processed").exists():
    (DATA_DIR / "processed").mkdir(parents=True, exist_ok=True)

GOOGLE_NEWS_PATH = "raw/news.csv"
ARTICLES_PATH = "raw/articles.csv"
YOUTUBE_VIDEOS_PATH = "raw/videos.csv"
TITLES_PATH = "raw/titles.csv"
SUMMARY_PATH = "processed/summary.txt"
FB_POST_PATH = "processed/post.txt"


# -----------------------------------
# HUGGINGFACE MODEL CONFIGURATION
# -----------------------------------
MODEL_ID = "meta-llama/Llama-3.2-1B-Instruct"

# -----------------------------------
# URLS FOR ARTICLES
# -----------------------------------
ARTICLE_URLS = [
   'https://www.vogue.es/belleza',
   'https://www.elle.com/es/belleza',
   'https://www.telva.com/belleza.html',
   'https://smoda.elpais.com/belleza/',
   'https://www.mujerhoy.com/belleza/'
]

