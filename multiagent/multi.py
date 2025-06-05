import logging
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__) + '/../'))
import requests
from langgraph.graph import StateGraph, END
from langgraph.graph.message import add_messages
from typing import TypedDict, Annotated
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.messages import AIMessage
from typing import Optional
from config import HUGGING

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


# Define graph state
class GraphState(TypedDict):
    """
    Condiciones o datos mínimos necesarios para generar una descripción precisa
    """
    packaging_color: str
    background_color: str
    visual_style: str
    lighting: str
    environment: str
    next:Optional[str]

def input_collector(state: GraphState) -> GraphState:
    """
    Recolecta la informacion de input
    """
    return state

def validate_input(state: GraphState) -> dict:
    if state['lighting']  in ['natural', 'brillante']
        return {"next": "generate_reply"}
    return {"next": END}


def generate_image(prompt):
    api_url = HUGGING["api_url"]
    headers = {
        "Authorization": f"Bearer  {HUGGING["api"]}",
        "Accept": "application/json"
    }
    response = requests.post(
        api_url,
        headers=headers,
        json={"inputs": prompt}
    )
    if response.status_code == 200:
        images_dir = os.path.join(os.path.dirname(__file__), "images")
        os.makedirs(images_dir, exist_ok=True)
        image_path = os.path.join(images_dir, "imagen_generada.png")
        with open(image_path, "wb") as f:
            f.write(response.content)
        print(f"Imagen guardada como {image_path}")
        return image_path
    else:
        print("Error:", response.status_code, response.text)
        return None

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
graph.add_node("reply", generate_image)
graph.add_node("end", node_end)
graph.set_entry_point("input")
graph.add_edge("input", "validate_input")
graph.add_edge("validate_input", "reply") 
graph.add_edge("reply", "end")  # FIN

app = graph.compile()

