from cmu_graphics import *
import util
import random

#app.world = [None, 'road', 'road', None, None, 'road', None, None, None, None, 'road']
app.roadLeft = app.width//4
app.roadTop = app.height*7/8
app.roadWidth = 2*app.width
app.roadHeight = 1
app.roadDepth = 100
app.cars = []

def drawTerrain(app):
    util.drawBlock(0, app.height, 2*app.width, 1, app.height*2, 'green')

def drawRoad(app, i):
    y = app.height - (i + 1) * (app.height // len(app.world))
    util.drawBlock(app.width//4, y, 2*app.width, 1, 75, 'gray')
    drawDashes(app, i)

def drawCar(app, i):
    colors = ['oliveDrab', 'cornflowerBlue', 'darkMagenta', 'deepPink']
    width = random.randint(25, 75)
    height = random.randint(25, 75)
    depth = 25
    y = app.height - (i + 1) * (app.height // len(app.world))
    util.drawBorderBlock(50, y, width, height, depth, random.choice(colors))    


def drawDashes(app, i):
    yRoad = app.height - (i + 1) * (app.height // len(app.world))
    roadWidth = app.height // len(app.world)

    dashWidth = 50
    dashGap = 30
    dashDepth = 10
    dashes = (app.width + dashGap) // (dashWidth + dashGap) + 1
    xStart = 0
    yStart = yRoad - roadWidth//2 + dashWidth//2 - dashWidth // 5

    for j in range(dashes):
        x = xStart + j * (dashWidth + dashGap)
        util.drawBorderBlock(x, yStart, dashWidth, 5, dashDepth, 'white')        

def drawGrass(app, i):
    y = app.height - (i + 1) * (app.height // len(app.world))
    util.drawBlock(app.width//4, y, 2*app.width, 1, 75, 'lightGreen')

def drawLake(app, i):
    y = app.height - (i + 1) * (app.height // len(app.world))
    util.drawBlock(app.width//4, y, 1.5*app.width, 1, 75, gradient('lightCyan', 'lightSkyBlue', 'skyBlue', 'deepSkyBlue', start = 'center'))



def drawWorld(app):
    for i in range (len(app.world)):
        terrain = app.world[i]
        if terrain == 'road':
            drawRoad(app, i)
            drawDashes(app, i)
        elif terrain == 'grass':
            drawGrass(app, i)
        elif terrain == 'lake':
            drawLake(app, i)