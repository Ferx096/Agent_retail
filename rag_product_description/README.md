# **Guía de Trabajo para la Carpeta `rag_product_description`**

Este documento describe el flujo de trabajo y la función de cada archivo en la carpeta `rag_product_description` para facilitar el desarrollo y mantenimiento del sistema RAG (Retrieval-Augmented Generation) aplicado a descripciones de productos.

El objetivo de esta carpeta es obtener información veraz, precisa, real y estructurada sobre el formato y los requisitos necesarios para generar descripciones de productos.

*Fuente:*  Memoria anual de alicorp 2023  [📄](https://www.alicorp.com.pe/media/PDF/memoria_anual_2023.pdf)

---
## Estructura de la Carpeta

- `extract_fragment.py`: Descarga un PDF de una pagian web, extrae un fragmento de texto relevante entre delimitadores y lo imprime. Este fragmento es la base para el procesamiento posterior.
- `rag.py`: Implementa el flujo principal RAG. Utiliza el fragmento extraído, lo divide en partes, lo indexa en FAISS, recupera los fragmentos relevantes y genera un prompt para un LLM, mostrando la respuesta generada.
- `prompt.py`: Contiene plantillas (prompts) para la generación de descripciones de productos saludables, así como ejemplos y condiciones mínimas requeridas. Esta plantilla fue generada por el flujo RAG del codigo `rag.py`.
- `document/`: Carpeta donde se almacenan los documentos PDF descargados y procesados por `extract_fragment.py`
- `__init__.py`: Archivo de inicialización del módulo.

---
## Flujo de Trabajo Sugerido

1. **Extracción de Fragmento**
   - Ejecuta `extract_fragment.py` para descargar de la pagina web y extraer el texto relevante del PDF. El resultado se imprime y puede ser importado por otros módulos.

2. **Procesamiento RAG**
   - Ejecuta `rag.py` para:
     - Dividir el fragmento extraído en partes manejables.
     - Indexar los fragmentos usando FAISS.
     - Recuperar los fragmentos más relevantes según la consulta.
     - Generar y mostrar un prompt reutilizable para LLMs.
       
3. **Definición de Prompts**
   - Traslado el prompt genrado por rag.py en `prompt.py` según la categoría o subcategoría de producto que se desee trabajar.

4. **Personalización y Pruebas**
   - Ajusta los parámetros de fragmentación, prompts y consultas según los resultados obtenidos y las necesidades del proyecto.

---
## MEJORAS:

Por el momento solo nos enfocaremos en usar 1 prompt relacionado al Consumo Masivo - alimentos (snack saludable).
En un futuro se se piensa personalizar prompt por cada categoriga general tal como lo plantea la pagina principal de ALICORP :

1. `CONSUMO MASIVO`

2. `ALICORP SOLUCIONES B2B`

3. `ACUICULTURA`

4. `INDUSTRIAS DEL ESPINO`

Tambien añadir cada prompt por subcategoria y clase por ejemplo en `CONSUMO MASIVO`:

- Alimentos:
  
      - aceites
  
		- salsas
  
		- fideos
  
		- galletas
  
- Cuidado del hogar:
  
      - detergentes
  
		- Jabón de lavar
  
		- lejías
  
		- lavavajillas
  
- Cuidado personal

*FUENTE*: [🅰️](https://www.alicorp.com.pe/pe/es/productos/consumo-masivo)
