from cmu_graphics import *

class Car: #in 2D for now
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def drawCar(app, i):
    colors = ['oliveDrab', 'cornflowerBlue', 'darkMagenta', 'deepPink']
    width = random.randint(25, 75)
    height = random.randint(25, 75)
    depth = 25
    y = app.height - (i + 1) * (app.height // len(app.world))
    util.drawBorderBlock(50, y, width, height, depth, random.choice(colors))    