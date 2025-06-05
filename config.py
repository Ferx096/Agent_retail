import os
from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI, AzureOpenAIEmbeddings
from pathlib import Path

# Busca .env en el directorio actual y en el padre (raíz del proyecto)
current_dir = Path(__file__).parent
root_dir = current_dir.parent

dotenv_path = current_dir / '.env'
if not dotenv_path.exists():
    dotenv_path = root_dir / '.env'
load_dotenv(dotenv_path)

AZURE_CONFIG = {
    "endpoint": os.getenv("AZURE_OPENAI_ENDPOINT"),
    "api_key": os.getenv("AZURE_OPENAI_API_KEY"),
    "deployment_name": os.getenv("AZURE_OPENAI_CHAT_DEPLOYMENT_NAME"),
    "embedding_deployment": os.getenv("AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME"),
    "api_version": os.getenv("AZURE_OPENAI_API_VERSION", "2023-05-15"),
}

def get_llm():
    return AzureChatOpenAI(
        azure_endpoint=AZURE_CONFIG["endpoint"],
        api_key=AZURE_CONFIG["api_key"],
        azure_deployment=AZURE_CONFIG["deployment_name"],
        api_version=AZURE_CONFIG["api_version"],
        temperature=0.0,
    )

def get_embedding():
    print(f"[DEBUG] Embedding deployment: {AZURE_CONFIG['embedding_deployment']}")
    return AzureOpenAIEmbeddings(
        azure_endpoint=AZURE_CONFIG["endpoint"],
        api_key=AZURE_CONFIG["api_key"],
        azure_deployment=AZURE_CONFIG["embedding_deployment"],
        api_version=AZURE_CONFIG["api_version"],
    )

#HUGGING-FACE
HUGGING={
    "api_url": os.getenv("HUGGINGFACE_API_URL"),
    "api": os.getenv("API_TOKEN_HUGGINGFACE"),
}

