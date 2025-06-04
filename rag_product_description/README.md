# Guía de Trabajo para la Carpeta `rag_product_description`

Este documento describe el flujo de trabajo y la función de cada archivo en la carpeta `rag_product_description` para facilitar el desarrollo y mantenimiento del sistema RAG (Retrieval-Augmented Generation) aplicado a descripciones de productos.

## Estructura de la Carpeta

- `extract_fragment.py`: Descarga un PDF, extrae un fragmento de texto relevante entre delimitadores y lo imprime. Este fragmento es la base para el procesamiento posterior.
- `prompt.py`: Contiene plantillas (prompts) para la generación de descripciones de productos saludables, así como ejemplos y condiciones mínimas requeridas.
- `rag.py`: Implementa el flujo principal RAG. Utiliza el fragmento extraído, lo divide en partes, lo indexa en FAISS, recupera los fragmentos relevantes y genera un prompt para un LLM, mostrando la respuesta generada.
- `document/`: Carpeta donde se almacenan los documentos PDF descargados y procesados.
- `__init__.py`: Archivo de inicialización del módulo.

## Flujo de Trabajo Sugerido

1. **Extracción de Fragmento**
   - Ejecuta `extract_fragment.py` para descargar y extraer el texto relevante del PDF. El resultado se imprime y puede ser importado por otros módulos.

2. **Definición de Prompts**
   - Modifica o añade prompts en `prompt.py` según la categoría o subcategoría de producto que se desee trabajar.

3. **Procesamiento RAG**
   - Ejecuta `rag.py` para:
     - Dividir el fragmento extraído en partes manejables.
     - Indexar los fragmentos usando FAISS.
     - Recuperar los fragmentos más relevantes según la consulta.
     - Generar y mostrar un prompt reutilizable para LLMs.

4. **Personalización y Pruebas**
   - Ajusta los parámetros de fragmentación, prompts y consultas según los resultados obtenidos y las necesidades del proyecto.

## Notas
- Mantén los archivos y la estructura organizados para facilitar la colaboración.
- No olvides actualizar este README si se agregan o modifican archivos relevantes en el flujo de trabajo.
- No hagas push de los cambios sin autorización.
