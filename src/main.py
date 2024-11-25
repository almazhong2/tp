from cmu_graphics import *
import random
import util
import player
import world

def onAppStart(app):
    app.background = gradient('gray', 'gainsboro', start = 'top')
    app.width = 1600
    app.height = 1050
    app.gameMode = False
    app.playColor = 'gray'
    app.playerX = app.width//8
    app.playerY = app.height*7/8
    

def onKeyPress(app, key):
    pass

def restart(app):
    onAppStart(app)

def redrawAll(app):
    if not app.gameMode:
        util.drawMenu(app)
        util.drawStars(app)
        util.drawButtons(app)
    if app.gameMode:
        #world.drawTerrain(app)
        world.drawRoad(app)
        player.drawPlayer(app)

def onStep(app):
    app.starAngle = (app.starAngle + app.starSpeed) % 360
    if app.gameMode:
        app.background = 'paleGreen'

def onMousePress(app, mouseX, mouseY):
    if not app.gameMode:
        if util.playButton(mouseX, mouseY):
            app.gameMode = True


def onMouseMove(app, mouseX, mouseY):
    if not app.gameMode:
        if util.playButton(mouseX, mouseY):
            app.playColor = 'gainsboro'
        else:
            app.playColor = 'gray'

def onKeyPress(app, key):
    if app.gameMode:
        if key == 'up' or key == 'w':
            app.playerX += app.depth
            app.playerY -= app.depth
        elif key == 'down' or key == 's':
            app.playerX -= app.depth
            app.playerY += app.depth
        elif key == 'left' or key == 'a':
            app.playerX -= 100
        elif key == 'right' or key == 'd':
            app.playerX += 100

def main():
    runApp()

main()