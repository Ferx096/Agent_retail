import logging
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__) + '/../'))
from generate_image import generate_image

prompt = "Un empaque de snacks saludables, diseño moderno y minimalista, colores verde y blanco, fondo blanco con luz natural, frutas frescas, estilo fotográfico profesional"
generate_image(prompt)
