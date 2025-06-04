import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__) + '/../'))
import logging
from config import get_embedding
from config import get_llm
from extract_fragment import fragmento_deseado
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain.schema import Document

# Configuración de logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

# ========================
# VECTORE STORE
# ========================
# chunk - split
embedding = get_embedding()
logger.info("Text split + chunl")
text_splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=20)
docs = [Document(page_content=fragmento_deseado)]
all_splits = text_splitter.split_documents(docs)

# vectore store - embedding
vectore_store = FAISS.from_documents(all_splits, embedding)  # search FAISS
retriever = vectore_store.as_retriever()  # converts index into a retriever
logger.info("vector store cargado")


# ========================
# FLUJO RAG
# ========================
llm = get_llm()
query = (
    "Con base en el contexto proporcionado:\n"
    "1. Escribe una descripción ideal de producto de Snacks saludables.\n"
    "2. Enumera las condiciones o datos mínimos necesarios para generar una descripción precisa.\n"
    "3. Muestrame 5 ejemplos de como crees que es una descripcion de producto ideal.\n"
    "Responde en formato de lista  y entrega la respuesta final como un prompt reutilizable para otro LLM, encerrado entre triple comilla (''')."
)
#Recupera los fragmentos más relevantes usando el retriever
docs_relevantes = retriever.get_relevant_documents(query)
#Junta los fragmentos en un solo contexto
contexto = "\n".join([doc.page_content for doc in docs_relevantes])
# Prepara el prompt para el LLM
prompt = f"""Usa el siguiente contexto para responder la pregunta de forma precisa y detallada.
Contexto:
{contexto}
Pregunta: {query}
Respuesta:"""

#test
respuesta = llm.invoke(prompt)
print("Respuesta generada por el LLM:")
print(respuesta.content)