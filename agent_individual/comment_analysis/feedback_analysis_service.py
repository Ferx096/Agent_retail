import logging
import sys
import os
from datetime import datetime
# Agrega la raíz del proyecto al sys.path
ROOT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
if ROOT_PATH not in sys.path:
    sys.path.insert(0, ROOT_PATH)

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Any
from concurrent.futures import ThreadPoolExecutor
import re
import json
from config import get_llm

llm = get_llm()

# Configuración de logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')
logger = logging.getLogger(__name__)

app = FastAPI(title="Microservicio de Análisis de Comentarios de productos")

class ComentariosRequest(BaseModel):
    comentarios: List[str]

class AnalisisRespuesta(BaseModel):
    resumen: str

def analizar_lote(lote: List[str]) -> Dict[str, Any]:
    prompt = (
        "Eres un analista experto en feedback de clientes. Analiza los siguientes comentarios, clasifica cada uno como POSITIVO, NEGATIVO o NEUTRO y justifica brevemente cada clasificación. "
        "Luego, genera un resumen ejecutivo de los principales temas y problemas detectados. "
        "Responde TODO en texto libre, NO en formato JSON.\n"
        "Comentarios:\n" + "\n".join([f"{i+1}. {c}" for i, c in enumerate(lote)])
    )
    logger.info(f"Enviando lote de {len(lote)} comentarios a Azure OpenAI...")
    text = llm.invoke(prompt)
    logger.info(f"Respuesta recibida de Azure OpenAI para lote: {str(text)[:200]}...")
    # Si la respuesta viene como objeto con content, extraerlo
    # Si la respuesta es un string que contiene content='...', extraerlo
    import re
    if isinstance(text, str):
        match = re.search(r"content='(.*?)'", text, re.DOTALL)
        if match:
            # Desescapar el string para mostrarlo limpio
            import codecs
            resumen_limpio = match.group(1)
            try:
                resumen_limpio = resumen_limpio.encode('utf-8').decode('unicode_escape')
            except Exception:
                pass
            return {"resumen": resumen_limpio}
    if hasattr(text, 'content'):
        return {"resumen": str(text.content)}
    if isinstance(text, dict) and 'content' in text:
        return {"resumen": str(text['content'])}
    return {"resumen": str(text)}


def procesar_comentarios(comentarios: List[str], batch_size: int = 10, max_workers: int = 4):
    lotes = [comentarios[i:i+batch_size] for i in range(0, len(comentarios), batch_size)]
    resultados = []
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        resultados = list(executor.map(analizar_lote, lotes))
    resumenes = [r.get("resumen", "") for r in resultados]
    return {"resumen": "\n".join(resumenes)}

@app.post("/analizar", response_model=AnalisisRespuesta)
def analizar_endpoint(request: ComentariosRequest):
    if not request.comentarios:
        logger.warning("Solicitud recibida sin comentarios.")
        raise HTTPException(status_code=400, detail="No se recibieron comentarios.")
    try:
        logger.info(f"Procesando solicitud con {len(request.comentarios)} comentarios...")
        resultado = procesar_comentarios(request.comentarios)
        logger.info("Análisis completado correctamente.")
        return resultado
    except Exception as e:
        logger.error(f"Error en el análisis: {e}")
        raise HTTPException(status_code=500, detail=str(e))
