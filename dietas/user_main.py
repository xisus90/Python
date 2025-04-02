from calculate_macros import CalculateMacros

try:
    WEIGHT = int(input("Escribe tu peso en kg: "))
except ValueError:
    print("El campo del peso no está definido o es inválido.")
    exit()

try:
    TALL = int(input("Escribe tu altura en centímetros: "))
except ValueError:
    print("El campo de la altura no está definido o es inválido.")
    exit()

try:
    DAYS = int(input("Escribe la cantidad de días que entrenas a la semana (0 a 7 días): "))
except ValueError:
    print("El campo de día no está definido o es inválido.")
    exit()

try:
    AGE = int(input("Escribe tu edad: "))
except ValueError:
    print("El campo de edad no está definido o es inválido.")
    exit()

try:
    GENER = input("Escribe cuál es tu género (hombre/mujer): ").lower()
    if GENER not in ["hombre", "mujer"]:
        print("El género no está definido correctamente.")
        exit()
except ValueError:
    print("No se asignó nada en la sección de género.")
    exit()

try:
    METHOD = input("¿Quieres ganar, perder, mantener o recomponer? (ganar/perder/mantener/recomponer): ").lower()
    if METHOD not in ["ganar", "perder", "mantener", "recomponer"]:
        print("El método no está definido correctamente.")
        exit()
except ValueError:
    print("No se asignó nada en el campo de método.")
    exit()

macronutrients = CalculateMacros(WEIGHT, TALL, DAYS, AGE, GENER, METHOD).execute()

<<<<<<< HEAD
print("\n--- RESULTADO PERSONALIZADO DE MACRONUTRIENTES ---\n")
print(f"✅ Calorías recomendadas totales: {macronutrients.metabolism_Basal} kcal")
print(f"🍗 Proteínas: {macronutrients.protein} g ({macronutrients.calories_protein} kcal)")
print(f"🥑 Grasas: {macronutrients.fats} g ({macronutrients.calories_fats} kcal)")
print(f"🍚 Carbohidratos: {macronutrients.carbs} g ({macronutrients.calories_carbs} kcal)")
=======
print("las calorías recomendadas son: ", macronutrients.metabolism_Basal)
print("los gramos de proteinas recomendables son: ",macronutrients.protein,"gr con unas calorias de proteinas de ", macronutrients.calories_protein )
print("los gramos de grasas saludables recomendables son: ",macronutrients.fats,"gr con unas calorias de grasas de ", macronutrients.calories_fats )
print("los gramos de carbohidratos recomendables son: ",macronutrients.carbs,"gr con unas calorias de carbohidratos de ", macronutrients.calories_carbs )


 
>>>>>>> ff26df478692ad1ddebf83324135e22ff88d4f70
