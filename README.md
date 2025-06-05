# retail_strategy: Plataforma Modular de Automatización para Retail

Este proyecto implementa una arquitectura modular para automatizar procesos clave en el sector retail, combinando técnicas de RAG (Retrieval-Augmented Generation) para enriquecer prompts y una colección de agentes inteligentes especializados. El objetivo es optimizar la generación de contenido, el análisis de feedback y la creatividad visual, todo orquestado para adaptarse dinámicamente a las necesidades del negocio.

---

## Objetivo General

Desarrollar una plataforma escalable que permita:
- Enriquecer y personalizar prompts mediante RAG, integrando información relevante de fuentes internas y externas.
- Delegar tareas específicas a agentes inteligentes (análisis de comentarios, generación de imágenes, descripciones de producto).
- Orquestar flujos multiagente para campañas, lanzamientos y análisis de tendencias en retail.

---

## Guía de funcionamiento

### 1. Enriquecimiento de Prompts con RAG
- El sistema utiliza RAG para buscar información relevante (por ejemplo, tendencias, datos de productos, feedback histórico) y enriquecer los prompts enviados a los modelos generativos.
- Esto asegura que los agentes trabajen siempre con contexto actualizado y específico del negocio.

### 2. Agentes Especializados
- **Análisis de Comentarios**: Microservicio FastAPI + Streamlit que analiza grandes volúmenes de feedback de clientes y genera resúmenes ejecutivos en texto plano usando Azure OpenAI.
- **Generación de Imágenes**: Scripts y app Streamlit para crear imágenes promocionales a partir de descripciones, usando modelos de Hugging Face.
- **Descripción de Productos**: Agente y app Gradio para generar descripciones de productos personalizadas a partir de atributos clave.

Cada agente es autónomo, pero están diseñados para integrarse en flujos multiagente.

### 3. Orquestación Multiagente (Fase 2)
- El sistema permitirá que los agentes interactúen entre sí, por ejemplo:
    - El análisis de comentarios detecta tendencias.
    - El generador de imágenes crea creatividades alineadas con los insights.
    - El generador de descripciones adapta el copywriting a los hallazgos.
- Todo el flujo será trazable y escalable.

---

## Estructura del repositorio

- `agent_individual/`: Contiene los agentes individuales y sus submódulos.
    - `comment_analysis/`: Análisis de comentarios y feedback.
    - `create_images/`: Generación automática de imágenes.
    - `product_description/`: Generación de descripciones de producto.
- (Próximamente) `rag/`: Módulos y utilidades para RAG y enriquecimiento de prompts.

---

## Ejemplo de flujo completo

1. El usuario o sistema solicita una campaña o análisis.
2. El módulo RAG busca y agrega contexto relevante al prompt.
3. Los agentes especializados procesan la solicitud (análisis, imágenes, descripciones).
4. El resultado se integra y presenta en una interfaz web o se exporta para uso en campañas.

---

**Desarrollado por Ferx096 / Equipo retail_strategy.**
