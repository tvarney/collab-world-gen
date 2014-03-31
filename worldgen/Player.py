
class Player(object):
    def __init__(self, name, race):
        self.name = name
        self.race = race
        self.tech = []
        self.cities = []
        self.army = 0
        self.population = 0
        self.wealth = 0
        self.culture = 0
        self.research = 0
        self.mage_research = 0
        
        self.draft_limit_add = 0.0
        self.magic_research_add = 0.0
        self.tech_research_add = 0.0
    
    def set_race(self, race):
        self.draft_limit = race.draft_limit
        self.magic_research_mod = race.magic_research_mod
        self.tech_research_mod = race.tech_research_mod
        self.wealth_mod = race.wealth_mod
    
    def give_tech(self, tech):
        if(not (tech in self.tech)):
            tech.append(tech)
    
    def update(self):
        self.population = 0
        for city in self.cities:
            (dWealth, dResearch, dCulture) = city.update()
            self.wealth += dWealth * self.wealth_mod
            self.research += dResearch * self.tech_research_mod
            self.culture += dCulture
            # Count this cities population
            self.population += city.population
    
    def draft(self, city_no, amount):
        if(city_no >= len(self.cities) or self.cities[city_no] == None):
            return
        
        if(amount > 0.01 * self.population):
            amount = 0.01 * self.population
        if(amount > self.cities[city_no].population):
            amount = self.cities[city_no].population
            self.cities[city_no] = None
        else:
            self.cities[city_no] -= amount
