# Agentes Individuales para Estrategia Retail

Este directorio contiene los agentes individuales desarrollados para automatizar tareas clave en el sector retail, cada uno especializado en un dominio específico: análisis de comentarios de usuarios, generación de imágenes promocionales y creación de descripciones de productos. Cada agente es autónomo, pero están diseñados para ser integrados en una futura arquitectura multiagente.

---

## Estructura de Carpetas

- **comment_analysis/**: Microservicio FastAPI + Streamlit para análisis masivo y en vivo de comentarios de usuarios usando Azure OpenAI vía LangChain. Devuelve resúmenes ejecutivos en texto plano.
- **create_images/**: Scripts y app Streamlit para generar imágenes promocionales a partir de descripciones de texto usando modelos de Hugging Face.
- **product_description/**: Agente y app Gradio para generar descripciones de productos a partir de atributos clave, usando IA y flujos LangGraph.

---

## Funcionalidad de cada agente

### 1. Análisis de Comentarios (`comment_analysis`)
- **Propósito**: Analizar grandes volúmenes de comentarios de clientes, clasificarlos y extraer un resumen ejecutivo de los principales temas detectados.
- **Tecnologías**: FastAPI, LangChain (Azure OpenAI), Streamlit, logging, concurrencia.
- **Salida**: Texto plano con el resumen del análisis, listo para ser mostrado o integrado en reportes.

### 2. Generación de Imágenes (`create_images`)
- **Propósito**: Crear imágenes promocionales automáticamente a partir de prompts de texto, facilitando campañas de marketing visual.
- **Tecnologías**: Python, Hugging Face, Streamlit, Pillow.
- **Salida**: Imágenes generadas y almacenadas localmente, con opción de visualización web.

### 3. Descripción de Productos (`product_description`)
- **Propósito**: Generar descripciones atractivas y personalizadas para productos retail, a partir de atributos y beneficios clave.
- **Tecnologías**: Python, Gradio, LangGraph, IA generativa.
- **Salida**: Texto descriptivo optimizado para catálogos, e-commerce o marketing.

---

## Visión a Futuro: Multiagente

La arquitectura está pensada para una segunda fase donde estos agentes individuales se integrarán en un sistema multiagente. Esto permitirá:
- **Orquestación inteligente**: Un agente coordinador podrá delegar tareas a los agentes especializados según el flujo de negocio.
- **Interacción entre agentes**: Por ejemplo, el análisis de comentarios puede alimentar la generación de nuevas imágenes o descripciones de producto adaptadas a tendencias detectadas.
- **Escalabilidad y modularidad**: Cada agente puede evolucionar de forma independiente y ser reutilizado en distintos contextos.

---

## Ejemplo de flujo multiagente (Fase 2)

1. El usuario sube comentarios y atributos de producto.
2. El agente de análisis detecta tendencias y problemas.
3. El agente de imágenes genera creatividades alineadas con los insights.
4. El agente de descripciones adapta el copywriting a los hallazgos.
5. Todo el flujo es orquestado y trazado automáticamente.

---

**Desarrollado por Ferx096 / Equipo retail_strategy.**
