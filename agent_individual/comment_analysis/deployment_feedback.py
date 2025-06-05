import streamlit as st
import requests
import pandas as pd
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')
logger = logging.getLogger(__name__)

st.title("Análisis de Comentarios de Usuarios - Feedback")
st.write("Carga comentarios manualmente o desde un archivo CSV. El análisis se realiza usando el microservicio FastAPI.")

comentarios = []
opcion = st.radio("¿Cómo quieres ingresar los comentarios?", ["Manual", "Archivo CSV"])
if opcion == "Manual":
    texto = st.text_area("Escribe un comentario por línea:")
    if texto:
        comentarios = [line.strip() for line in texto.split("\n") if line.strip()]
else:
    archivo = st.file_uploader("Sube un archivo CSV con una columna 'comentario':", type="csv")
    if archivo:
        df = pd.read_csv(archivo)
        if "comentario" in df.columns:
            comentarios = df["comentario"].dropna().tolist()
        else:
            st.error("El archivo debe tener una columna llamada 'comentario'.")

if comentarios:
    st.write(f"Total de comentarios a analizar: {len(comentarios)}")
    if st.button("Analizar comentarios"):
        with st.spinner("Analizando..."):
            url = "http://localhost:8000/analizar"
            try:
                logger.info(f"Enviando {len(comentarios)} comentarios al microservicio...")
                resp = requests.post(url, json={"comentarios": comentarios}, timeout=120)
                if resp.status_code == 200:
                    data = resp.json()
                    st.subheader("Clasificación de comentarios")
                    df_result = pd.DataFrame(data["clasificados"])
                    st.dataframe(df_result)
                    st.subheader("Resumen ejecutivo")
                    st.write(data["resumen"])
                    logger.info("Resultados mostrados correctamente en Streamlit.")
                else:
                    st.error(f"Error del microservicio: {resp.text}")
                    logger.error(f"Error del microservicio: {resp.text}")
            except Exception as e:
                st.error(f"Error de conexión: {e}")
                logger.error(f"Error de conexión: {e}")
else:
    st.info("Agrega comentarios para analizar.")

st.markdown("---")
st.markdown("**Desarrollado para análisis masivo y en vivo con OpenAI GPT-4o y FastAPI.**")
