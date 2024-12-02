from cmu_graphics import *
import util
import world

app.playerColor = 'violet'
app.depth = 25
app.world = ['grass', 'road', 'road', 'grass', 'grass', 'road', 'grass', 'grass', 'road', 'grass', 'road']

"""
def drawPlayer(app):
    util.drawBorderBlock(app.playerX, app.playerY, 75, 50, app.depth, app.playerColor)
"""

#will snap the player to be aligned with the terrain
def snapTerrainY(app, i):
    tierHeight = app.height // len(app.world)
    y = app.height - (i + 1)*tierHeight
    return y

def snapTerrainX(app, j):
    tierWidth = app.width // 15 #allow 15 hops width
    x = tierWidth * (j) 
    return x

class Player:

    def __init__(self, x, y, hopHeight, frames):
        self.x = x
        self.y = y

        #hopping coordinates start off stationary
        self.x1 = x
        self.y1 = y

        self.x2 = x
        self.y2 = y

        self.hopHeight = hopHeight
        self.currentFrame = 0
        self.totalFrames = frames
        self.isHopping = False
        
    
    def hop(self):
        if self.isHopping == False:
            
            """
            self.x1 = self.x
            self.y1 = self.y

            self.x2 = x2
            self.y2 = y2
            """

            self.currentFrame = 0
            self.isHopping = True

    def updateHop(self):
        if self.isHopping:
            time = self.currentFrame / self.totalFrames
            self.y = self.y = (1-time)*self.y1 + time*self.y2
            self.y += 4*self.hopHeight*(time - 0.5)**2

            """
            #chatGPT: formulas for frame by frame hopping (in a parabolic motion)
            self.x = (1-time)*self.x1 + time*self.x2 
            self.y = (1-time)*self.y1 + time*self.y2
            self.y -= 4*self.hopHeight*(time - 0.5)**2
            """
            self.currentFrame +=1

            if self.currentFrame >= self.totalFrames:
                self.y = self.y
                self.isHopping = False
    
    def snapTerrain(self, app, i, j):
        x = snapTerrainX(app, j)
        y = snapTerrainY(app, i)
        return x, y

    
    def drawPlayer(self, app):
        util.drawBorderBlock(self.x, self.y, 75, 50, app.depth, app.playerColor)

    #app.hopX1, app.hopY1, app.hopX2, app.hopY2 = player.getHoppingVariables(app.playerX, app.playerY)

