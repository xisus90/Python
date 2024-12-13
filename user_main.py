from calculate_macros import CalculateMacros


try:
    WEIGHT = int(input("Escribe tu peso en kg: "))
except ValueError:
    print("El campo del peso no está definido o es inválido.")
    exit()

try:
    TALL = int(input("Escribe tu altura en centimetros: "))
except ValueError:
    print("El campo de la altura no está definido o es inválido.")
    exit()

try:
    DAYS = int(input("Escribe la cantidad de días que entrenas a la semana (0 a 7 días):"))
except ValueError:
        print ("el campo de día no está definido o es inválido")
        exit()

try:
    AGE = int(input("Escribe tu edad: "))
except ValueError:
    print ("el campo de años no está definido o es inválido")
    exit()


try:
    GENER = input("Escribe cual es tu genero (hombre/mujer): ")
    if GENER != "hombre" and GENER != "mujer":
        print("El genero no está definido correctamente")
        exit()
except ValueError:
    print ("no se asignadó nada en la sección de genero")
    exit()

try:
    METHOD = input("Quieres ganar, perder o mantener el peso (ganar/perder/mantener): ")
    if METHOD != "ganar" and METHOD != "perder" and METHOD != "mantener":
        print("El genero no está definido correctamente")
        exit()
except ValueError:
    print ("No se asignó nada en el campo de método")
    exit()


macronutrients = CalculateMacros(WEIGHT, TALL, DAYS, AGE, GENER, METHOD).execute()

print("las calorías recomendadas son: ", macronutrients.metabolism_Basal)
print("los gramos de proteinas recomendables son: ",macronutrients.protein,"gr con unas calorias de proteinas de ", macronutrients.calories_protein )
print("los gramos de grasas saludables recomendables son: ",macronutrients.fats,"gr con unas calorias de grasas de ", macronutrients.calories_fats )
print("los gramos de carbohidratos recomendables son: ",macronutrients.carbs,"gr con unas calorias de carbohidratos de ", macronutrients.calories_carbs )

#buscar algo acerca de excepcions en python 
#principios solid estudiarlos por encima
#open close--> abierto al cambio 