import os
import gradio as gr
import uuid
from generator_p_description import app

os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"


#FUNCION PRINCIPAL DEL CHATBOT
def run_chatbot(snack_type, main_ingredients, nutritional_benefits, available_flavors, target_audience, key_differentiator, allergen_certifications, query):
    #Prepare entrada de chatbot = 
    try:
        input_state = {
            "query":query, 
            "Tipo de snack": snack_type, 
            "Ingredientes principales": main_ingredients, 
            "Beneficios nutricionales":nutritional_benefits, 
            "Sabores disponibles":available_flavors, 
            "Publico objetivo":target_audience, 
            "Diferenciador clave":key_differentiator, 
            "Alergenos y/o certificaciones":allergen_certifications, 
            "messages": []
            }
        
        result = app.invoke(input_state)
        reply = result["messages"][-1].content if result["messages"] else "No se genero respuesta."
        return reply
    except Exception as e:
        return f"⚠️ Error occurred: {str(e)}"


#INTERFACE
with gr.Blocks(theme=gr.themes.Glass()) as demo:
    gr.Markdown(
    """
    <h1 style='text-align: center; font-size: 3em;'>🅰️ <strong>AGENTE GENERADOR DE DESCRIPCION DE PRODUCTO - RETAIL</strong></h1>
    <p style='text-align: center;'>Generador experto de descripciones de producto, Ingresa las condiciones en la columna izquierda 👈🏼 </p>
    """,
        elem_id="title-centered",
    )

    with gr.Row():
        with gr.Column():
            snack_type = gr.Dropdown(choices=['barra', 'cereal', 'galleta', 'chips'], label="Tipo de snack")
            main_ingredients = gr.Textbox(lines=2, label="Ingredientes principales (naturales, orgánicos, etc.)")
            nutritional_benefits = gr.Textbox(lines=2, label="Beneficios Nutricionales (bajo en calorías, alto en fibra, sin azúcar, etc.)")
            available_flavors = gr.Textbox(lines=2, label="Sabores disponibles")
            target_audience = gr.Radio(choices=['niños', 'adultos', 'deportistas', 'jovenes', 'edad avanzada'], label="Publico Objetivo")           
            key_differentiator = gr.Textbox(lines=2, label="Diferenciador clave (más relleno, sin conservadores, empaque ecológico, etc.)")
            allergen_certifications = gr.Textbox(lines=2, label="Alergenos y/o certificaciones (sin gluten, vegano, etc.)")
            query = gr.Textbox(lines=2, label="💬 Consulta adicional opcional")

            btn = gr.Button("Enviar")

        with gr.Column():
            output_text = gr.Textbox(label="📜 Descripcion de producto")

    btn.click(
        fn=run_chatbot,
        inputs=[snack_type, main_ingredients, nutritional_benefits, available_flavors, target_audience, key_differentiator, allergen_certifications, query],
        outputs=[output_text],
    )

demo.launch()