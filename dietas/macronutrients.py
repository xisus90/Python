from dataclasses import dataclass

WEIGHT = float(input("Escribe tu peso coporal en kg: "))
TALL = float(input("Escribe tu altura en centimetros: "))
DAYS = int(input("Escribe la cantidad de días que entrenas a la semana:"))
ADGE = int(input("Escribe tu edad: "))
GENER = input("Escribe cual es tu genero (hombre/mujer): ")
METHOD = input("Quieres ganar, perder o mantener el peso (ganar/perder/mantener): ")
@dataclass 
class CalculateMacronutrients():
    protein: int
    carbs: int
    fats: int
    calories_protein: int
    calories_fats: int
    calories_carbs: int
    metabolism_Basal: int


def calcuLate_metabolism_basal():
    
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
        if DAYS > 7:
            print("Una semana no tiene más de 7 días, coloca los días correctamente")


def calculate_macros_gain():
    
    metabolism_Basal = calcuLate_metabolism_basal()
    metabolism_Basal = metabolism_Basal + 500
    protein_kg = 2.5

    return macronutrients(metabolism_Basal, protein_kg)


def calculate_macros_lose():
    
    metabolism_Basal = calcuLate_metabolism_basal()
    metabolism_Basal = metabolism_Basal - 500
    protein_kg = 2

    return macronutrients(metabolism_Basal, protein_kg)


def calculate_macros_keep():
    
    metabolism_Basal = calcuLate_metabolism_basal()
    protein_kg = 2.2

    return macronutrients(metabolism_Basal, protein_kg)


def calculate_protein_to_eat(protein_kg, weight):

    return protein_kg * weight


def calculate_calories_for_carbs(metabolism_Basal, calories_protein, calories_fats):
    sum_prote_fats = calories_protein + calories_fats
    sum_prote_fats = round(sum_prote_fats)
    calories_carbs = metabolism_Basal - sum_prote_fats
    return calories_carbs


def macronutrients(metabolism_Basal, protein_kg):
    
    protein = calculate_protein_to_eat(protein_kg, WEIGHT)
    calories_protein = protein * 4
    calories_protein = round(calories_protein)

    fats = WEIGHT
    calories_fats = fats * 9
    fats = round(fats)
    calories_fats = round(calories_fats)

    calories_carbs = calculate_calories_for_carbs(metabolism_Basal, calories_protein, calories_fats)
    carbs = calories_carbs / 4
    calories_carbs = round(calories_carbs)
    carbs = round(carbs)

    #return round(protein),calories_protein,fats,calories_fats,calories_carbs,carbs, metabolism_Basal
    return CalculateMacronutrients(
        protein=round(protein),
        calories_protein= calories_protein,
        fats = fats,
        calories_fats = calories_fats,
        calories_carbs = calories_carbs,
        carbs = carbs,
        metabolism_Basal = metabolism_Basal
        )


def execute():
    
    if METHOD == "ganar":
        macronutrients = calculate_macros_gain()     
        
    if METHOD == "perder":
        macronutrients = calculate_macros_lose()
       
    if METHOD == "mantener":
        macronutrients = calculate_macros_keep()

    print("las calorías recomendadas son: ", macronutrients.metabolism_Basal)
    print("los gramos de proteinas recomendables son: ",macronutrients.protein,"gr con unas calorias de proteinas de ", macronutrients.calories_protein )
    print("los gramos de grasas saludables recomendables son: ",macronutrients.fats,"gr con unas calorias de grasas de ", macronutrients.calories_fats )
    print("los gramos de carbohidratos recomendables son: ",macronutrients.carbs,"gr con unas calorias de carbohidratos de ", macronutrients.calories_carbs )

execute()