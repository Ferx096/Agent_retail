import logging
import sys
import os
from datetime import datetime
# Agrega la raíz del proyecto al sys.path
ROOT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
if ROOT_PATH not in sys.path:
    sys.path.insert(0, ROOT_PATH)
import requests
from huggingface_hub import InferenceClient
from config import HUGGING

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
# 1. Tu token personal de Hugging Face
api_token = HUGGING['api']

import os

client = InferenceClient(
    api_key=api_token,
)
#prompt
prompt = "Un empaque de snacks saludables, diseño moderno y minimalista, colores verde y blanco, fondo blanco con luz natural, frutas frescas, estilo fotográfico profesional"
# output is a PIL.Image object
image = client.text_to_image(
    prompt,
    model="black-forest-labs/FLUX.1-dev",
)

# Obtiene la ruta absoluta del directorio donde está este script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Define la ruta de la carpeta images al mismo nivel que el script
images_dir = os.path.join(script_dir, "images")
os.makedirs(images_dir, exist_ok=True)

# Define el nombre del archivo
filename = f"imagen_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
image_path = os.path.join(images_dir, filename)

# Guarda la imagen
image.save(image_path)
print(f"✅ Imagen guardada en: {image_path}")




