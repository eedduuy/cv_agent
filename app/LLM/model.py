import os

from dotenv import load_dotenv
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
from huggingface_hub import login

load_dotenv()

# Cache global para el modelo
model_cache = None

def get_model():
    global model_cache
    if model_cache is None:
        # Login con el token
        HF_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")
        if not HF_TOKEN:
            raise ValueError("HUGGINGFACEHUB_API_TOKEN not found in environment variables.")
        
        login(HF_TOKEN)
        
        # Cargar modelo y tokenizer
        model_id = "meta-llama/Llama-3.2-3B-Instruct"
        tokenizer = AutoTokenizer.from_pretrained(model_id)
        model = AutoModelForCausalLM.from_pretrained(model_id)
        model_cache = pipeline("text-generation", model=model, tokenizer=tokenizer, max_new_tokens=1024)
    
    return model_cache
