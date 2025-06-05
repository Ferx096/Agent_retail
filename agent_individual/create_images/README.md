# Carpeta `create_images`

Esta carpeta contiene los módulos y scripts relacionados con la generación automática de imágenes a partir de descripciones de texto, utilizando modelos de inteligencia artificial alojados en Hugging Face. Es parte del agente individual del sistema de estrategia retail.

## Estructura de la carpeta

- **generate_image.py**: Script principal para generar imágenes a partir de un prompt de texto usando la API de Hugging Face. Permite guardar las imágenes generadas en la subcarpeta `images`.
- **deployment_images.py**: Aplicación web desarrollada con Streamlit que permite a los usuarios ingresar un prompt desde una interfaz gráfica y obtener la imagen generada, la cual también se guarda localmente.
- **test_generate_image.py**: Script de prueba para validar la generación de imágenes y la integración con la API de Hugging Face.
- **images/**: Carpeta donde se almacenan las imágenes generadas automáticamente por los scripts.
- **__init__.py**: Archivo para marcar la carpeta como un módulo de Python.

## Funcionamiento general

1. **Entrada de texto (prompt):** El usuario proporciona una descripción textual de la imagen que desea generar.
2. **Generación de imagen:** El sistema utiliza modelos de difusión o similares alojados en Hugging Face para crear una imagen basada en el prompt.
3. **Almacenamiento:** Las imágenes generadas se guardan automáticamente en la subcarpeta `images`.
4. **Interfaz web (opcional):** A través de `deployment_images.py` y Streamlit, se puede interactuar con el generador de imágenes desde el navegador.

## Requisitos
- Python 3.8+
- Dependencias: `huggingface_hub`, `streamlit`, `Pillow`, y otras listadas en `requirements.txt`.
- Token de Hugging Face con permisos para usar los modelos de generación de imágenes.

## Notas
- Es posible que algunos modelos requieran créditos pagos en Hugging Face.
- El archivo `.env` debe contener el token de acceso bajo la variable `API_TOKEN_HUGGINGFACE`.


## Ejecución de la interfaz web (Streamlit)

Para lanzar la aplicación web y generar imágenes desde el navegador, ejecuta el siguiente comando desde la raíz del proyecto o desde esta carpeta:

```bash
streamlit run deployment_images.py
```

Si estás en la raíz del proyecto, usa la ruta relativa:

```bash
streamlit run agent_individual/create_images/deployment_images.py
```

Esto abrirá una interfaz web donde podrás ingresar el prompt y generar imágenes de forma interactiva.

---

**Autor:** Ferx096 / Equipo de retail_strategy
