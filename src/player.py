from cmu_graphics import *
import util

app.playerColor = 'violet'
app.depth = 25

def drawPlayer(app):
    util.drawBlock(app.playerX, app.playerY, 75, 50, app.depth, app.playerColor)