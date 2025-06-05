import logging
import sys
import os
# Agrega la raíz del proyecto al sys.path
ROOT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
if ROOT_PATH not in sys.path:
    sys.path.insert(0, ROOT_PATH)
import requests
from PIL import Image
from io import BytesIO
from config import HUGGING


# 1. Tu token personal de Hugging Face
api_token = HUGGING['api']

# 2. Model ID sacado de Hugging Face
model_id = "stabilityai/stable-diffusion-2"

# 3. URL de inferencia
API_URL = f"https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2"

# 4. Prompt descriptivo
prompt = "Un empaque de snacks saludables, diseño moderno y minimalista, colores verde y blanco, fondo blanco con luz natural, frutas frescas, estilo fotográfico profesional"
# 5. Headers de autenticación
headers = {"Authorization": f"Bearer {api_token}"}
# 6. Función para llamar a la API
def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    if response.status_code == 200:
        return response.content
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None
# 7. Llamada a la API
image_bytes = query({"inputs": prompt})
# 8. Mostrar/guardar imagen
if image_bytes:
    image = Image.open(BytesIO(image_bytes))
    image.show()
    # Crear carpeta si no existe
    images_dir = "images"
    os.makedirs(images_dir, exist_ok=True)
    # Nombre del archivo (ej: imagen_20250604_1452.png)
    filename = f"imagen_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    image_path = os.path.join(images_dir, filename)
    image.save(image_path)
    print(f"✅ Imagen guardada en: {image_path}")
