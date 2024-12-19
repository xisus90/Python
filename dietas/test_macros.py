
import unittest
from calculate_macros  import CalculateMacros

class test_macronutrients(unittest.TestCase):
    def test_zero_number(self):
        macronutrients = CalculateMacros(weight = 70, tall = 175, days = 0, age = 30, gener = "hombre", method = "ganar").execute()
        self.assertEqual(macronutrients.metabolism_Basal, 2478)
        self.assertEqual(macronutrients.protein, 175 )
        self.assertEqual(macronutrients.fats, 70 )
        self.assertEqual(macronutrients.carbs, 287 )

    def test_first_number(self):
        macronutrients = CalculateMacros(weight = 70, tall = 175, days = 1, age = 30, gener = "hombre", method = "ganar").execute()
        self.assertEqual(macronutrients.metabolism_Basal, 2767)
        self.assertEqual(macronutrients.protein, 175 )
        self.assertEqual(macronutrients.fats, 70 )
        self.assertEqual(macronutrients.carbs, 359 )


    def test_second_number(self):
        macronutrients = CalculateMacros(weight = 70, tall = 175, days = 2, age = 30, gener = "hombre", method = "ganar").execute()
        self.assertEqual(macronutrients.metabolism_Basal, 2767)
        self.assertEqual(macronutrients.protein, 175 )
        self.assertEqual(macronutrients.fats, 70 )
        self.assertEqual(macronutrients.carbs, 359 )

    def test_third_number(self):
        macronutrients = CalculateMacros(weight = 70, tall = 175, days = 3, age = 30, gener = "hombre", method = "ganar").execute()
        self.assertEqual(macronutrients.metabolism_Basal, 2767) 
        self.assertEqual(macronutrients.protein, 175 )
        self.assertEqual(macronutrients.fats, 70 )
        self.assertEqual(macronutrients.carbs, 359 )
    
    def test_fourth_number(self):
        macronutrients = CalculateMacros(weight = 70, tall = 175, days = 4, age = 30, gener = "hombre", method = "ganar").execute()
        self.assertEqual(macronutrients.metabolism_Basal, 3056)        
        self.assertEqual(macronutrients.protein, 175 )
        self.assertEqual(macronutrients.fats, 70 )
        self.assertEqual(macronutrients.carbs, 432 )

    def test_fifth_number(self):
        macronutrients = CalculateMacros(weight = 70, tall = 175, days = 5, age = 30, gener = "hombre", method = "ganar").execute()
        self.assertEqual(macronutrients.metabolism_Basal, 3056)        
        self.assertEqual(macronutrients.protein, 175 )
        self.assertEqual(macronutrients.fats, 70 )
        self.assertEqual(macronutrients.carbs, 432 )

    def test_sixth_number(self):
        macronutrients = CalculateMacros(weight = 70, tall = 175, days = 6, age = 30, gener = "hombre", method = "ganar").execute()
        self.assertEqual(macronutrients.metabolism_Basal, 3344)        
        self.assertEqual(macronutrients.protein, 175 )
        self.assertEqual(macronutrients.fats, 70 )
        self.assertEqual(macronutrients.carbs, 504 )
        
    def test_seventh_number(self):
        macronutrients = CalculateMacros(weight = 70, tall = 175, days = 7, age = 30, gener = "hombre", method = "ganar").execute()
        self.assertEqual(macronutrients.metabolism_Basal, 3633)        
        self.assertEqual(macronutrients.protein, 175 )
        self.assertEqual(macronutrients.fats, 70 )
        self.assertEqual(macronutrients.carbs, 576 )

if __name__ == '__main__':
    unittest.main()