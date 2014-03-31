
class BuildingTemplate(object):
    def __init__(self, name, pop, wealth, culture, tech, magic, combat,
                 max_level, max_per_city, research = None):
        self.name = name
        self.pop_mod = pop
        self.wealth_mod = wealth
        self.culture_mod = culture
        
        self.max_level = max_level
        self.max_per_city = max_per_city
        self.research = research if research != None else []

class Building(object):
    def __init__(self, template, level = 1):
        self.template = template
        self.level = level
    
    def cost(self, level = None):
        if(level == None):
            level = self.level
        return 1000 * ((level + 1) ** 2)
    
    def upgrade_cost(self):
        return cost(self.level + 1)
    
