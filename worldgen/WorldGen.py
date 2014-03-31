
class WorldGen(object):
    def __init__(self):
        self.players = {}
        self.turn = 0
    
    def update(self):
        self.turn += 1
        for player in self.players:
            player.update()
