# prueba.py

import os
import argparse
from huggingface_hub import InferenceClient
from dotenv import load_dotenv

load_dotenv()
def generate_text(prompt: str,
                  model: str,
                  max_new_tokens: int,
                  temperature: float,
                  top_p: float):
    # Inicializa el cliente una sola vez
    client = InferenceClient(
        provider="hf-inference",
        api_key=os.environ["HF_TOKEN"],
    )

    # Llamada al endpoint de text-generation
    # fijate que usamos client.text_generation(...) en vez de client.text_generation.create
    response = client.chat.completions.create(
    model="HuggingFaceTB/SmolLM3-3B",
    messages=[
        {
            "role": "user",
            "content": "okay take it easy"
        }
    ],
)

    # El resultado suele ser una lista de dicts con la clave 'generated_text'
    if isinstance(response, list) and "generated_text" in response[0]:
        return response[0]["generated_text"]
    # O, en versiones antiguas, puede venir así:
    if hasattr(response, "generated_text"):
        return response.generated_text

    # Fallback genérico
    return str(response)

def main():
    parser = argparse.ArgumentParser(
        description="Script de prueba para generación de texto HF InferenceClient"
    )
    parser.add_argument("--model", type=str,
                        default="HuggingFaceTB/SmolLM3-3B",
                        help="ID del modelo en HF Hub")
    parser.add_argument("--prompt", type=str,
                        default="En un lugar de la Mancha,",
                        help="Texto de entrada")
    parser.add_argument("--max_new_tokens", type=int, default=50,
                        help="Máximo número de tokens a generar")
    parser.add_argument("--temperature", type=float, default=0.7,
                        help="Aleatoriedad (0.0–1.0)")
    parser.add_argument("--top_p", type=float, default=0.9,
                        help="Núcleo de muestreo (top-p)")
    args = parser.parse_args()

    generated = generate_text(
        prompt=args.prompt,
        model=args.model,
        max_new_tokens=args.max_new_tokens,
        temperature=args.temperature,
        top_p=args.top_p
    )

    print("=== Texto Generado ===")
    print(generated)

if __name__ == "__main__":
    main()

