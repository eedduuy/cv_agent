from os import getenv
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

from app.config import MODEL_ID

load_dotenv()

# Cache global para el modelo
model_cache = None


def get_model() -> InferenceClient:

    """
    Returns an instance of the Meta-Llama-3-70B-Instruct model for text generation.

    The model is cached globally, so subsequent calls to this function will return the same instance.
    """
    global model_cache
    if model_cache is None:
        model_cache = InferenceClient(
            provider="auto",
            api_key=getenv("HF_TOKEN"),
            model=MODEL_ID
        )
    return model_cache


def generate_text(prompt: str) -> str:
    model = get_model()
    response = model.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content


