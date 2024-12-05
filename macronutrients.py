
WEIGHT = float(input("Escribe tu peso coporal en kg: "))
TALL = float(input("Escribe tu altura en centimetros: "))
DAYS = int(input("Escribe la cantidad de días que entrenas a la semana:"))
ADGE = int(input("Escribe tu edad: "))
GENER = input("Escribe cual es tu genero (hombre/mujer): ")
METHOD = input("Quieres ganar, perder o mantener el peso (ganar/perder/mantener): ")


def calcuLate_metabolism_basal(WEIGHT, TALL, DAYS, ADGE ,GENER):
    
    if GENER == "hombre":
        Man_Basal = (10 * WEIGHT) + (6.25 * TALL) - (5 * ADGE) + 5
        if DAYS == 0:
            Man_Basal = Man_Basal * 1.2
            Man_Basal = round(Man_Basal)
            return Man_Basal
        if 1 <= DAYS <= 3:
            Man_Basal = Man_Basal * 1.375
            Man_Basal = round(Man_Basal)
            return Man_Basal
        if 4 <= DAYS <=5:
            Man_Basal = Man_Basal * 1.55
            Man_Basal = round(Man_Basal)
            return Man_Basal
        if DAYS == 6:
            Man_Basal = Man_Basal * 1.725
            Man_Basal = round(Man_Basal)
            return Man_Basal
        if DAYS == 7:
            Man_Basal = Man_Basal * 1.9
            Man_Basal = round(Man_Basal)
            return Man_Basal
        if DAYS > 7:
            print("Una semana no tiene más de 7 días, coloca los días correctamente")

    if GENER == "mujer":
        Woman_Basal = (10 * WEIGHT) + (6.25 * TALL) - (5 * ADGE) - 161
        if DAYS == 0:
            Woman_Basal = Woman_Basal * 1.2
            Woman_Basal = round(Woman_Basal)
            return Woman_Basal
        if 1 <= DAYS <= 3:
            Woman_Basal = Woman_Basal * 1.375
            Woman_Basal = round(Woman_Basal)
            return Woman_Basal
        if 4 <= DAYS <=5:
            Woman_Basal = Woman_Basal * 1.55
            Woman_Basal = round(Woman_Basal)
            return Woman_Basal
        if DAYS == 6:
            Woman_Basal = Woman_Basal * 1.725
            Woman_Basal = round(Woman_Basal)
            return Woman_Basal
        if DAYS == 7:
            Woman_Basal = Woman_Basal * 1.9
            Woman_Basal = round(Woman_Basal)
            return Woman_Basal


def calculate_macros_gain(metabolism_Basal, WEIGHT, METHOD):
    
    protein= 2.5 * WEIGHT
    calories_protein = protein * 4
    protein = round(protein)
    calories_protein = round(calories_protein)
    print ("las proteinas a consumir son:", protein, "y las calorias son: ", calories_protein)

    fats = 1 * WEIGHT
    calories_fats = fats * 9
    fats = round(fats)
    calories_fats = round(calories_fats)
    print("las grasas a consumir son:", fats,"gr y las calorias son: ", calories_fats)

    sum_prote_fats = calories_protein + calories_fats
    calories_carbs = metabolism_Basal - sum_prote_fats
    carbs = calories_carbs / 4
    print("los carbo hidratos a consumir son:", carbs,"gr con unas calorias de :",calories_carbs)

    return protein, carbs, fats, calories_prote, calories_fats, calories_carbs


def calculate_macros_lose(metabolism_Basal, WEIGHT, METHOD):
    
    protein= 2 * WEIGHT
    calories_protein = protein * 4
    protein = round(protein)
    calories_protein = round(calories_protein)
    print ("las proteinas a consumir son:", protein, "y las calorias son: ", calories_protein)

    fats = 1 * WEIGHT
    calories_fats = fats * 9
    fats = round(fats)
    calories_fats = round(calories_fats)
    print("las grasas a consumir son:", fats,"gr y las calorias son: ", calories_fats)

    sum_prote_fats = calories_protein + calories_fats
    calories_carbs = metabolism_Basal - sum_prote_fats
    carbs = calories_carbs / 4
    print("los carbo hidratos a consumir son:", carbs,"gr con unas calorias de :",calories_carbs)

    return protein, carbs, fats, calories_prote, calories_fats, calories_carbs


def calculate_macros_keep(metabolism_Basal, WEIGHT, METHOD):
       
    protein= 2.2 * WEIGHT
    calories_protein = protein * 4
    protein = round(protein)
    calories_protein = round(calories_protein)
    print ("las proteinas a consumir son:", protein, "y las calorias son: ", calories_protein)

    fats = 1 * WEIGHT
    calories_fats = fats * 9
    fats = round(fats)
    calories_fats = round(calories_fats)
    print("las grasas a consumir son:", fats,"gr y las calorias son: ", calories_fats)

    sum_prote_fats = calories_protein + calories_fats
    calories_carbs = metabolism_Basal - sum_prote_fats
    carbs = calories_carbs / 4
    print("los carbo hidratos a consumir son:", carbs,"gr con unas calorias de :",calories_carbs)

    return protein, carbs, fats, calories_prote, calories_fats, calories_carbs



if WEIGHT and TALL and DAYS >= 0 and ADGE and GENER.isalpha() and METHOD.isalpha() :
    metabolism_Basal = calcuLate_metabolism_basal(WEIGHT, TALL, DAYS, ADGE ,GENER)
    if METHOD == "ganar":
        metabolism_Basal = metabolism_Basal + 500
        protein, carbs, fats, calories_prote, calories_fats, calories_carbs = calculate_macros_gain(metabolism_Basal, WEIGHT, METHOD)
        print("las calorías recomendadas son: ", metabolism_Basal)
        print("los gramos de proteinas recomendables son: ",protein,"gr con unas calorias de proteinas de ", calories_prote )
        print("los gramos de grasas saludables recomendables son: ",fats,"gr con unas calorias de grasas de ", calories_fats )
        print("los gramos de carbohidratos recomendables son: ",carbs,"gr con unas calorias de carbohidratos de ", calories_carbs )
    if METHOD == "perder":
        metabolism_Basal = metabolism_Basal - 500
        protein, carbs, fats, calories_prote, calories_fats, calories_carbs = calculate_macros_lose(metabolism_Basal, WEIGHT, METHOD)
        print("las calorías recomendadas son: ", metabolism_Basal)
        print("los gramos de proteinas recomendables son: ",protein,"gr con unas calorias de proteinas de ", calories_prote )
        print("los gramos de grasas saludables recomendables son: ",fats,"gr con unas calorias de grasas de ", calories_fats )
        print("los gramos de carbohidratos recomendables son: ",carbs,"gr con unas calorias de carbohidratos de ", calories_carbs )
    protein, carbs, fats, calories_prote, calories_fats, calories_carbs = calculate_macros_keep(metabolism_Basal, WEIGHT, METHOD)
    print("las calorías recomendadas son: ", metabolism_Basal)
    print("los gramos de proteinas recomendables son: ",protein,"gr con unas calorias de proteinas de ", calories_prote )
    print("los gramos de grasas saludables recomendables son: ",fats,"gr con unas calorias de grasas de ", calories_fats )
    print("los gramos de carbohidratos recomendables son: ",carbs,"gr con unas calorias de carbohidratos de ", calories_carbs )
else:
    print("Debes rellenar todos los campos correctamente")