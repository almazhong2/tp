from cmu_graphics import *

class GameObject: #in 2D for now
    def __init__(self, x, y, width, height, color):
        #tentative
        self.left = x
        self.top = y
        self.right = x + width
        self.bottom = y + height

    def move(self, dx, dy):
        self.left += dx
        self.right += dx
        self.top += dy
        self.bottom += dy
    
    def outFrame(self):
        #object is out of frame
        pass

class Obstacle(GameObject):
    def __init__(self):
        super().__init__(0, 0, 30, 10, 'red') #list of obstacles later

class Collectible(GameObject):
    def __init__(self):
        super().__init__(0, 0, 10, 10, 'yellow') #collectibles will look the same


class Player(GameObject):
    def __init__(self, x, y):
        #will later have a list of players here
        super().__init__(x, y, 20, 20, 'blue')
        self.key = None

    def move_player(self, key):
        key = self.key
        if self.key == 'left' and self.left > 0:
            self.move(-5, 0)
        elif self.key == 'right' and self.right <  app.width:
            self.move(+5, 0)
        elif self.key == 'up' and self.top > 0:
            self.move(0, -5)
        elif self.key == 'down' and self.bottom < app.height:
            self.move(0, +5)
    
