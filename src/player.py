from cmu_graphics import *
import util
import world

app.playerColor = 'violet'
app.depth = 25
app.world = ['grass', 'road', 'road', 'grass', 'grass', 'road', 'grass', 'grass', 'road', 'grass', 'road']

def drawPlayer(app):
    util.drawBorderBlock(app.playerX, app.playerY, 75, 50, app.depth, app.playerColor)

#will snap the player to be aligned with the terrain
def snapTerrain(app, i):
    tierHeight = app.height // len(app.world)
    y = app.height - (i + 1)*tierHeight
    return y


