
import unittest
from calculate_macros  import CalculateMacros

class test_macronutrients(unittest.TestCase):
    def test_first_number(self):
        macronutrients = CalculateMacros(weight = 70, tall = 175, days = 3, age = 30, gener = "hombre", method = "ganar").execute()
        self.assertEqual(macronutrients.protein, 175 )
        self.assertEqual(macronutrients.fats, 70 )
        self.assertEqual(macronutrients.carbs, 359 )



if __name__ == '__main__':
    unittest.main()