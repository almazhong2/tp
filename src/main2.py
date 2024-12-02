from cmu_graphics import *
import random as py_random
import util
from player import *
import world
from Car import *

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

    app.carTimer = app.stepsPerSecond*1.25

    """
    app.playerX = player.snapTerrainX(app, app.playerXIndex)
    app.playerY = player.snapTerrainY(app, app.playerYIndex)
    """

    #app.playerY = app.height*7/8

    #starting world
    app.world = ['lake', 'road', 'road', 'grass', 'lake', 'road', 'grass', 'lake', 'road', 'grass', 'road']

    #timer events
    app.stepsPerSecond = 30
    app.counter = 0
    app.cars = []

    #player animations
    app.player = Player(0, 0, 50, app.stepsPerSecond//2)
    app.playerYIndex = len(app.world)//2
    app.playerXIndex = 7
    startX, startY = app.player.snapTerrain(app, app.playerYIndex, app.playerXIndex)
    app.player = Player(startX, startY, 50, app.stepsPerSecond//3)
    app.cars = [[] for i in range(len(app.world))]

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
    
    if app.charMode:
        util.drawBoard(app)


def onStep(app):
    app.counter += 1 #timer
    #menu changes
    app.starAngle = (app.starAngle + app.starSpeed) % 360

    if app.gameMode:     
        app.player.updateHop()
        app.player.snapTerrain(app, app.playerYIndex, app.playerXIndex)
        world.updateCars(app)


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
    terrain = py_random.choice(['grass', 'road', 'lake'])
    app.world.append(terrain)
    if terrain == 'road':
        cars = []
        totalCars = py_random.randint(2, 6)
        prevX = 0
        for _ in range(totalCars):
            colors = ['oliveDrab', 'cornflowerBlue', 'darkMagenta', 'deepPink']
            width = py_random.randint(25, 76)
            height = py_random.randint(25, 76)
            speed = 15
            x = py_random.randint(prevX - 500, prevX - 100)
            prevX = x
            cars.append(Car(x, width, height, py_random.choice(colors), speed))
        app.cars.append(cars)
    else:
        app.cars.append([])
    
    app.world.pop(0)
    app.cars.pop(0)


def main():
    runApp()
    

main()