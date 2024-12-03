from cmu_graphics import *
import util

class Collectible:
    def __init__(self, app, xindex, yindex):
        self.index = xindex
        self.x = snapTerrainX(app, xindex)
        self.y = snapTerrainY(app, yindex)
        self.dimension = 40
        self.baseDepth = 10
        self.width = self.dimension
        self.height = self.dimension
        self.depth = self.baseDepth
        self.color = None
        self.shrink = True #starts with shrinking
    
    def animate(self):
        factor = 0.75

        if self.shrink:
            self.width -= 1
            self.height -= 1
            self.depth -= .25
            if self.width < self.dimension*factor:
                self.shrink = False
        else:
            self.width += 1
            self.height += 1
            self.depth += .25
            if self.width >= self.dimension:
                self.shrink = True 




#for player
"""
def snapTerrainY(app, i):
    tierHeight = app.height // len(app.world)
    y = app.height - (i + 1)*tierHeight + 60
    return y

def snapTerrainX(app, j):
    tierWidth = app.width // 15 #allow 15 hops width
    x = tierWidth * (j) 
    return x
"""
#for collectible

def snapTerrainY(app, i):
    tierHeight = app.height // len(app.world)
    y = app.height - (i + 1)*tierHeight + 50
    return y

def snapTerrainX(app, j):
    tierWidth = app.width // 15 #allow 15 hops width
    x = tierWidth * (j) 
    return x
    
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




