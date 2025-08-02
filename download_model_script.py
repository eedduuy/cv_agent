import os
import json
from dotenv import load_dotenv
from huggingface_hub import login
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
from huggingface_hub import INferenceCLient
# Cargar variables de entorno
load_dotenv()

def download_and_test_model():
    """
    Descarga el modelo Llama y hace una prueba básica
    """
    # Configuración
    model_id = "meta-llama/Llama-3.2-1B-Instruct"
    HF_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")
    
    if not HF_TOKEN:
        raise ValueError("HUGGINGFACEHUB_API_TOKEN not found in environment variables.")
    
    print("🔐 Logging in to Hugging Face...")
    login(HF_TOKEN)
    print("✅ Login successful!")
    
    print(f"📥 Downloading model: {model_id}")
    print("This may take several minutes depending on your internet connection...")
    
    try:
        # Descargar tokenizer
        print("📝 Loading tokenizer...")
        tokenizer = AutoTokenizer.from_pretrained(model_id)
        print("✅ Tokenizer loaded successfully!")
        
        # Descargar modelo
        print("🧠 Loading model...")
        model = AutoModelForCausalLM.from_pretrained(
            model_id,
            torch_dtype="auto",  # Usa el tipo de datos óptimo
            device_map="auto"    # Distribución automática en GPU/CPU
        )
        print("✅ Model loaded successfully!")
        
        # Crear pipeline
        print("🔧 Creating pipeline...")
        llama_pipe = pipeline(
            "text-generation", 
            model=model, 
            tokenizer=tokenizer,
            max_new_tokens=300,
            device_map="auto"
        )
        print("✅ Pipeline created successfully!")
        
        return llama_pipe
        
    except Exception as e:
        print(f"❌ Error downloading model: {e}")
        return None

def test_profile_extraction(pipe):
    """
    Prueba la extracción de perfil con texto de ejemplo
    """
    print("\n🧪 Testing profile extraction...")
    
    # Texto de CV de ejemplo
    sample_cv = """
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
    
    prompt = f"""You are an assistant that extracts structured user profile data from unstructured text.
Given the following text:
{sample_cv}

Extract the user's profile into the following JSON format:
- name
- title
- contact (email, phone, linkedin)
- photo (optional)
- summary
- experience (list of roles, companies, dates, descriptions)
- education (list of degrees, institutions, years)
- courses
- languages
- skills

Respond only with a valid JSON object."""
    
    try:
        print("🔄 Generating response...")
        response = pipe(prompt, max_new_tokens=1024, temperature=0.3, do_sample=True)
        generated_text = response[0]['generated_text']
        
        # Extraer solo la parte generada
        response_only = generated_text[len(prompt):].strip()
        
        print("\n📄 Raw response:")
        print("-" * 50)
        print(response_only)
        print("-" * 50)
        
        # Intentar parsear como JSON
        try:
            # Limpiar formato markdown si existe
            response_clean = response_only
            if response_clean.startswith("```json"):
                response_clean = response_clean[7:-3].strip()
            elif response_clean.startswith("```"):
                response_clean = response_clean[3:-3].strip()
            
            profile_json = json.loads(response_clean)
            
            print("\n✅ Successfully parsed JSON:")
            print(json.dumps(profile_json, indent=2))
            
            # Guardar en archivo
            with open("test_profile.json", "w") as f:
                json.dump(profile_json, f, indent=2)
            print("\n💾 Profile saved to 'test_profile.json'")
            
        except json.JSONDecodeError as e:
            print(f"\n❌ Failed to parse as JSON: {e}")
            print("You may need to adjust the prompt or post-processing.")
            
    except Exception as e:
        print(f"❌ Error during generation: {e}")

def main():
    print("🚀 Starting model download and test...")
    print("=" * 60)
    
    # Descargar modelo
    pipe = download_and_test_model()
    
    if pipe:
        # Probar extracción de perfil
        test_profile_extraction(pipe)
        print("\n✅ Process completed successfully!")
    else:
        print("\n❌ Failed to download model. Please check your token and internet connection.")

if __name__ == "__main__":
    main()
