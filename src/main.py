from cmu_graphics import *
import random
import util

def onAppStart(app):
    app.background = gradient('gray', 'gainsboro', start = 'top')
    app.width = 1600
    app.height = 1050

def onKeyPress(app, key):
    pass

def restart(app):
    onAppStart(app)

def redrawAll(app):
    util.drawMenu(app)
    util.drawStars(app)
    util.drawButtons(app)

    


    

def onStep(app):
    app.starAngle = (app.starAngle + app.starSpeed) % 360

def main():
    runApp()

main()