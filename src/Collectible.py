from cmu_graphics import *
import util
from player import *


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
        self.collected = False
    
    def animate(self):
        factor = 0.75
        if self.width > 0 and self.shrink:
            self.width -= 1
            self.height -= 1
            self.depth -= .25
            if self.width < self.dimension*factor:
                self.shrink = False
        elif self.width > 0:
            self.width += 1
            self.height += 1
            self.depth += .25
            if self.width >= self.dimension:
                self.shrink = True 
    
    def collect(self, app, obj):
        left, right, top, bottom = util.getBoundaries(util.getVertices(obj.x, obj.y, obj.width, obj.height, obj.depth))
        #CMU Cs academy 4.3.5 point-rectangle intersection
        c1 = left <= self.x <= right 
        c2 = top <= self.y <= bottom
        

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


