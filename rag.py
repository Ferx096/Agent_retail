from config import get_embedding
from config import get_llm

# Configuración de logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Cargar variables de entorno
load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
openai.api_key = OPENAI_API_KEY

# --- Generar embedding y almacenar en FAISS ---
if fragmento_deseado:
    logging.info("Generando embedding del fragmento extraído...")
    response = openai.get_embedding(
        input=fragmento_deseado,
        model="text-embedding-ada-002"
    )
    embedding = np.array(response['data'][0]['embedding'], dtype=np.float32).reshape(1, -1)
    
    # Crear índice FAISS y almacenar embedding
    dim = embedding.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embedding)
    faiss.write_index(index, os.path.join(document_folder, "fragment_embedding.index"))
    logging.info("Embedding generado y almacenado en FAISS: %s", os.path.join(document_folder, "fragment_embedding.index"))


start_idx = fragmento.find(start_text)
end_idx = fragmento.find(end_text)

if start_idx == -1 or end_idx == -1:
    raise ValueError("No se encontraron los textos delimitadores en el PDF extraído.")

end_idx += len(end_text)
fragmento_deseado = fragmento[start_idx:end_idx]

logging.info("Fragmento extraído:\n%s", fragmento_deseado)