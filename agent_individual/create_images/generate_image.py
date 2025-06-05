import logging
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__) + '/../'))
import requests
from config import HUGGING
git addlogging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


api_token = HUGGING['api']
api_url = HUGGING['api_url']
def generate_image(prompt, filename="imagen_generada.png"):
    headers = {
        "Authorization": f"Bearer {api_token}",
        "Accept": "application/json"
    }
    response = requests.post(
        api_url,
        headers=headers,
        json={"inputs": prompt}
    )
    if response.status_code == 200:
        images_dir = "images"
        os.makedirs(images_dir, exist_ok=True)
        image_path = os.path.join(images_dir, filename)
        with open(image_path, "wb") as f:
            f.write(response.content)
        print(f"Imagen guardada en {image_path}")
        return image_path
    else:
        print("Error:", response.status_code, response.text)
        return None




