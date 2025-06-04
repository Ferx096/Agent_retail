import pdfplumber

pdf_path = "tu_archivo.pdf"
start_page = 21  # Página 22 (índice base 0)
end_page = 28    # Página 29 (índice base 0)

# Textos delimitadores
start_text = "A. NEGOCIO DE CONSUMO MASIVO"
end_text = "Además, logra excelentes resultados de indicadores digitales, como un sentiment positivo del 89% y un VTR (view through rate) del 45% en Youtube."

# 1. Extraer texto de las páginas relevantes
with pdfplumber.open(pdf_path) as pdf:
    fragmento = ""
    for i in range(start_page, end_page + 1):
        page = pdf.pages[i]
        page_text = page.extract_text()
        if page_text:
            fragmento += page_text + "\n"

# 2. Buscar los textos delimitadores
start_idx = fragmento.find(start_text)
end_idx = fragmento.find(end_text)

if start_idx == -1 or end_idx == -1:
    raise ValueError("No se encontraron los textos delimitadores en el PDF extraído.")

# 3. Extraer el fragmento entre los delimitadores (incluyendo el texto final)
end_idx += len(end_text)
fragmento_deseado = fragmento[start_idx:end_idx]

# Ahora puedes usar fragmento_deseado para generar embeddings
print(fragmento_deseado)
