from cmu_graphics import *
import util

app.world = [None, 'road', 'road', None, None, 'road', None, None, None, None]
app.roadLeft = app.width//4
app.roadTop = app.height*7/8
app.roadWidth = 2*app.width
app.roadHeight = 1
app.roadDepth = 100

def drawTerrain(app):
    util.drawBlock(0, app.height, 2*app.width, 1, app.height*2, 'green')

def drawRoad(app):
    util.drawBlock(app.width//4, app.height*7/8, 2*app.width, 1, 75, 'gray')
    drawDashes(app)

def drawDashes(app):
    pass

def drawBlock(x, y, width, height, depth, color):
    pass