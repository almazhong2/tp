from cmu_graphics import *

class Car: #in 2D for now
    def __init__(self, x, width, height, color, speed, tier):
        self.x = 50
        self.width = width
        self.height = height
        self.color = color
        self.speed = speed 
        self.index = tier
        #self.y = app.height - (tier + 1) * (app.height // len(app.world))

    
    def move(self):
        self.x += self.speed
