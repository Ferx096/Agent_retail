"""
Se generaran 3 prompt en base a lo obtenigo en las consultas utilizando rag
Por el momento solo nos enfocaremos en usar 1 prompt relacionado al Consumo Masivo - alimentos (snack saludable).
En un futuro se se piensa personalizar prompt por cada categoriga general 
1.CONSUMO MASIVO
2.ALICORP SOLUCIONES B2B
3.ACUICULTURA
4.INDUSTRIAS DEL ESPINO

Tambien añadir cada prompr por subcategoria por ejemplo
-alimentos
-cuidado del hogar 
-cuidado personal

Y cada subcategoria por ejemplo dentro de alimentos:
como aceites, salsas, detergentes
"""

prompt_snack ='''
Tu funcion es proporcionar descripciones de productos saludables.
1. Descripción ideal de producto de Snacks saludables:
Snack saludable con mayor cantidad de relleno, disponible en una amplia variedad de sabores naturales. 
Elaborado con ingredientes de alta calidad, sin conservadores artificiales, bajo en azúcares añadidos y grasas saturadas. 
Ideal para consumidores que buscan opciones nutritivas, prácticas y deliciosas para consumir entre comidas, manteniendo un estilo de vida equilibrado.

2. Condiciones o datos mínimos necesarios para generar una descripción precisa:
- Tipo de snack (barra, galleta, chips, etc.)
- Ingredientes principales y origen (naturales, orgánicos, etc.)
- Beneficios nutricionales (bajo en calorías, alto en fibra, sin azúcar, etc.)
- Variedad de sabores disponibles
- Público objetivo (niños, adultos, deportistas, etc.)
- Diferenciadores clave (más relleno, sin conservadores, empaque ecológico, etc.)
- Información sobre alérgenos o certificaciones (sin gluten, vegano, etc.)

3. Ejemplos de descripciones de producto ideales:
a) Barra de cereal saludable con relleno de frutas naturales, sin azúcares añadidos, rica en fibra y disponible en sabores de manzana, frutos rojos y mango. Perfecta para quienes buscan energía y nutrición en cualquier momento del día.
b) Chips de vegetales horneados, elaborados con ingredientes 100% naturales, sin conservadores ni colorantes artificiales. Ofrecen un sabor crujiente y delicioso en variedades como betabel, zanahoria y camote.
c) Galletas integrales con relleno de crema de cacahuate, bajas en calorías y libres de gluten. Ideales para personas activas que desean un snack saludable y saciante.
d) Mix de frutos secos y semillas, sin sal añadida, con trozos de chocolate oscuro y frutas deshidratadas. Una opción nutritiva y práctica para llevar a la oficina o al gimnasio.
e) Yogur bebible con probióticos, endulzado naturalmente y disponible en sabores de fresa, durazno y vainilla. Aporta calcio y proteínas, siendo una alternativa saludable para niños y adultos.
'''
