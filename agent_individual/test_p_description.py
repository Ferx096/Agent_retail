from generator_p_description import app
from langchain_core.messages import HumanMessage

initial_state = {
    "query":"",
    "snack_type": "barra",
    "main_ingredients": "organico",
    "nutritional_benefits": "alto en fibra",
    "available_flavors": "menta, fresa, chocolate",
    "target_audience": "niños y jovenes",
    "key_differentiator": "sin conservadores",
    "allergen_certifications": "sin azucar",
    "messages": [],
}

final_result = app.invoke(initial_state)
print(final_result["messages"][-1].content)