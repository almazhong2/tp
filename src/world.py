from cmu_graphics import *
import util
import random as py_random #debugging strategy from chatGPT
from Car import *

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


#cars
#drawing the cars that appear on road
def drawCars(app, i):
    if i < len(app.cars):
        cars = app.cars[i]
    else:
        cars = []
    
    for car in cars:
        drawCar(app, i, car)

#drawing individual car
def drawCar(app, i, car):
    carDepth = 25
    y = app.height - (i + 1) * (app.height // len(app.world))
    util.drawBorderBlock(car.x, y, car.width, car.height, carDepth, car.color)


#depending on cars and road terrain, create these random cars and add to app.cars
def createCars(app, i):
    cars = []
    prevX = 0
    totalCars = py_random.randint(2, 6)
    for _ in range(totalCars):
        colors = ['oliveDrab', 'cornflowerBlue', 'darkMagenta', 'deepPink']
        width = py_random.randint(25, 76)
        height = py_random.randint(25, 76)
        speed = 15
        x = py_random.randint(prevX - 500, prevX - 100)
        prevX = x
        cars.append(Car(x, width, height, py_random.choice(colors), speed, i))
    
    app.cars.append(cars)

#updating car movement
def updateCars(app):
    for cars in app.cars:
        for car in cars:
            car.move() 
            #CMU CS Academy 6.3.2 Wraparound
            if car.x > app.width + car.width:
                car.x = -car.width
            
            """
            if car.index < len(app.world):
                car.y = app.height - (len(app.world) - 1 + 1) * (app.height // len(app.world))
            """


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

def drawLake(app, i):
    y = app.height - (i + 1) * (app.height // len(app.world))
    util.drawBlock(app.width//4, y, 1.5*app.width, 1, 75, gradient('lightCyan', 'lightSkyBlue', 'skyBlue', 'deepSkyBlue', start = 'center'))

def drawWorld(app):
    for i in range (len(app.world)):
        terrain = app.world[i]
        if terrain == 'road':
            drawRoad(app, i)
            drawDashes(app, i)
            drawCars(app, i)
        elif terrain == 'grass':
            drawGrass(app, i)
        elif terrain == 'lake':
            drawLake(app, i)

