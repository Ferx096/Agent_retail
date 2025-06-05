import streamlit as st
import logging
import sys
import os
from datetime import datetime
# Agrega la raíz del proyecto al sys.path
ROOT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
if ROOT_PATH not in sys.path:
    sys.path.insert(0, ROOT_PATH)
from huggingface_hub import InferenceClient
from config import HUGGING

# Configuración de la página
st.set_page_config(page_title="Generador de Imágenes", layout="centered")

# Título
st.title("🅰️ Generador de Imágenes Promocionales con Hugging Face")

# Campo de texto para el prompt
prompt = st.text_area(
    "Describe la imagen que quieres generar en base a la promocion:",
    value="Un empaque de snacks saludables, diseño moderno y minimalista, colores verde y blanco, fondo blanco con luz natural, frutas frescas, estilo fotográfico profesional"
)

# Botón para generar la imagen
if st.button("Generar imagen"):
    with st.spinner("Generando imagen..."):
        api_token = HUGGING['api']
        client = InferenceClient(api_key=api_token)
        try:
            image = client.text_to_image(
                prompt,
                model="black-forest-labs/FLUX.1-dev",
            )
            # Guardar la imagen en la carpeta images al lado del script
            script_dir = os.path.dirname(os.path.abspath(__file__))
            images_dir = os.path.join(script_dir, "images")
            os.makedirs(images_dir, exist_ok=True)
            filename = f"imagen_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
            image_path = os.path.join(images_dir, filename)
            image.save(image_path)
            st.success(f"Imagen generada y guardada en: {image_path}")
            st.image(image, caption="Imagen generada", use_column_width=True)
        except Exception as e:
            st.error(f"Ocurrió un error: {e}")