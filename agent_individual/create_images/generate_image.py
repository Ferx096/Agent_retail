import logging
import sys
import os
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
    provider="nscale",
    api_key=api_token,
)

# output is a PIL.Image object
image = client.text_to_image(
    "Astronaut riding a horse",
    model="black-forest-labs/FLUX.1-dev",
)

images_dir = "images"
os.makedirs(images_dir, exist_ok=True)
# Nombre del archivo (ej: imagen_20250604_1452.png)
filename = f"imagen_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
image_path = os.path.join(images_dir, filename)
image.save(image_path)
print(f"✅ Imagen guardada en: {image_path}")




