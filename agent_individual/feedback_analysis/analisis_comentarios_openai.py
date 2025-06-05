import os
import pandas as pd
import openai

# Cargar comentarios desde CSV
df = pd.read_csv('comentarios.csv')

# Configurar API Key de OpenAI (usa variable de entorno OPENAI_API_KEY)
openai.api_key = os.getenv('OPENAI_API_KEY')

# Función para analizar sentimiento y extraer resumen/temas

def analizar_comentarios(comentarios):
    prompt = (
        "Eres un analista de feedback de clientes. Analiza los siguientes comentarios de usuarios sobre un producto. "
        "Clasifica cada comentario como POSITIVO, NEGATIVO o NEUTRO. Después, genera un resumen ejecutivo de los principales temas y problemas detectados. "
        "Comentarios:\n" + "\n".join(comentarios)
    )
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=500
    )
    return response.choices[0].message['content']

if __name__ == "__main__":
    comentarios = df['comentario'].tolist()
    resultado = analizar_comentarios(comentarios)
    print("\n--- ANÁLISIS DE COMENTARIOS ---\n")
    print(resultado)
