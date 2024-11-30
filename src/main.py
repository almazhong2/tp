from cmu_graphics import *
import random
import util
import player
import world

def onAppStart(app):
    #menu
    app.background = gradient('gray', 'gainsboro', start = 'top')
    app.width = 1600
    app.height = 1050
    app.gameMode = False
    app.charMode = False
    app.playColor = 'gray'
    app.menuMode = True

    #player and terrain generation
    app.playerX = app.width//8
    app.playerIndex = 1
    app.playerY = player.snapTerrain(app, app.playerIndex)
    #app.playerY = app.height*7/8
    app.world = ['lake', 'road', 'road', 'grass', 'lake', 'road', 'grass', 'lake', 'road', 'grass', 'road']
    app.stepsPerSecond = 30

    #counter/timer
    app.counter = 0

def restart(app):
    onAppStart(app)

def redrawAll(app):
    if app.menuMode:
        util.drawMenu(app)
        util.drawStars(app)
        util.drawButtons(app)
    if app.gameMode:
        #world.drawTerrain(app)
        world.drawWorld(app)
        #world.drawRoad(app)
        player.drawPlayer(app)
        world.drawCar(app, 2)
    if app.charMode:
        util.drawBoard(app)


def onStep(app):
    app.counter += 1
    app.starAngle = (app.starAngle + app.starSpeed) % 360
    if app.gameMode:
        #app.background = 'paleGreen'
        if app.counter % int(app.stepsPerSecond*.75)== 0:
            app.world.append(random.choice(['grass', 'road', 'lake']))  
            app.world.pop(0)            

        """popping terrain that moves offscreen
        terrainPos = app.height // len(app.world)
        terrainTime  = app.stepsPerSecond * (app.height // terrainPos) #how long the terrain should be on screen
        if app.counter % terrainTime == 0:
            app.world.pop(0)
        """      
        
        #app.playerY += 1


def onMousePress(app, mouseX, mouseY):
    if not app.gameMode:
        if util.playButton(mouseX, mouseY):
            app.gameMode = True
            app.menuMode = False
            app.charMode = False
        elif util.charButton(mouseX, mouseY):
            app.gameMode = False
            app.charMode = True
            app.menuMode = False

def onMouseMove(app, mouseX, mouseY):
    if not app.gameMode:
        if util.playButton(mouseX, mouseY):
            app.playColor = 'gainsboro'
        else:
            app.playColor = 'gray'


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

#test on key press
"""
def onKeyPress(app, key):
    if app.gameMode:
        if key == 'up' or key == 'w':
            app.nextIndex = app.playerIndex - 1
            app.hop = True
        elif key == 'down' or key == 's':
            app.nextIndex = app.playerIndex + 1
            app.hop = True
        elif key == 'left' or key == 'a':
            app.playerX -= 100
            app.hop = False
            return
        elif key == 'right' or key == 'd':
            app.playerX += 100
            app.hop = False
            return
        
        if app.hop:
            app.hopX1, app.hopY1, app.hopX2, app.hopY2 = player.getHoppingVariables(app.playerX, app.playerY)
        #app.hopFrame = 0 maybe, maybe not!
        
"""


def main():
    runApp()

main()