from cmu_graphics import *
import random
import util

def onAppStart(app):
    app.background = gradient('gray', 'gainsboro', start = 'top')
    app.width = 800
    app.height = 800

def onKeyPress(app, key):
    pass

def restart(app):
    onAppStart(app)

def redrawAll(app):
    #drawLabel("I am going to crash out", 200, 200, size = 24, bold = True)

    util.drawMenu(app)

def onStep(app):
    pass

def main():
    runApp()

main()