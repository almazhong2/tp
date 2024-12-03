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
    
    app.hopCount = 0

def restart(app):
    onAppStart(app)

def redrawAll(app):
    if app.menuMode:
        util.drawMenu(app)
        util.drawStars(app)
        util.drawButtons(app)
    if app.gameMode:
        world.drawWorld(app)
        app.player.drawPlayer(app)
        #world.drawCar(app, 2)
        drawLabel(f'Total Hops: {app.hopCount}', app.width//2, 50, size = 50, font = 'orbitron', 
                  bold = True, fill = gradient('lightBlue', 'blue', 'black', start = 'top'), 
                  borderWidth = 2, align = 'center')
        if app.gameOver:
            drawLabel('gameOver', app.width//2, app.height//2, align = 'center', size = 100)
    
    if app.charMode:
        util.drawBoard(app)


def onStep(app):
    app.counter += 1 #timer
    #menu changes
    app.starAngle = (app.starAngle + app.starSpeed) % 360
    if app.counter > app.stepsPerSecond * 100:
        app.counter = 0

    if app.gameMode:     
        app.player.updateHop()
        app.player.snapTerrain(app, app.playerYIndex, app.playerXIndex)
        world.updateCars(app)
        world.updateCollectibles(app)
        if carCollision(app):
            app.gameOver = True
        
def carCollision(app):
    for cars in app.cars:
        for car in cars:
            if car.collision(app.player):
                return True
    return False


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
    if app.gameMode:
        if key == 'up' or key == 'w':
            app.player.hop()
            updateWorld(app)
            app.hopCount += 1
            
        elif key == 'down' or key == 's':
            app.player.hop()

        elif key == 'left' or key == 'a':
            app.playerXIndex -= 1
            newX, newY = newX, newY = app.player.snapTerrain(app, app.playerYIndex, app.playerXIndex)
            app.player.x = newX
        
        elif key == 'right' or key == 'd':
            app.playerXIndex += 1
            newX, newY = newX, newY = app.player.snapTerrain(app, app.playerYIndex, app.playerXIndex)
            app.player.x = newX

def updateWorld(app):
    if app.prevTerrain == 'lake':
        terrain = py_random.choice(['grass', 'road'])
    else:
        terrain = py_random.choice(['grass', 'road', 'lake'])
    app.world.append(terrain)
    if terrain == 'road':
        cars = []
        totalCars = py_random.randint(2, 4)
        for i in range(totalCars):
            offset = 400
            colors = ['oliveDrab', 'cornflowerBlue', 'darkMagenta', 'deepPink']
            width = py_random.randint(50, 70)
            height = py_random.randint(50, 70)
            speed = 15
            x = -(i*offset)
            cars.append(Car(x, width, height, py_random.choice(colors), speed, len(app.world) - 1))
        app.cars.append(cars)
    else:
        app.cars.append([])
    
    collectibles = []
    if terrain == 'grass':
        app.greenery.append(getPlants(app))
        for index in range(15):
            if app.greenery[-1][index] != 'tree' and app.greenery[-1][index] != 'bush':
                collectibles.append(getCollectible(app, index, len(app.world) - 1))
            else:
                collectibles.append('no')
    else:
        app.greenery.append(['no'] * 15)
        collectibles = ['no']*15

    if terrain == 'lake':
        app.logs.append(getLogs(app))
        for index in range(15):
            if app.logs[-1][index] == 'log':
                collectibles[index] = getCollectible(app, py_random.randint(index, index+3), len(app.world) - 1) 
            else:
                collectibles[index] = 'no'
    else:
        app.logs.append(['no']*15)
    app.collectibles.append(collectibles)

    app.world.pop(0)
    app.cars.pop(0)
    app.greenery.pop(0)
    app.logs.pop(0)
    app.collectibles.pop(0)
    app.prevTerrain = terrain


def getLogs(app):
    logs = ['no' for xindex in range(15)]
    totalLogs = py_random.randint(1, 4)
    if totalLogs == 1:
        j = py_random.randint(5, 10)
        logs[j] = 'log'
    for _ in range(totalLogs):
        j = py_random.randint(1,7)
        if j*3 < len(app.logs):
            logs[j*3] = 'log'
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

def main():
    runApp()
    

main()