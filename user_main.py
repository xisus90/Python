from calculate_macros import CalculateMacros


WEIGHT = float(input("Escribe tu peso coporal en kg: "))
TALL = float(input("Escribe tu altura en centimetros: "))
DAYS = int(input("Escribe la cantidad de días que entrenas a la semana:"))
AGE = int(input("Escribe tu edad: "))
GENER = input("Escribe cual es tu genero (hombre/mujer): ")
METHOD = input("Quieres ganar, perder o mantener el peso (ganar/perder/mantener): ")


macronutrients = CalculateMacros(WEIGHT, TALL, DAYS, AGE, GENER, METHOD).execute()

print("las calorías recomendadas son: ", macronutrients.metabolism_Basal)
print("los gramos de proteinas recomendables son: ",macronutrients.protein,"gr con unas calorias de proteinas de ", macronutrients.calories_protein )
print("los gramos de grasas saludables recomendables son: ",macronutrients.fats,"gr con unas calorias de grasas de ", macronutrients.calories_fats )
print("los gramos de carbohidratos recomendables son: ",macronutrients.carbs,"gr con unas calorias de carbohidratos de ", macronutrients.calories_carbs )

#poner un if a cada valor del input para evitar errores
#buscar algo acerca de excepcions en python 
#principios solid estudiarlos por encima
#open close--> abierto al cambio 