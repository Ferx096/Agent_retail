import os
import logging
from dotenv import load_dotenv
import requests
import pdfplumber
import openai
import faiss
import numpy as np

# Configuración de logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# 1. Descargar el PDF desde el enlace web y guardarlo en la carpeta document
pdf_url = "https://www.alicorp.com.pe/media/PDF/memoria_anual_2023.pdf"
document_folder = "document"
os.makedirs(document_folder, exist_ok=True)
local_pdf = os.path.join(document_folder, "memoria_anual_2023.pdf")

if not os.path.exists(local_pdf):
    logging.info("Descargando PDF...")
    response = requests.get(pdf_url)
    with open(local_pdf, "wb") as f:
        f.write(response.content)
    logging.info("PDF descargado en: %s", local_pdf)
    

# 2. Extraer el fragmento entre los textos delimitadores
start_page = 21  # Página 22 (índice base 0)
end_page = 28    # Página 29 (índice base 0)

start_text = "A. NEGOCIO DE CONSUMO MASIVO"
end_text = """Además, logra excelentes
resultados de indicadores digitales, como un sentiment positivo del 89% y un VTR (view-
through rate) del 45% en Youtube."""

with pdfplumber.open(local_pdf) as pdf:
    fragmento = ""
    for i in range(start_page, end_page + 1):
        page = pdf.pages[i]
        page_text = page.extract_text()
        if page_text:
            fragmento += page_text + "\n"

#Seleccionar texto exclusivo para el embeddings
start_idx = fragmento.find(start_text)
end_idx = fragmento.find(end_text)

if start_idx == -1 or end_idx == -1:
    raise ValueError("No se encontraron los textos delimitadores en el PDF extraído.")

end_idx += len(end_text)
fragmento_deseado = fragmento[start_idx:end_idx]
print(fragmento_deseado)
