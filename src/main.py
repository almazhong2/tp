from cmu_graphics import *
import random as py_random
import util
from player import *
import world

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
    startX, startY = app.player.snapTerrain(app, 0, 1)
    app.player = Player(startX, startY, 50, app.stepsPerSecond//2)
    app.playerYIndex = 1
    app.playerXIndex = 0

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
        if app.counter % int(app.stepsPerSecond*.75)== 0:
            terrain = py_random.choice(['grass', 'road', 'lake'])
            app.world.append(terrain)
            #if terrain == 'road':
                #world.createCars(app, len(app.world) - 1)
            app.world.pop(0)
    
        app.player.updateHop()
        
        #world.updateCars(app)
    
    if app.carTimer > 0:
        app.carTimer -= 1

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

"""
def onKeyPress(app, key):
    if app.gameMode:
        if key == 'up' or key == 'w':
            app.playerX += app.depth*1.2
            app.playerY -= app.depth*1.2
        elif key == 'down' or key == 's':
            app.playerX -= app.depth*1.2
            app.playerY += app.depth*1.2
        elif key == 'left' or key == 'a':
            app.playerX -= 100
        elif key == 'right' or key == 'd':
            app.playerX += 100
"""

#test on key press

def onKeyPress(app, key):
    if app.gameMode:
        if key == 'up' or key == 'w':
            app.playerYIndex += 1
            app.playerXIndex += 1
            newX, newY = app.player.snapTerrain(app, app.playerYIndex, app.playerXIndex)
            app.player.hop(newX, newY)

        elif key == 'down' or key == 's':
            app.playerYIndex -= 1
            app.playerXIndex -= 1
            newX, newY = app.player.snapTerrain(app, app.playerYIndex, app.playerXIndex)
            app.player.hop(newX, newY)
  

        elif key == 'left' or key == 'a':
            app.playerXIndex -= 1
            newX, newY = newX, newY = app.player.snapTerrain(app, app.playerYIndex, app.playerXIndex)
            app.player.x = newX
        
        elif key == 'right' or key == 'd':
            app.playerXIndex += 1
            newX, newY = newX, newY = app.player.snapTerrain(app, app.playerYIndex, app.playerXIndex)
            app.player.x = newX
        
        """
        if app.hop:
            app.hopX1, app.hopY1, app.hopX2, app.hopY2 = player.getHoppingVariables(app.playerX, app.playerY)
        #app.hopFrame = 0 maybe, maybe not!
        """


def main():
    runApp()

main()