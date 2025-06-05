# Microservicio de Análisis de Comentarios de Usuarios

Este módulo implementa un microservicio escalable para el análisis masivo y en vivo de comentarios de usuarios sobre productos, utilizando Azure OpenAI vía LangChain y una interfaz de visualización con Streamlit. El sistema está diseñado para ser trazable, eficiente y fácil de probar.

## Estructura de archivos

- `feedback_analysis_service.py`: Microservicio FastAPI que expone el endpoint `/analizar` para procesar lotes de comentarios y devolver un resumen ejecutivo en texto plano.
- `deployment_feedback.py`: Aplicación Streamlit que permite cargar comentarios manualmente o desde CSV, enviarlos al microservicio y mostrar el resumen generado.
- `__init__.py`: Inicialización del módulo.

## feedback_analysis_service.py

### Propósito
Expone un endpoint REST `/analizar` que recibe una lista de comentarios, los analiza usando Azure OpenAI (vía LangChain) y retorna un resumen ejecutivo en texto plano, sin estructuras JSON ni tablas.

### Componentes principales
- **FastAPI**: Framework para exponer el microservicio.
- **Pydantic**: Validación de datos de entrada y salida.
- **ThreadPoolExecutor**: Permite el análisis concurrente de lotes grandes de comentarios.
- **Logging**: Trazabilidad completa de cada solicitud y respuesta.
- **Extracción robusta del resumen**: El sistema extrae el texto plano del campo `content` de la respuesta de Azure OpenAI, desescapando caracteres para mostrar el resumen limpio.

### Flujo principal
1. **Recibe una lista de comentarios** (vía POST `/analizar`).
2. **Genera un prompt** para el modelo, pidiendo análisis y resumen solo en texto libre.
3. **Invoca Azure OpenAI** usando LangChain.
4. **Extrae el resumen** del campo `content` (si existe) y lo desescapa para evitar artefactos de serialización.
5. **Devuelve** `{ "resumen": <texto plano> }`.

### Ejemplo de uso
```bash
curl -X POST http://localhost:8000/analizar -H 'Content-Type: application/json' -d '{"comentarios": ["Muy buen producto", "No me gustó"]}'
```
Respuesta:
```json
{"resumen": "En este lote de comentarios se identifican opiniones polarizadas..."}
```

## deployment_feedback.py

### Propósito
Permite a usuarios cargar comentarios manualmente o desde un archivo CSV, enviarlos al microservicio y visualizar el resumen ejecutivo en texto plano.

### Componentes principales
- **Streamlit**: Interfaz web para pruebas y visualización.
- **requests**: Comunicación HTTP con el microservicio FastAPI.
- **pandas**: Soporte para carga de archivos CSV.
- **Logging**: Registro de eventos y errores.

### Flujo principal
1. El usuario ingresa comentarios manualmente o sube un CSV.
2. Al presionar "Analizar comentarios", los comentarios se envían al endpoint `/analizar`.
3. Se muestra el resumen recibido en texto plano.

### Ejemplo de uso
- Ejecutar con:
```bash
streamlit run deployment_feedback.py --server.port 53239 --server.address 0.0.0.0
```
- Acceder vía navegador a `http://localhost:53239`

## Consideraciones técnicas
- **No se utiliza la API estándar de OpenAI**: Solo Azure OpenAI vía LangChain.
- **Respuesta solo en texto plano**: Para evitar problemas de parseo y simplificar la integración.
- **Escalabilidad**: Soporta análisis concurrente de grandes volúmenes de comentarios.
- **Trazabilidad**: Todo el flujo está instrumentado con logging.

## Ejemplo de integración end-to-end
1. El usuario carga comentarios en Streamlit.
2. Streamlit los envía al microservicio FastAPI.
3. FastAPI procesa y retorna un resumen limpio.
4. El usuario visualiza el resumen en la interfaz web.

---

**Desarrollado para análisis masivo y en vivo con Azure OpenAI, LangChain, FastAPI y Streamlit.**
