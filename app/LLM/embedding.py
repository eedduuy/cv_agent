from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

from app.config import EMBEDDER_ID


def extract_profile_chunks(profile : dict) -> list[str]:
    chunks = []
    for section, items in profile.items():
        if isinstance(items, str):
            chunks.append(f"{section.capitalize()}: {items}")
        elif isinstance(items, list):
            for item in items:
                if isinstance(item, dict):
                    chunks.append("; ".join(f"{k}: {v}" for k, v in item.items()))
                else:
                    chunks.append(str(item))

    return chunks

def build_embeddings(profile : dict) -> FAISS:
    texts = extract_profile_chunks(profile)
    embedder = HuggingFaceEmbeddings(model_name=EMBEDDER_ID)
    vector_store = FAISS.from_texts(texts, embedder)
    return vector_store

def get_relevant_info(profile: dict, job_desc : str) -> str:
    vector_store = build_embeddings(profile)
    docs = vector_store.similarity_search(job_desc, k=8)
    relevant = "\n".join(doc.page_content for doc in docs)
    return relevant