from dataclasses import dataclass
@dataclass 
class CalculateMacronutrients():
    protein: int
    carbs: int
    fats: int
    calories_protein: int
    calories_fats: int
    calories_carbs: int
    metabolism_Basal: int


class CalculateMacros:
    def __init__(self, weight, tall, days, age, gener, method):
        self._weith = weight
        self._tall = tall
        self._days = days
        self._age = age
        self._gener = gener
        self._method = method

    basal_days = [1.2, 1.375, 1.375, 1.375, 1.55, 1.55, 1.725, 1.9]


    def calculate_basal_gener(self):
        
        if self._gener == "hombre":
            basal = (10 * self._weith) + (6.25 * self._tall) - (5 * self._age) + 5
            return basal
        
        if self._gener == "mujer":
            basal = (10 * self._weith) + (6.25 * self._tall) - (5 * self._age) - 161
            return basal


    def calcuLate_metabolism_basal(self):
        
        basal_gener = self.calculate_basal_gener()

        if 0 <= self._days <= 7:
            basal_gener = basal_gener * self.basal_days[self._days]
            basal_gener = round(basal_gener)
            return basal_gener
        if self._days > 7:
            print("Una semana no tiene más de 7 días, coloca los días correctamente")
            exit()


    def calculate_macros_gain(self):
        
        metabolism_Basal = self.calcuLate_metabolism_basal()
        metabolism_Basal = metabolism_Basal + 500
        protein_kg = 2.5

        return self.macronutrients(metabolism_Basal, protein_kg)


    def calculate_macros_lose(self):
        
        metabolism_Basal = self.calcuLate_metabolism_basal()
        metabolism_Basal = metabolism_Basal - 500
        protein_kg = 2

        return self.macronutrients(metabolism_Basal, protein_kg)


    def calculate_macros_keep(self):
        
        metabolism_Basal = self.calcuLate_metabolism_basal()
        protein_kg = 2.2

        return self.macronutrients(metabolism_Basal, protein_kg)


    def calculate_protein_to_eat(self, protein_kg, weight):

        return protein_kg * weight


    def calculate_calories_for_carbs(self, metabolism_Basal, calories_protein, calories_fats):
        sum_prote_fats = calories_protein + calories_fats
        sum_prote_fats = round(sum_prote_fats)
        calories_carbs = metabolism_Basal - sum_prote_fats
        return calories_carbs


    def macronutrients(self, metabolism_Basal, protein_kg):
        
        protein = self.calculate_protein_to_eat(protein_kg, self._weith)
        calories_protein = protein * 4
        calories_protein = round(calories_protein)

        fats = self._weith
        calories_fats = fats * 9
        fats = round(fats)
        calories_fats = round(calories_fats)

        calories_carbs = self.calculate_calories_for_carbs(metabolism_Basal, calories_protein, calories_fats)
        carbs = calories_carbs / 4
        calories_carbs = round(calories_carbs)
        carbs = round(carbs)

        return CalculateMacronutrients(
            protein=round(protein),
            calories_protein= calories_protein,
            fats = fats,
            calories_fats = calories_fats,
            calories_carbs = calories_carbs,
            carbs = carbs,
            metabolism_Basal = metabolism_Basal
            )


    def execute(self):
        
        if self._method == "ganar":
            macronutrients = self.calculate_macros_gain()     
            
        if self._method == "perder":
            macronutrients = self.calculate_macros_lose()
        
        if self._method == "mantener":
            macronutrients = self.calculate_macros_keep()

        return macronutrients