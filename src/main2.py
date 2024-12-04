from cmu_graphics import *
import random as py_random
import util
from player import *
import world
from Car import *
from Collectible import *


def onAppStart(app):
    #menu starters
    app.background = gradient('gray', 'gainsboro', start = 'top')
    app.width = 1600
    app.height = 1050
    
    #modes
    app.gameMode = False
    app.charMode = False
    app.menuMode = True

    #button colors
    app.playColor = 'gray'
    app.charColor = 'gray'
    app.howColor = 'gray'

    #terrain generation
    app.cars = [[] for i in range(len(app.world))]
    app.greenery = [[] for i in range(len(app.world))]
    app.logs = [[] for i in range(len(app.world))]
    app.collectibles = [[] for i in range(len(app.world))]
    app.prevTerrain = None
    #app.playerY = app.height*7/8

    #starting world
    app.world = ['grass', 'road', 'road', 'grass', 'grass', 'road', 'grass', 'grass', 'road', 'grass', 'road']
    app.seen = []

    #timer events
    app.stepsPerSecond = 30
    app.counter = 0
    app.gameOver = False


    #player animations
    app.player = Player(0, 0, 50, app.stepsPerSecond//2)
    app.playerYIndex = len(app.world)//2
    app.playerXIndex = 7
    startX, startY = app.player.snapTerrain(app, app.playerYIndex, app.playerXIndex)
    app.player = Player(startX, startY, 50, app.stepsPerSecond//5)
    
    #game counts
    app.hopCount = 0
    app.coinCount = 0
    app.backCount = 5 
    
    

def restart(app):
    onAppStart(app)

def redrawAll(app):
    if app.menuMode:
        util.drawMenu(app)
        util.drawStars(app)
        util.drawButtons(app)
    if app.gameMode:
        world.drawWorld(app)
        for i in range (len(app.world)):
            terrain = app.world[i]
            if terrain == 'road' and i < len(app.cars):
                world.drawCars(app, app.cars[i], i)
        app.player.drawPlayer(app)
        #world.drawCar(app, 2)
        drawLabel(f'Back Hops Left: {app.backCount}', app.width*.25, 50, size = 50, font = 'orbitron', 
                  bold = True, fill = 'black', 
                  borderWidth = 2, align = 'center')
        
        drawLabel(f'Total Hops: {app.hopCount}', app.width//2, 50, size = 50, font = 'orbitron', 
                  bold = True, fill = 'black', 
                  borderWidth = 2, align = 'center')
        
        drawLabel(f'Coins: {app.coinCount}', app.width*.75, 50, size = 50, font = 'orbitron', 
                  bold = True, fill = 'black', 
                  borderWidth = 2, align = 'center')
        
        if app.gameOver:
            drawLabel('gameOver', app.width//2, app.height//2, align = 'center', size = 100)
    if app.charMode:
        util.drawBoard(app)


def onStep(app):
    app.counter += 1 #timer
    #menu changes
    app.starAngle = (app.starAngle + app.starSpeed) % 360
    if app.counter%app.stepsPerSecond * 3 == 0:
        app.gameOver = False
        

    if app.gameMode:    
        app.player.updateHop()
        app.player.snapTerrain(app, app.playerYIndex, app.playerXIndex)        
        world.updateCars(app)
        world.updateCollectibles(app)
        #correctCols(app)
        #popCollectibles(app, app.player)

    
        #if carCollision(app, app.player) and not app.player.isHopping:
            #app.gameOver = True
        
        
        
def carCollision(app, obj):
    for index in range(len(app.cars)):
        cars = app.cars[index]
        for xindex in range(len(cars)):
            car = cars[xindex]
            if util.collision(obj, car):
                return True
    return False


def distance(x0, y0, x1, y1):
    # Use the distance formula to find the distance
    # from the point (x0, y0) to the point (x1, y1)
    return ((x1 - x0)**2 + (y1 - y0)**2)**0.5
"""
def updateCollectibleList(app):
    for colList in app.collectibles:
        for xindex in range(len(colList)):
            col = colList[xindex]
            if col != 'no' and col.collect(app, app.player):
                colList[xindex] = 'no'
"""
    
def onMousePress(app, mouseX, mouseY):
    if app.menuMode:
        if util.playButton(mouseX, mouseY):
            app.gameMode = True
            app.menuMode = False
            app.charMode = False
        elif util.charButton(mouseX, mouseY):
            app.gameMode = False
            app.charMode = True
            app.menuMode = False
    
    if app.charMode:
        app.background = 'lightSkyBlue'


def onMouseMove(app, mouseX, mouseY):
    if app.menuMode:
        if util.playButton(mouseX, mouseY):
            app.playColor = 'gainsboro'
        else:
            app.playColor = 'gray'
        
        if util.charButton(mouseX, mouseY):
            app.charColor = 'gainsboro'
        else:
            app.charColor = 'gray'

#test on key press
def onKeyPress(app, key):
    popCols(app)
    if app.gameMode:
        if (key == 'up' or key == 'w') and forwardLegal(app):
            if inWater(app, key):
                app.gameOver = True
            app.player.hop()
            updateWorld(app)
            app.hopCount += 1
            app.backCount = 5 
            
        elif (key == 'down' or key == 's') and backwardLegal(app):
            reverseWorld(app)
            if app.backCount > 0:
                app.backCount -=1
            else:
                app.backCount = 0
            app.hopCount -= 1
            app.player.hop()

        elif (key == 'left' or key == 'a') and leftLegal(app):
            if inWater(app, key):
                app.gameOver = True
            app.playerXIndex -= 1
            newX, newY = newX, newY = app.player.snapTerrain(app, app.playerYIndex, app.playerXIndex)
            app.player.x = newX
        
        elif (key == 'right' or key == 'd') and rightLegal(app):
            if inWater(app, key):
                app.gameOver = True
            app.playerXIndex += 1
            newX, newY = newX, newY = app.player.snapTerrain(app, app.playerYIndex, app.playerXIndex)
            app.player.x = newX


def reverseWorld(app):
    if len(app.seen) > 0:
        lastTier = app.seen[-1]
        app.world.insert(0, lastTier['world'])
        app.collectibles.insert(0, lastTier['cols'])
        app.greenery.insert(0, lastTier['plants'])
        app.logs.insert(0, lastTier['logs'])
        app.cars.insert(0, lastTier['cars'])

        app.world.pop()
        app.collectibles.pop()
        app.greenery.pop()
        app.logs.pop()
        app.cars.pop()
        app.seen.pop()
    else:
        app.gameOver = True

def backwardLegal(app):
    tier = 5
    plantList = app.greenery[tier - 2]    
    for xindex in range(len(plantList)):
        plant = plantList[xindex]
        if plant =='bush' or plant == 'tree':
            x = world.snapTerrain(app, xindex)
            if abs(app.player.x - x) == 0:
                return False
    if app.backCount == 0:
        app.gameOver = True
    return app.backCount > 0

def inWater(app, key):
    if key in ['up','w']:
        tier = 5
        if app.world[tier] == 'lake':
            logList = app.logs[tier]
            index = app.playerXIndex 
            if index < len(logList):
                log = logList[index]
                if log == 'no' and logList[index + 1] == 'no' and logList[index - 1] == 'no':
                    return True
    elif key in ['right', 'd']:
        tier = 3
        if app.world[tier + 1] == 'lake':
            logList = app.logs[tier + 1]
            index = app.playerXIndex + 1
            if index < len(logList):
                log = logList[index]
                if log == 'no':
                    if index + 1 < len(logList) and logList[index + 1] == 'log':
                        return False
                    elif logList[index - 1] == 'no':
                        return True
                
    elif key in ['left', 'a']:
        tier = 3
        if app.world[tier + 1] == 'lake':
            logList = app.logs[tier + 1]
            index = app.playerXIndex 
            if index < len(logList):
                log = logList[index]
                if log == 'no':
                    if logList[index - 2] == 'log':
                        return False
                    elif logList[index - 1] == 'no':
                        return True
    return False


def forwardLegal(app):
    tier = 5
    plantList = app.greenery[tier]    
    for xindex in range(len(plantList)):
        plant = plantList[xindex]
        if plant =='bush' or plant == 'tree':
            x = world.snapTerrain(app, xindex)
            if abs(app.player.x - x) == 0:
                return False
    return True        

def rightLegal(app):
    tier = 4
    plantList = app.greenery[tier]
    for xindex in range(len(plantList)):
        plant = plantList[xindex]
        newX, newY = app.player.snapTerrain(app, app.playerYIndex, app.playerXIndex + 1)
        if plant =='bush' or plant == 'tree':
            x = world.snapTerrain(app, xindex)
            if abs(newX - x) == 0:
                return False
    return True

def leftLegal(app):
    tier = 4
    plantList = app.greenery[tier]
    for xindex in range(len(plantList)):
        plant = plantList[xindex]
        newX, newY = app.player.snapTerrain(app, app.playerYIndex, app.playerXIndex - 1)
        if plant =='bush' or plant == 'tree':
            x = world.snapTerrain(app, xindex)
            if abs(newX - x) == 0:
                return False
    return True

def getTier(app, y): 
    tierHeight = app.height // len(app.world) 
    yindex = int((app.height - y) // tierHeight)

    return yindex

def popCols(app):
     for tier in range(len(app.collectibles)):
        colList = app.collectibles[tier]
        for xindex in range(len(colList)):
            col = colList[xindex]
            if isinstance(col, Collectible):
                x1 = getXIndex(app, col.x)
                x2 = getXIndex(app, app.player.x)
                y = app.height - (tier + 1) * (app.height // len(app.world)) + 50
                if x1 == x2 and int(abs(app.player.y - y)) < 25:
                    app.collectibles[tier][xindex] = 'no'

                    if type(col) == Coin:
                        app.coinCount += 1
                    """
                    elif type(col) == Powerup:
                        util.powerUp(app)
                    elif type(col) == Powerdown:   
                    """
                                 
    
    

def correctCols(app):
    for tier in range(len(app.collectibles)):
        colList = app.collectibles[tier]
        for xindex in range(len(colList)):
            col = colList[xindex]
            if isinstance(col, Collectible):
                x1 = getXIndex(app, col.x)
                logY = app.height - (tier + 1) * (app.height // len(app.world)) - 25
                colY = app.height - (tier + 1) * (app.height // len(app.world)) + 50
                plantY = app.height - (tier + 1) * (app.height // len(app.world)) - 40
                if x1 + 1 < len(app.logs[tier]):
                    if app.logs[tier][x1] != 'log':
                        app.collectibles[tier][x1] = 'no'
                elif app.greenery[tier][x1] == 'no':
                    app.collectibles[tier][x1] = 'no'
    """
    telling if a collectible is on a log
    if (log index + 3) - collectible x index >= 0
    if ys match
    """

def getXIndex(app, x):
    tierWidth = app.width//15  
    xindex = int(x//tierWidth)
    return xindex


def updateWorld(app):
    maxBackward = 5
    if len(app.seen) == maxBackward:
        app.seen.pop(0)

    prevTier = {'world': app.world[0], 
                'cols': app.collectibles[0],
                'plants': app.greenery[0],
                'logs': app.logs[0],
                'cars': app.cars[0]
                }
    app.seen.append(prevTier)

    if app.prevTerrain == 'lake':
        terrain = py_random.choice(['grass', 'road'])
    else:
        terrain = py_random.choice(['grass', 'road', 'lake'])


    if terrain == 'road':
        cars = []
        totalCars = py_random.randint(2, 4)
        direction = py_random.choice(['left', 'right'])
        if direction == 'right':
            for i in range(totalCars):
                offset = 400
                colors = ['oliveDrab', 'cornflowerBlue', 'darkMagenta', 'deepPink']
                width = py_random.randint(50, 130)
                height = py_random.randint(50, 70)
                speed = 15
                x = -(i*offset)
                cars.append(Car(x, width, height, py_random.choice(colors), speed, len(app.world) - 1, direction))
        else:
            for i in range(totalCars):
                offset = 400
                colors = ['oliveDrab', 'cornflowerBlue', 'darkMagenta', 'deepPink']
                width = py_random.randint(50, 130)
                height = py_random.randint(20, 70)
                speed = 15
                x = app.width + (i*offset)
                cars.append(Car(x, width, height, py_random.choice(colors), speed, len(app.world) - 1, direction))
        app.cars.append(cars)
    else:
        app.cars.append([])
    
    collectibles = ['no'] * 15
    if terrain == 'grass':
        app.greenery.append(getPlants(app))
        for index in range(15):
            if app.greenery[-1][index] == 'no':
                collectibles[index] = getCollectible(app, index, len(app.world) - 1)
    else:
        app.greenery.append(['no'] * 15)

    
    if terrain == 'lake':
        app.logs.append(getLogs(app))
        for index in range(15):
            if app.logs[-1][index] == 'log':
                #collectibles[index] = getCollectible(app, py_random.randint(index, index+3), len(app.world) - 1)
                collectibles[index] = getCollectible(app, index, len(app.world) - 1) 
    else:
        app.logs.append(['no']*15)

    app.collectibles.append(collectibles)
    app.world.pop(0)
    app.collectibles.pop(0)
    app.greenery.pop(0)
    app.logs.pop(0)
    app.cars.pop(0)
    
    
    app.world.append(terrain)
    app.prevTerrain = terrain


def getLogs(app):
    logs = ['no' for xindex in range(15)]
    totalLogs = py_random.randint(1, 3)
    if totalLogs == 1:
        j = py_random.randint(5, 10)
        logs[j] = 'log'
        if j + 10 < 12:
            logs[j + 10] = 'log'
        else:
            logs[py_random.choice([3,7,10])] = 'log'
    for _ in range(totalLogs):
        j = py_random.randint(1,7)
        if j*3 < 15:
            logs[j*3] = 'log'
        else:
            logs[py_random.choice([3,7,10])] = 'log'
    return logs

def getPlants(app):
    greenery = ['no' for xindex in range(15)]
    greenCount = py_random.randint(1, 4)
    green = ['tree', 'bush']
    
    for _ in range(greenCount):
        j = py_random.randint(0, 15)
        if j < len(app.greenery):
            greenery[j] = py_random.choice(green)
    return greenery

def getCollectible(app, xindex, tier):
    chances = ['0']*9 + ['1']
    choice = py_random.choice(chances)
    types = ['coin']*12 + ['up', 'down']
    obj = 'no'
    if choice == '1':
        colType = py_random.choice(types)
        if colType == 'coin':
            obj = Coin(app, xindex, tier)
        elif colType == 'up':
            obj = Powerup(app, xindex, tier)
        elif colType == 'down':
            obj = Powerdown(app, xindex, tier)
    return obj

def transformWorld(app):
    choice = py_random.choice(['grass', 'road'])
    app.world = [py_random.choice(['grass', 'road'])]*4 + ['grass'] + [py_random.choice(['grass', 'road'])]*6


def main():
    runApp()
    

main()