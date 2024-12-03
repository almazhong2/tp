from cmu_graphics import *
import random as py_random

class Car: #in 2D for now
    def __init__(self, x, width, height, color, speed, index, direction):
        self.x = x
        self.width = width
        self.height = height
        self.color = color
        self.speed = speed 
        self.index = index
        self.depth = 25
        self.direction = direction
        #self.y = app.height - (tier + 1) * (app.height // len(app.world))
    
    def move(self):
        if self.direction == 'left':
            self.x -= self.speed
        else:
            self.x += self.speed
        
    
    def __repr__(self):
        return 'car'
    
    def getTier(self, app):
        y = self.y
        tierHeight = app.height // len(app.world)
        tier = ((app.height - y) // tierHeight) - 1
        if tier < 0:
            tier = 0
        elif tier >= len(app.world):
            tier = len(app.world) - 1
    
    def collision(self, player):
        xcollision = self.x + self.width >= player.x - player.width
        return xcollision and self.getTier(app) == 4
    