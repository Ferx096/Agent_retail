import requests
import os

def generate_image(prompt, api_token):
    api_url = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2-1"
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
        images_dir = os.path.join(os.path.dirname(__file__), "images")
        os.makedirs(images_dir, exist_ok=True)
        image_path = os.path.join(images_dir, "imagen_generada.png")
        with open(image_path, "wb") as f:
            f.write(response.content)
        print(f"Imagen guardada como {image_path}")
        return image_path
    else:
        print("Error:", response.status_code, response.text)
        return None

if __name__ == "__main__":
    # Reemplaza con tu token de Hugging Face
    API_TOKEN = "tu_token_aqui"
    prompt = "Snacks saludables, empaque colorido, fondo blanco, estilo moderno, luz natural"
    generate_image(prompt, API_TOKEN)
