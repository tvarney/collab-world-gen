
class City(object):
    Sizes = [0, 1000, 5000, 10000, 25000, 50000, 100000, 250000]
    Wealth = [0, 50, 250, 500, 1250, 2500, 5000, 12500]
    Culture = [0, 1, 5, 10, 25, 50, 100, 250]
    TechResearch = [0, 1, 5, 10, 25, 50, 100, 250]
    MagicResearch = [0, 1, 5, 10, 25, 50, 100, 250]
    MaxSize = 300000
    
    def __init__(self, population, resource_list = None, name = None):
        self.resource_list = resource_list if resource_list != None else []
        self.name = name
        self.population = population
        self.culture = 0
        self.wealth = 0
        self.research = 0
        self.pop_mod = 1.0
        self.wealth_mod = 1.0
        self.culture_mod = 1.0
        self.research_mod = 1.0
        self.combat_mod = 1.0
        
        self.calc_attributes()
    
    def size(self):
        for i in range(len(City.Sizes) - 1, 0, -1):
            if(self.population >= City.Sizes[i]):
                return i
        return 0
    
    def calc_attributes(self):
        size = self.size()
        self.wealth = 50 * City.Attributes[size]
        self.culture = City.Attributes[size]
        self.research = City.Attributes[size]
        for resource in self.resource_list:
            pass
        for building in self.building_list:
            pass
    
    def update_population(self):
        pop = self.population
        if(pop > City.MaxSize):
            pop -= (((pop / City.MaxSize) - 1.0) * pop)
        pop *= (1.25 * self.pop_mod)
        
        self.population = pop
        self.calc_attributes()
    
    def update(self):
        self.update_population()
        wealth = self.wealth * self.wealth_mod
        research = self.research * self.research_mod
        culture = self.culture * self.culture_mod
        return (wealth, research, culture)
    
    def change_population(self, amount):
        self.population += amount
        self.calc_attributes()
