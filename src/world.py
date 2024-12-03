from cmu_graphics import *
import util
import random as py_random #debugging strategy from chatGPT
from Car import *
from Collectible import *


#app.world = [None, 'road', 'road', None, None, 'road', None, None, None, None, 'road']
app.roadLeft = app.width//4
app.roadTop = app.height*7/8
app.roadWidth = 2*app.width
app.roadHeight = 1
app.roadDepth = 100

def drawTerrain(app):
    util.drawBlock(0, app.height, 2*app.width, 1, app.height*2, 'green')

def drawRoad(app, i):
    y = app.height - (i + 1) * (app.height // len(app.world))
    util.drawBlock(app.width//4, y, 2*app.width, 1, 75, 'gray')
    drawDashes(app, i)
    drawCars(app, app.cars[i], i)     


def drawCars(app, cars, i):
    #xOffset = py_random.randint(10, 25)
    for index in range(len(cars)):
        car = cars[index]
        carDepth = 25
        #startX = xOffset*index
        #car.x -= startX
        car.y = app.height - (i + 1) * (app.height // len(app.world)) - 40
        util.drawBorderBlock(car.x, car.y, car.width, car.height, carDepth, car.color)

def updateCars(app):
    for cars in app.cars:
        for car in cars:
            car.move() 
            #CMU CS Academy 6.3.2 Wraparound Motion
            if car.direction == 'right':
                if car.x > app.width + car.width:
                    car.x = -car.width
            else:
                if car.x + car.width <= 0:
                    car.x = app.width + car.width 

#depending on cars and road terrain, create these random cars and add to app.cars

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
    
    if i < len(app.greenery):
        plantList = app.greenery[i]
        drawGreenery(app, plantList, i)

def drawGreenery(app, plantList, tier):
    for xindex in range(len(plantList)):
        plant = plantList[xindex]
        x = snapTerrain(app, xindex)
        y = app.height - (tier + 1) * (app.height // len(app.world)) - 40
        if plant == 'tree':
            drawTree(x, y)
        elif plant == 'bush':
            drawBush(x, y)
    

def drawTree(x, y):
    util.drawBorderBlock(x, y, 50, 60, 25, 'forestGreen')

def drawBush(x, y):
    util.drawBorderBlock(x, y, 50, 40, 25, 'yellowGreen')


#for bushes
def snapTerrain(app, j):
    tierWidth = app.width // 15 #allow 15 spaces
    x = tierWidth * (j) 
    return x

def drawLake(app, i):
    y = app.height - (i + 1) * (app.height // len(app.world))
    util.drawBlock(app.width//4, y, 1.5*app.width, 1, 75, gradient('lightCyan', 'lightSkyBlue', 'skyBlue', 'deepSkyBlue', start = 'center'))
    if i < len(app.logs):
        logList = app.logs[i]
    drawLogs(app, logList, i)

def drawLogs(app, logList, tier):
    for xindex in range(len(logList)):
        log = logList[xindex]
        if log == 'log':
            x = snapTerrain(app, xindex)
            y = app.height - (tier + 1) * (app.height // len(app.world)) - 25
            drawLog(x, y)

def drawLog(x, y):
    util.drawBlock(x, y, 300, 15, 25, 'saddleBrown')

#drawTraintrackss
#drawTrain
def drawCollectibles(app, xindex, tier, colList):
    col = colList[xindex]
    if col != 'no':
        x = snapTerrain(app, xindex)
        y = app.height - (tier + 1) * (app.height // len(app.world)) + 50
        util.drawBorderBlock(x, y, col.width, col.height, col.depth, col.color)
    
    

"""
def getColType(obj, xindex, tier):
    if obj == 'coin':
        return Coin(app, xindex, tier)
    elif obj == 'up':
        return Powerup(app, xindex, tier)
    elif obj == 'down':
        return Powerdown(app, xindex, tier)
    return None
"""


def drawWorld(app):
    for i in range (len(app.world)):
        terrain = app.world[i]
        if i < len(app.collectibles):
            colList = app.collectibles[i]
            for xindex in range(len(colList)):
                drawCollectibles(app, xindex, i, colList)
        if terrain == 'road':
            drawRoad(app, i)
        elif terrain == 'grass':
            drawGrass(app, i)
        elif terrain == 'lake':
            drawLake(app, i)

        


def updateCollectibles(app):
    for colList in app.collectibles:
        for xindex in range(len(colList)):
            col = colList[xindex]
            if isinstance(col, Collectible):
                col.animate()
                
                    
            

        
        

