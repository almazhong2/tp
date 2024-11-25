from cmu_graphics import *
import math

#3D projection (~2.5D): from CMU CS Academy 3D graphics video
app.x, app.y, app.z = 0.25, 2, 3

app.verticalView = -30
app.horizontalView = 0

#converting 3D points in 2D points
#mathematical formula from https://en.wikipedia.org/wiki/3D_projection
def convert2D(point, x, y, z):
    aX, aY, aZ = point
    cX, cY, cZ = x, y, z

    #angles for a the correct view
    xAngle = app.horizontalView
    yAngle = app.verticalView

    thetaX, thetaY = yAngle, xAngle
    eX, eY, eZ = (app.width//2, app.height//2, min(app.width, app.height) * 0.714) #eye position
    x, y, z = aX - cX, aY - cY, aZ - cZ #translated point

    cX = dcos(thetaX)
    cY = dcos(thetaY)

    sX = dsin(thetaX)
    sY = dsin(thetaY)

    dX = cY * x - sY * z
    dY = sX * (cY * z + sY * x) + cX * y
    dZ = cX * (cY * z + sY * x) - sX * y

    if dZ == 0 or dZ < -30:
        return [None, None]
    
    elif dZ > 0:
        return [None, None]
    
    bX = eZ/dZ * dX + eX
    bY = eZ/dZ * dY + eY

    return [bX, bY]

def drawPlane(corners, color):
    #corners is a list of 4 3D coordinates
    #convert each point in corners to a 2D point
    newCorners = []
    for point in corners:
        newPoint  = convert2D(point, app.x, app.y, app.z)
        newCorners += newPoint

    #draw a polygn with the new 2D corners
    Polygon(*newCorners, fill = color, border = 'black')
    

def drawBlock3D(length, width, height, color):
    #draw top, front, and right side (points in (x, y, z))
    if app.z > 0:
        front = [(0, 0, width),
                (length, 0, width),
                (length, height, width), 
                (0, height, width)
                ]
    else:
        front = [ (0, 0, 0),
                (length, 0, 0),
                (length, height, 0),
                (0, height, 0)
        ]
    drawPlane(front, color)


    top = [(0, height, 0),
           (length, height, 0),
           (length, height, width), 
           (0, height, width)
           ]
    drawPlane(top, color)

def drawMenu(app):
    drawImage('src/krossykartlogo.png', app.width//2, app.height//3, align = 'center')

#15112 Homework Fancy Wheel Inspired
#star variables
app.starAngle = 90
app.starRadius = app.height*0.8 - 50
app.starSpeed = 5

app.starX = app.width
app.starY = app.height
app.starWidth = app.width //2
app.starHeight = app.height//2

def getRadiusEndpoint(cx, cy, r, theta):
    return (cx + r*math.cos(math.radians(theta)),
            cy - r*math.sin(math.radians(theta)))

def drawStars(app):
    x, y = getRadiusEndpoint(app.starX, app.starY, app.starRadius, app.starAngle)
    drawImage('src/star.png', x - app.starWidth // 2, y - app.starHeight//2, width = app.starWidth, height = app.starHeight)

#print(getImageSize('src/star.png'))

app.playLeft = app.width/3.2 + 100
app.playTop = app.height*0.5
app.playWidth = app.width//4
app.playHeight = app.height*0.1


def drawButtons(app):
    drawRect(app.width/3.2 + 100, app.height*0.5, 
             app.width//4, app.height*0.1, 
             fill = app.playColor, border = 'black')
    drawLabel('Start', app.width/3.2 + 100 + (app.width//4) // 2, app.height*0.5 + (app.height*.1)//2, 
              size = app.height*.05, font = 'arial', bold = True, fill = 'paleTurquoise', align = 'center')
    drawRect(app.width/3.2 + 100, app.height*0.625, 
             app.width//4, app.height*0.1, 
             fill = 'gray', border = 'black')
    drawLabel('Characters', app.width/3.2 + 100 + (app.width//4) // 2, app.height*0.625 + (app.height*.1)//2, 
              size = app.height*.05, font = 'arial', bold = True, fill = 'paleTurquoise', align = 'center')
    drawRect(app.width/3.2 + 100, app.height*0.75, 
             app.width//4, app.height*.1, 
             fill = 'gray', border = 'black')
    drawLabel('How to Play', app.width/3.2 + 100 + (app.width//4) // 2, app.height*0.75 + (app.height*.1)//2, 
              size = app.height*.05, font = 'arial', bold = True, fill = 'paleTurquoise', align = 'center')

#CS academy intersection conditions (4.3.5)    
def playButton(mouseX, mouseY):
    right = app.width/3.2 + 100 + app.width//4
    bottom = app.height*0.5 + app.height*0.1
    if (app.width/3.2 + 100 <= mouseX <= right) and (app.height*0.5 <= mouseY <= bottom):
        return True
    return False

def getVertices(x, y, width, height, depth):
    w, h = width//2, height//2
    
    #adjust away from center point by half of each dimension's size
    #base vertices
    bottomFrontLeft = (x - w, y + h) 
    bottomFrontRight = (x + w, y + h)
    bottomBackRight = (x + w + depth, y + h - depth)
    bottomBackLeft = (x - w + depth, y + h - depth)
    
    #top vertices
    topFrontLeft = (x - w, y - h)
    topFrontRight = (x + w, y - h)
    topBackRight = (x + w + depth, y - h - depth)
    topBackLeft = (x - w + depth, y - h - depth)

    vertex = [bottomFrontLeft, bottomFrontRight,
            bottomBackRight, bottomBackLeft,
            topFrontLeft, topFrontRight,
            topBackRight, topBackLeft
            ]
    
    return [bottomFrontLeft, bottomFrontRight,
            bottomBackRight, bottomBackLeft,
            topFrontLeft, topFrontRight,
            topBackRight, topBackLeft
            ]

#new way: draw 3 polygons using depth perception
def drawBlock(x, y, width, height, depth, color):
    vertices = getVertices(x, y, width, height, depth)

    #dictionary of 3 sides visible, and the index of vertex to access from vertices
    faceVertices = {'front': [0, 1, 5, 4],
                    'top': [4, 5, 6, 7],
                    'side': [1, 2, 6, 5]
                    }
    
    for side in faceVertices:
        indexList = faceVertices[side]
        points = [] 
        for index in indexList:
            vx, vy = vertices[index]
            points.extend([vx, vy]) #in format for polygon
        drawPolygon(*points, fill = color, border = 'black')

"""
    Label(value, centerX, centerY, size=12, font='arial', bold=False,
      italic=False, fill='black', border=None, borderWidth=2, opacity=100,
      rotateAngle=0, align='center', visible=True)
"""

