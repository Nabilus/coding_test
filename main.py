import requests
import math

class Units():

    def __init__(self):
        self.url = "https://age-of-empires-2-api.herokuapp.com/api/v1/units"
        self.ages= ['Dark', 'Feudal', 'Castle', 'Imperial']
        self.all_units  = self.get_units_from_api().json()['units']
        


    def get_units_from_api(self):
        """The Method call the api to get Units

            Returns:
            list:Returning value

        """
        return requests.get(self.url)

    def get_units_by_age(self, age):
        #List comprehension to create a list
        return [ unit for unit in self.all_units if unit['age'] == age]
        
    def get_most_expensive_food(self, units):
        expensive = {'name': '', 'cost': 0}
        # cost and food keys not always created, I used TRY/Catch Method to handle the error
        for unit in units:
            try:
                if unit['cost']['Food'] > expensive['cost']:
                    expensive['name'] = unit['name']
                    expensive['cost'] = unit['cost']['Food']
            except:    
                pass
        return expensive

    def get_most_expensive_food_by_age(self):
        #for each age, I'm printing the cost, the name and the corresponding age
        for age in self.ages:
            units_by_age = self.get_units_by_age(age)
            result = self.get_most_expensive_food(units_by_age)
            print(f" For the {age} age, the {result['name']} were the most expensive unit, they were worth {result['cost']} food \n")
    
    def get_build_time(self, expensive_unit):

        build_time = 0
        for unit in self.all_units:
            if unit['name'] == expensive_unit['name']:
                build_time = unit['build_time']
        return build_time


    def print_villagers_number(self):
        expensive_unit = self.get_most_expensive_food(self.all_units)
        #get build time                
        build_time = self.get_build_time(expensive_unit)

        #caclulating max food gathered by a villager during the build time
        food_gathered_by_villager = 0.44 * build_time

        #Calculating the max numbers of villager and rounding up the result

        villagers_number = math.ceil(expensive_unit['cost'] / food_gathered_by_villager)

        print(f" To continuously build {expensive_unit['name']} we'd need {villagers_number} villagers gathering food at the same time. \n")

