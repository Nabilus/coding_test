import unittest
from main import Units


class TestUnits(unittest.TestCase):
    
    def setUp(self):
        self.units =Units()

    def test_api_status_code(self):
        #check api availability
        status_code = self.units.get_units_from_api().status_code 
        self.assertEqual(status_code, 200, 'API OK')
    
    def test_units_by_age(self):
        #check corresponding age
        self.assertEqual(self.units.get_units_by_age('Feudal')[0]['age'], 'Feudal', 'Age OK')

    def test_get_most_expensive_food(self):
        #Check if unit name had been correctly filled
        self.units.all_units
        self.assertNotEqual(self.units.get_most_expensive_food(self.units.all_units), '', 'Unit Name OK')
    
    def test_get_most_expensive_food_by_age(self):
        #calling the method to check the output in the console
        self.units.get_most_expensive_food_by_age()

    def test_print_villagers_number(self):
        #calling the method to check the output in the console
        self.units.print_villagers_number()









if __name__ == '__main__':
    unittest.main()