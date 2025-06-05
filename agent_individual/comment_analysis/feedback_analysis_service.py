import streamlit as st
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
import logging
from config import get_llm

llm = get_llm()

# Configuración de logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')
logger = logging.getLogger(__name__)

openai.api_key = os.getenv('OPENAI_API_KEY')

app = FastAPI(title="Microservicio de Análisis de Comentarios de productos")

class ComentariosRequest(BaseModel):
    comentarios: List[str]

class ComentarioClasificado(BaseModel):
    comentario: str
    clasificacion: str
    justificacion: str

class AnalisisRespuesta(BaseModel):
    clasificados: List[ComentarioClasificado]
    resumen: str

def analizar_lote(lote: List[str]) -> Dict[str, Any]:
    prompt = (
        "Eres un analista experto en feedback de clientes. Para cada comentario, clasifícalo como POSITIVO, NEGATIVO o NEUTRO y justifica brevemente la clasificación. "
        "Después, genera un resumen ejecutivo de los principales temas y problemas detectados en este lote. "
        "Responde en formato JSON con dos claves: 'clasificados' (lista de objetos con 'comentario', 'clasificacion', 'justificacion') y 'resumen' (string).\n"
        "Comentarios:\n" + "\n".join([f"{i+1}. {c}" for i, c in enumerate(lote)])
    )
    logger.info(f"Enviando lote de {len(lote)} comentarios a OpenAI...")
    response = llm.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=900
    )
    text = response.choices[0].message['content']
    logger.info(f"Respuesta recibida de OpenAI para lote: {text[:200]}...")
    match = re.search(r'\{.*\}', text, re.DOTALL)
    if match:
        try:
            return json.loads(match.group())
        except Exception as e:
            logger.error(f"Error al parsear JSON: {e}")
    logger.warning("No se pudo extraer JSON, devolviendo texto completo como resumen.")
    return {"clasificados": [], "resumen": text}

def procesar_comentarios(comentarios: List[str], batch_size: int = 10, max_workers: int = 4):
    lotes = [comentarios[i:i+batch_size] for i in range(0, len(comentarios), batch_size)]
    resultados = []
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        resultados = list(executor.map(analizar_lote, lotes))
    clasificados = []
    resumenes = []
    for r in resultados:
        clasificados.extend(r.get("clasificados", []))
        resumenes.append(r.get("resumen", ""))
    logger.info(f"Total de comentarios clasificados: {len(clasificados)}")
    return {"clasificados": clasificados, "resumen": "\n".join(resumenes)}

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
