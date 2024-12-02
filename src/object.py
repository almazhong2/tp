from cmu_graphics import *

class Collectible:
    def __init__(self, app, xindex, yindex):
        self.index = xindex
        self.x = snapTerrainX(app, xindex)
        self.y = snapTerrainY(app, yindex)
        self.width = 50
        self.height = 50
        self.color = None
    
    def animate(self):
        #shrink and expand
        pass

    def collision():
        pass

class Coin(Collectible):
    def __init__(self, app, xindex, yindex):
        super().__init__(app, xindex, yindex)
        self.color = 'yellow'

class Powerup(Collectible):
    def __init__(self, app, xindex, yindex):
        super().__init__(app, xindex, yindex)
        self.color = 'blue'

class Powerdown(Collectible):
    def __init__(self, app, xindex, yindex):
        super().__init__(app, xindex, yindex)
        self.color = 'red'


def snapTerrainY(app, i):
    tierHeight = app.height // len(app.world)
    y = app.height - (i + 1)*tierHeight + 50
    return y

def snapTerrainX(app, j):
    tierWidth = app.width // 15 #allow 15 hops width
    x = tierWidth * (j) 
    return x

