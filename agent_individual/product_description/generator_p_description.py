import logging
import sys
import os
from datetime import datetime
# Agrega la raíz del proyecto al sys.path
ROOT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
if ROOT_PATH not in sys.path:
    sys.path.insert(0, ROOT_PATH)
from langgraph.graph import StateGraph, END
from langgraph.graph.message import add_messages
from typing import TypedDict, Annotated
from langchain_core.runnables import RunnableLambda
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.messages import AIMessage
from typing import Optional
from config import get_llm
from rag_product_description.prompt import prompt_snack

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
llm = get_llm()

# Define graph state
class GraphState(TypedDict):
    """
    Condiciones o datos mínimos necesarios para generar una descripción precisa
    """
    messages: Annotated[list, add_messages]
    query: Optional[str]
    snack_type: str
    main_ingredients: str
    nutritional_benefits: str
    available_flavors: str
    target_audience: str
    key_differentiator: str
    allergen_certifications: str
    next:Optional[str]

def input_collector(state: GraphState) -> GraphState:
    """
    Recolecta la informacion de input
    """
    return state

def validate_input(state: GraphState) -> dict:
    if state['target_audience']  in ['niños', 'adultos', 'deportistas', 'jovenes', 'edad avanzada'] and  state['snack_type']  in ['barra', 'cereal', 'galleta', 'chips']:
        return {"next": "generate_reply"}
    return {"next": END}

def generate_reply(state: GraphState) -> GraphState:
    """Generador de respuesta (descripcion de producto en base al prompt)"""
    base_context = prompt_snack
    prompt = (
        f"Usar (Tipo de snack: {state['snack_type']}, Ingredientes Pricipales: {state['main_ingredients']}, Beneficios Nutricionales: {state['nutritional_benefits']}, Sabores Disponibles: {state['available_flavors']}, Publico Objetivo: {state['target_audience']}, Diferenciador clave: {state['key_differentiator']}, Alergenos y/o certificaciones: {state['allergen_certifications']}): {state['query']}\n"
        f"Generar una respuesta basada en todas las instrucciones en {base_context}. La respuesta debe contener la funcion de generacion automática de descripciones de producto."
    )
    #generar respuesta
    response = llm.invoke(prompt)
    logging.info('Descripcion de producto generada')
    #validad respuesta
    reply = response.content if hasattr(response, "content") else response
    logging.info('Validar informacion')
    #Añadir respeusta a los mensajes
    state["messages"].append(AIMessage(content=reply))
    return state

def node_end(state: GraphState) -> None:
    """ Nodo final, no hace nada o solo marca fin"""
    logging.info('Proceso finalizado')
    return None

# ==================
# ORQUESTACION
# ==================
graph = StateGraph(GraphState)
graph.add_node("input", input_collector)
graph.add_node("validate_input", validate_input)
graph.add_node("reply", generate_reply)
graph.add_node("end", node_end)
graph.set_entry_point("input")
graph.add_edge("input", "validate_input")
graph.add_edge("validate_input", "reply") 
graph.add_edge("reply", "end")  # FIN

app = graph.compile()