class GameObject: #in 2D for now
    def __init__(self, x, y, width, height, color):
        self.shape = Rect(x, y, width, height, fill = color) #tentative, do i need this for later?
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
    pass

class Player(GameObject):
    def __init__(self, x, y):
        #will later have a list of players here
        super().__init__()

class Game:
    pass

